"""What the probes and watches of the-way's environment facts share (WAY-81, WAY-82, WAY-91).

The checks of each fact stand in `probes/<identifier>/`, and its method
runs them, from the root of the repository:

    python -B gate/run_tests.py probes/<identifier> --record .runs/fact-<identifier>.jsonl

A check takes what it needs of its fact — the address and passages of *Source*, the release
*Holds for* names — from the fact's entry in `foundations/environment_facts.md`, looked up by
identifier and read with the parser of the facts guard, so that nothing of the entry is copied
into a check.

Verdicts, as the test runner reads a test's outcome:

- the world says something other than the fact: the test fails, and the runner records `fail`;
- no verdict — the network failed, a page could not be read, git could not run: the test skips
  with the reason, the runner records no verdict and a line naming why, and the gate reads
  `error`, never `fail`;
- a probe whose tool runs a release outside *Holds for*, and whose behaviour agreed with the fact:
  the test skips with the reason the template lists for `unchecked`, naming the release it ran on
  (WAY-91). The runner writes no `unchecked` yet, so the line holds the reason in its
  `description` while the gate reads the fact as it reads any skip. A failure names the release
  first in its message, which the runner writes into the `description` of the line; a pass line
  holds no `description`, so a pass records no release.

Standard library only (WAY-38, WAY-89); the only program started is git, every call of it with
`-c core.ignorecase=false` and with no configuration of the machine it runs on (WAY-81). A page is
fetched with `urllib`, with no cookie and no header but a user agent that names no person, machine,
product or version, the same on every machine: GitHub's API refuses a request that sends none.
"""

import html
import html.parser
import importlib.util
import json
import os
import re
import subprocess
import tempfile
import unittest
import urllib.error
import urllib.request
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
FACTS_FILE = os.path.join(ROOT, "foundations", "environment_facts.md")
GUARD_FILE = os.path.join(ROOT, "elements", "environment-facts", "format_guard.py")

# How long a page may take to answer before the check gives no verdict.
TIMEOUT = 60
# The one header a request sends: a user agent that identifies nobody.
USER_AGENT = "fact-probe"
# The reason for `unchecked` the template lists for a probe on another release (WAY-91, WAY-63).
OUTSIDE_HOLDS_FOR = "a probe ran on a release of its tool outside *Holds for*"


def _load_guard():
    spec = importlib.util.spec_from_file_location("environment_facts_format_guard", GUARD_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


guard = _load_guard()


# --- the entry ------------------------------------------------------------------------------


class NoVerdict(unittest.SkipTest):
    """A check could not reach a verdict: the network, a page, the entry or git failed it. It is
    a skip, so that the runner records no verdict and the gate reads `error`, never `fail`."""

    def __init__(self, reason):
        super().__init__("no verdict: %s" % reason)


def entry(identifier):
    """The fact's entry in foundations/environment_facts.md."""
    with open(FACTS_FILE, encoding="utf-8") as handle:
        facts = guard.facts_of(handle.read(), guard.read_rules())
    found = facts.entries.get(identifier)
    if found is None:
        raise NoVerdict("foundations/environment_facts.md holds no entry `%s`" % identifier)
    return found


def field_value(identifier, name):
    return guard.flat(guard.value_of(entry(identifier), name)[0])


class Page:
    """A page *Source* cites: its address and the passages quoted from it, with their places."""

    def __init__(self, address):
        self.address = address
        self.passages = []          # (place, passage)


def cited_pages(identifier):
    """Every page the fact's *Source* cites, in the form WAY-80 gives a cited page."""
    source = field_value(identifier, "Source")
    passage = re.compile(r"(?:§ (%s) — )?(%s)" % (guard._PLACE, guard._PASSAGE))
    pages = []
    for cited in re.finditer(guard._CITED, source):
        text = cited.group(0)
        page = Page(re.match(guard._URL, text).group(0))
        rest = text[len(page.address):]
        archived = re.match(r" \(archived: %s, %s\)" % (guard._URL, guard.DATE), rest)
        if archived:
            rest = rest[archived.end():]
        rest = re.sub(r"; read %s$" % guard.DATE, "", rest)
        place = None
        for found in passage.finditer(rest):
            place = found.group(1) or place
            page.passages.append((place, found.group(2)[1:-1]))
        pages.append(page)
    if not pages:
        raise NoVerdict("the *Source* of `%s` cites no page" % identifier)
    return pages


def named_release(identifier, tool):
    """The release of a tool the fact's *Holds for* names, as `2.55.0`."""
    holds = field_value(identifier, "Holds for")
    found = re.search(r"\b%s (\d+(?:\.\d+)+)\b" % re.escape(tool), holds)
    if found is None:
        raise NoVerdict("the *Holds for* of `%s` names no release of %s" % (identifier, tool))
    return found.group(1)


# --- pages ----------------------------------------------------------------------------------


def fetch(address):
    """(status, content type, body) of an anonymous GET, sent with no header but USER_AGENT. A
    status other than 2xx is returned, never raised; a network failure raises NoVerdict."""
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", USER_AGENT)]
    try:
        with opener.open(urllib.request.Request(address), timeout=TIMEOUT) as answer:
            return answer.status, answer.headers.get("Content-Type", ""), answer.read()
    except urllib.error.HTTPError as answer:
        return answer.code, answer.headers.get("Content-Type", ""), b""
    except (urllib.error.URLError, OSError, ValueError) as problem:
        raise NoVerdict("%s could not be read: %s" % (address, getattr(problem, "reason", problem)))


def read_page(address):
    """The body of a page that answers 200; any other answer leaves the check without a verdict."""
    status, kind, body = fetch(address)
    if status != 200:
        raise NoVerdict("%s answered HTTP %d" % (address, status))
    return kind, body


def collapse(text):
    return " ".join(text.split())


# Elements that start or end a run of text, and elements whose content a reader never sees.
BLOCKS = {"address", "article", "aside", "blockquote", "body", "caption", "dd", "details", "div",
          "dl", "dt", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4",
          "h5", "h6", "head", "header", "hr", "html", "li", "main", "nav", "ol", "p", "pre",
          "section", "summary", "table", "tbody", "td", "tfoot", "th", "thead", "title", "tr",
          "ul"}
HIDDEN = {"script", "style", "template", "noscript"}


class _Runs(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.runs, self.current, self.hidden = [], [], 0

    def close_run(self):
        text = collapse("".join(self.current))
        if text:
            self.runs.append(text)
        self.current = []

    def handle_starttag(self, tag, attributes):
        if tag in HIDDEN:
            self.hidden += 1
        elif tag in BLOCKS:
            self.close_run()
        elif tag == "br":
            self.current.append(" ")

    def handle_endtag(self, tag):
        if tag in HIDDEN:
            self.hidden = max(0, self.hidden - 1)
        elif tag in BLOCKS:
            self.close_run()

    def handle_data(self, data):
        if not self.hidden:
            self.current.append(data)


def html_runs(body, kind):
    """The runs of text of an HTML page as a reader sees them — a paragraph, a list item, a table
    cell, a heading — with markup dropped and whitespace collapsed."""
    charset = re.search(r"charset=([\w-]+)", kind or "")
    parser = _Runs()
    parser.feed(body.decode(charset.group(1) if charset else "utf-8", errors="replace"))
    parser.close()
    parser.close_run()
    return parser.runs


_STREAM = re.compile(rb"(?<!end)stream\r?\n")
_LITERAL = re.compile(rb"\((?:\\.|[^\\()])*\)", re.S)
_ESCAPES = {ord("n"): b"\n", ord("r"): b"\r", ord("t"): b"\t", ord("b"): b"\b", ord("f"): b"\f",
            0x0a: b"", 0x0d: b""}


def _unescape(literal):
    out, index = bytearray(), 0
    while index < len(literal):
        byte = literal[index]
        index += 1
        if byte != 0x5c or index >= len(literal):
            out.append(byte)
            continue
        following = literal[index]
        index += 1
        if 0x30 <= following <= 0x37:
            digits = bytes([following])
            while len(digits) < 3 and index < len(literal) and 0x30 <= literal[index] <= 0x37:
                digits += bytes([literal[index]])
                index += 1
            out.append(int(digits, 8) & 0xFF)
        else:
            out += _ESCAPES.get(following, bytes([following]))
    return bytes(out)


def pdf_runs(body):
    """The text of each content stream of a PDF as a reader sees it: the strings its text
    operators show, in order, with whitespace collapsed. Only the Flate streams and the literal
    strings of simple fonts are read; a string a composite font shows in hex is not."""
    runs = []
    for start in _STREAM.finditer(body):
        end = body.find(b"endstream", start.end())
        try:
            content = zlib.decompressobj().decompress(body[start.end():end])
        except zlib.error:
            continue
        if b"BT" not in content:
            continue
        shown = [_unescape(found.group(0)[1:-1]).decode("cp1252", errors="replace")
                 for found in _LITERAL.finditer(content)]
        text = collapse("".join(shown))
        if text:
            runs.append(text)
    return runs


def page_runs(address):
    kind, body = read_page(address)
    if body.startswith(b"%PDF-") or "pdf" in kind.lower():
        runs = pdf_runs(body)
    else:
        runs = html_runs(body, kind)
    if not runs:
        raise NoVerdict("%s shows no text this check can read" % address)
    return runs


def missing_passages(identifier):
    """(address, place, passage) of every passage the fact's *Source* quotes that no longer
    stands in one run of text at its address, compared as a reader sees the page."""
    missing = []
    for page in cited_pages(identifier):
        runs = page_runs(page.address)
        for place, passage in page.passages:
            wanted = collapse(passage)
            if not any(wanted in run for run in runs):
                missing.append((page.address, place, passage))
    return missing


def rfc_state(identifier):
    """The `obsoleted_by` and `updated_by` the RFC Editor publishes as data for the RFC the
    fact's *Source* cites, read beside its page: `<address>.json` for `<address>.html`."""
    address = cited_pages(identifier)[0].address
    if not re.fullmatch(r"https://www\.rfc-editor\.org/rfc/rfc\d+\.html", address):
        raise NoVerdict("%s is no page of the RFC Editor this check reads the state of" % address)
    data_address = address[:-len(".html")] + ".json"
    _, body = read_page(data_address)
    try:
        state = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as problem:
        raise NoVerdict("%s is not JSON: %s" % (data_address, problem))
    lists = {key: state.get(key) for key in ("obsoleted_by", "updated_by")} \
        if isinstance(state, dict) else {}
    if len(lists) != 2 or not all(isinstance(value, list) for value in lists.values()):
        raise NoVerdict("%s holds no list `obsoleted_by` or `updated_by`" % data_address)
    return data_address, lists


# A versioned address of a paper at arXiv, its abstract or its HTML: the paper, new-style as
# `2510.20270` or old-style as `cond-mat/0309395`, and the version.
_ARXIV_ADDRESS = re.compile(r"https://arxiv\.org/(?:abs|html)/"
                            r"(\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})v([1-9]\d*)")
# What arXiv's abstract page shows: the list of versions, one per line, and the mark on a
# version that withdraws the paper, and the notice over the abstract of a withdrawn one.
_SUBMISSION_HISTORY = re.compile(r'<div class="[^"]*\bsubmission-history\b[^"]*">(.*?)</div>',
                                 re.S)
_VERSION = re.compile(r"\[v([1-9]\d*)\]")
_WITHDRAWN_MARK = "(withdrawn)"
_WITHDRAWN_NOTICE = re.compile(r'<span class="error"[^>]*>\s*(This paper has been withdrawn[^<]*)')


def arxiv_edition(identifier):
    """(paper, version) of the edition at arXiv the fact's *Source* cites: every page it cites
    must be a versioned address of one paper, in one version."""
    editions = set()
    for page in cited_pages(identifier):
        found = _ARXIV_ADDRESS.fullmatch(page.address)
        if found is None:
            raise NoVerdict("%s is no versioned address of a paper at arXiv" % page.address)
        editions.add((found.group(1), int(found.group(2))))
    if len(editions) != 1:
        raise NoVerdict("the *Source* of `%s` cites more than one edition at arXiv: %s"
                        % (identifier, ", ".join("%sv%d" % edition for edition in
                                                  sorted(editions))))
    return editions.pop()


def arxiv_state(identifier):
    """What arXiv's own abstract page for the paper the fact cites shows, read at the address
    with no version, which shows the paper's last version: (that address, the version cited,
    the versions its submission history lists, what marks the paper withdrawn)."""
    paper, cited = arxiv_edition(identifier)
    address = "https://arxiv.org/abs/%s" % paper
    kind, body = read_page(address)
    charset = re.search(r"charset=([\w-]+)", kind or "")
    page = body.decode(charset.group(1) if charset else "utf-8", errors="replace")
    history = _SUBMISSION_HISTORY.search(page)
    if history is None:
        raise NoVerdict("%s shows no submission history this check can read" % address)
    versions, withdrawn = [], []
    for line in re.split(r"<br\s*/?>", history.group(1)):
        text = collapse(html.unescape(re.sub(r"<[^>]+>", " ", line)))
        found = _VERSION.search(text)
        if found is None:
            continue
        versions.append(int(found.group(1)))
        if _WITHDRAWN_MARK in text:
            withdrawn.append("v%s is marked %s" % (found.group(1), _WITHDRAWN_MARK))
    if not versions:
        raise NoVerdict("the submission history at %s lists no version" % address)
    notice = _WITHDRAWN_NOTICE.search(page)
    if notice:
        withdrawn.append("the page reads \"%s\"" % collapse(html.unescape(notice.group(1))))
    return address, cited, versions, withdrawn


# --- git ------------------------------------------------------------------------------------


class Repository:
    """A temporary git repository that no configuration of the machine reaches: no system or
    global configuration, no attributes or excludes file of the user, no template, no GIT_*
    variable of the environment; every call of git runs with `-c core.ignorecase=false`
    (WAY-81)."""

    def __init__(self):
        self.folder = tempfile.TemporaryDirectory(prefix="the-way-probe-")
        self.path = os.path.join(self.folder.name, "work")
        os.makedirs(self.path)
        empty = os.path.join(self.folder.name, "empty")
        open(empty, "w").close()
        self.environment = {name: value for name, value in os.environ.items()
                            if not name.upper().startswith("GIT_")}
        self.environment.update({"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": empty})
        self.settings = ["-c", "core.ignorecase=false", "-c", "core.attributesFile=" + empty,
                         "-c", "core.excludesFile=" + empty]
        self.git("init", "--quiet", "--template=")

    def close(self):
        self.folder.cleanup()

    def run(self, *arguments):
        """git's CompletedProcess; git that cannot run leaves the check without a verdict."""
        try:
            return subprocess.run(["git"] + self.settings + list(arguments), cwd=self.path,
                                  env=self.environment, capture_output=True, text=True,
                                  encoding="utf-8", errors="replace", timeout=TIMEOUT)
        except (OSError, subprocess.SubprocessError) as problem:
            raise NoVerdict("git could not run: %s" % problem)

    def git(self, *arguments):
        done = self.run(*arguments)
        if done.returncode != 0:
            raise NoVerdict("`git %s` exited %d: %s" % (" ".join(arguments), done.returncode,
                                                         collapse(done.stderr)))
        return done.stdout

    def write(self, path, text=""):
        full = os.path.join(self.path, *path.split("/"))
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)

    def release(self):
        """The release of git that runs here, as `git version` prints it: `2.55.0.windows.3`."""
        found = re.match(r"git version (\S+)", self.git("version"))
        if found is None:
            raise NoVerdict("`git version` printed no release")
        return found.group(1)

    def attributes(self, names, paths):
        """{(path, attribute): value} as `git check-attr` answers it: `set`, `unset`,
        `unspecified` or the value."""
        answer = self.git("check-attr", *names, "--", *paths)
        values = {}
        for line in answer.splitlines():
            path, name, value = line.rsplit(": ", 2)
            values[(path, name)] = value
        return values

    def ignored(self, paths):
        """The paths `git check-ignore --no-index` answers are ignored."""
        done = self.run("check-ignore", "--no-index", "--", *paths)
        if done.returncode not in (0, 1):
            raise NoVerdict("`git check-ignore` exited %d: %s" % (done.returncode,
                                                                 collapse(done.stderr)))
        return set(done.stdout.splitlines())


def built_from(release, named):
    """Whether a release git prints is the named release or a build of it, as Git for Windows
    `2.55.0.windows.3` builds git 2.55.0 (WAY-91)."""
    return release == named or re.fullmatch(r"%s\.windows\.\d+" % re.escape(named), release) \
        is not None


# --- the checks -----------------------------------------------------------------------------


class FactCheck(unittest.TestCase):
    """A check of a fact. What it cannot decide raises NoVerdict, never a failure."""

    def repository(self):
        repository = Repository()
        self.addCleanup(repository.close)
        return repository

    def judge_release(self, identifier, tool, release, differences):
        """A probe's verdict on the release it ran on (WAY-91): a difference fails the fact on
        any release, naming it; agreement counts only on the release *Holds for* names, a build
        of it included, and elsewhere leaves the fact unchecked for that reason."""
        if differences:
            self.fail("%s %s: %s" % (tool, release, "; ".join(differences)))
        named = named_release(identifier, tool)
        if not built_from(release, named):
            self.skipTest("unchecked: %s: it ran on %s %s, where *Holds for* names %s %s, and "
                          "its behaviour agreed with the fact"
                          % (OUTSIDE_HOLDS_FOR, tool, release, tool, named))

    def watch_passages(self, identifier):
        """The watch of a page: every passage the fact quotes still stands at its address."""
        missing = missing_passages(identifier)
        if missing:
            self.fail("%d passage(s) no longer stand: %s" % (len(missing), " | ".join(
                "%s § %s — \"%s\"" % found for found in missing)))

    def watch_rfc(self, identifier):
        """The watch of an RFC's state: nothing obsoletes or updates the edition."""
        address, lists = rfc_state(identifier)
        changed = ["%s: %s" % (key, ", ".join(map(str, value))) for key, value in lists.items()
                   if value]
        if changed:
            self.fail("%s publishes a change to the edition: %s" % (address, "; ".join(changed)))

    def watch_arxiv(self, identifier):
        """The watch of a paper at arXiv: its abstract page lists no version newer than the one
        the fact's *Source* cites, and does not mark the paper withdrawn (WAY-82)."""
        address, cited, versions, withdrawn = arxiv_state(identifier)
        found = []
        if cited not in versions:
            found.append("a submission history listing %s and no v%d, the version *Source* cites"
                         % (", ".join("v%d" % version for version in versions), cited))
        changed = []
        newer = sorted(version for version in versions if version > cited)
        if newer:
            changed.append("it publishes %s, newer than v%d, which *Source* cites"
                           % (", ".join("v%d" % version for version in newer), cited))
        changed += withdrawn
        if changed:
            found.append("a change to the edition: %s" % "; ".join(changed))
        if found:
            self.fail("%s shows %s" % (address, " — and ".join(found)))
