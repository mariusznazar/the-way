"""Tests of process-audit/audit_count.py, run on temporary git repositories and temporary
locations files, never on the user's own."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "audit_count.py"

GIT_ENV = dict(os.environ, GIT_AUTHOR_NAME="Tester", GIT_AUTHOR_EMAIL="tester@example.com",
               GIT_COMMITTER_NAME="Tester", GIT_COMMITTER_EMAIL="tester@example.com",
               GIT_CONFIG_NOSYSTEM="1", GIT_TERMINAL_PROMPT="0")

PIN = "0123456789abcdef0123456789abcdef01234567"
BASE = "89abcdef0123456789abcdef0123456789abcdef"

# The register of problems, as the template gives it; the tests add rows under its headers.
TEMPLATE = (HERE / "problem_register.md").read_text(encoding="utf-8")
CLASSES_HEADER = "| Class | Meaning | Added | Withdrawn |\n|---|---|---|---|\n"
ISSUES_HEADER = "| Issue | What | Fate | Fix |\n|---|---|---|---|\n"
PROBLEMS_HEADER = ("| Repository | Record | Stages | What | Class | Weight | Issue |\n"
                   "|---|---|---|---|---|---|---|\n")


def register_text(classes=(), issues=(), problems=()) -> str:
    """The template of the register with rows added under the headers of its tables."""
    text = TEMPLATE
    for header, rows in ((CLASSES_HEADER, classes), (ISSUES_HEADER, issues),
                         (PROBLEMS_HEADER, problems)):
        assert text.count(header) == 1, header
        text = text.replace(header, header + "".join(row + "\n" for row in rows))
    return text


def issue_row(name, fate="open", fix="none") -> str:
    return f"| {name} | the matter | {fate} | {fix} |"


def problem_row(repository, record, issue="none", cls="process-remark", weight="Minor") -> str:
    return f"| {repository} | {record} | author · reviewer | a lapse | {cls} | {weight} | {issue} |"


def record(pin_line=f"- Process pin: `{PIN}`", remarks="- Process remarks on the-way: none",
           extra=""):
    """A cycle record in the form of task-cycle/record_template.md."""
    return (f"# Cycle record — a task\n\n- Task source: the task document\n"
            f"- Product repository: product\n{pin_line}\n"
            f"- Target branch and base: `main`, `{BASE}`\n- Task branch: task/a\n"
            f"- Status: request open\n\n## Events\n\n| Time | Stage |\n|---|---|\n{extra}\n"
            f"## Request handoff\n\n- Request URL and status: draft\n{remarks}\n")


def split_row(line: str) -> list[str]:
    """The cells of a table row as a GFM reader splits it: a backslash escapes the character
    after it, and every other bar ends a cell."""
    cells, current, escaped = [], [], False
    for char in line.strip():
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            current.append(char)
            escaped = True
        elif char == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    return cells[1:]


class Repository:
    """A git repository whose commits are built from snapshots, without a working tree."""

    def __init__(self, root: Path):
        self.root = root
        root.mkdir(parents=True, exist_ok=True)
        self.git("init", "-q", "-b", "main")
        self.time = 1_760_000_000

    def git(self, *args, data: bytes | None = None) -> str:
        done = subprocess.run(["git", "-C", str(self.root), *args], input=data,
                              capture_output=True, env=self.env(), check=True)
        return done.stdout.decode("utf-8").strip()

    def env(self):
        when = f"{getattr(self, 'time', 1_760_000_000)} +0000"
        return dict(GIT_ENV, GIT_AUTHOR_DATE=when, GIT_COMMITTER_DATE=when)

    def blob(self, data: bytes) -> str:
        return self.git("hash-object", "-w", "--stdin", data=data)

    def tree(self, files: dict) -> str:
        """`files` maps a path to its text, bytes, or (mode, bytes) for a symbolic link."""
        here: dict[bytes, tuple[bytes, str, str]] = {}
        nested: dict[str, dict] = {}
        for path, content in files.items():
            head, _, rest = path.partition("/")
            if rest:
                nested.setdefault(head, {})[rest] = content
                continue
            mode = "100644"
            if isinstance(content, tuple):
                mode, content = content
            data = content.encode("utf-8") if isinstance(content, str) else content
            here[head.encode("utf-8")] = (mode.encode(), "blob", self.blob(data))
        for name, inner in nested.items():
            here[name.encode("utf-8")] = (b"040000", "tree", self.tree(inner))
        listing = b"".join(mode + b" " + kind.encode() + b" " + sha.encode() + b"\t" + name + b"\0"
                           for name, (mode, kind, sha) in sorted(here.items()))
        return self.git("mktree", "-z", data=listing)

    def commit(self, files: dict, message: str, *parents: str) -> str:
        self.time += 3600
        arguments = ["commit-tree", self.tree(files), "-m", message]
        for parent in parents:
            arguments += ["-p", parent]
        return self.git(*arguments)

    def commit_dated(self, files: dict, parent: str, stamp: str) -> str:
        """A commit whose author and committer lines carry `stamp` as it is, written as a raw
        object, so that a date git's own commands would refuse can stand in the history."""
        person = f"Tester <tester@example.com> {stamp} +0000"
        text = f"tree {self.tree(files)}\nparent {parent}\nauthor {person}\ncommitter {person}\n\nRaw\n"
        return self.git("hash-object", "-t", "commit", "-w", "--literally", "--stdin",
                        data=text.encode("utf-8"))

    def branch(self, name: str, commit: str) -> None:
        self.git("update-ref", f"refs/heads/{name}", commit)

    def cycle(self, folder: str, files: dict, base_files: dict | None = None,
              parent: str | None = None, branch: str | None = "main") -> tuple[str, str]:
        """A commit that adds the copy of a record under docs/task-cycles/<folder>/ and the next
        that removes it; returns both."""
        base_files = base_files or {"README.md": "a product\n"}
        if parent is None:
            parent = self.commit(base_files, "Start")
        copy = {**base_files, **{f"docs/task-cycles/{folder}/{name}": content
                                 for name, content in files.items()}}
        added = self.commit(copy, "Add the record", parent)
        removed = self.commit(base_files, "Remove the record", added)
        if branch:
            self.branch(branch, removed)
        return added, removed


class AuditCountCase(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.home = Path(self.temporary.name)
        self.results = self.home / "results"
        self.results.mkdir()
        self.register = self.home / "register.md"
        self.register.write_text(TEMPLATE, encoding="utf-8")
        self.locations = self.home / "locations.json"

    def tearDown(self):
        self.temporary.cleanup()

    def repository(self, name="product") -> Repository:
        return Repository(self.home / "repos" / name)

    def write_locations(self, data) -> None:
        text = data if isinstance(data, str) else json.dumps(data)
        self.locations.write_text(text, encoding="utf-8")

    def places(self, **repositories) -> dict:
        """A locations file's content: the-way's two places and each named repository."""
        data = {"the-way": {"problem_register": str(self.register),
                            "audit_results": str(self.results)}}
        for key, repository in repositories.items():
            data.setdefault(key, {})["repository"] = str(repository.root)
        return data

    def run_count(self, *arguments, locations=True, timeout=120):
        command = [sys.executable, "-B", str(SCRIPT)]
        if locations:
            command += ["--locations", str(self.locations)]
        try:
            return subprocess.run(command + list(arguments), capture_output=True,
                                  stdin=subprocess.DEVNULL, timeout=timeout,
                                  env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        except subprocess.TimeoutExpired:
            self.fail(f"the command did not finish within {timeout} s")

    def latest(self) -> str:
        path = self.results / "count-latest.md"
        self.assertTrue(path.is_file(), "the command wrote no result")
        return path.read_bytes().decode("utf-8")

    def rows(self, heading: str) -> list[list[str]]:
        """The rows of the table under `## <heading>` of the latest result, as cells."""
        text = self.latest()
        self.assertIn(f"\n## {heading}\n", text, f"the result has no section `## {heading}`")
        section = text.split(f"\n## {heading}\n", 1)[1].split("\n## ", 1)[0]
        lines = [line for line in section.splitlines() if line.startswith("|")]
        return [split_row(line) for line in lines[2:]]

    def cycles(self) -> list[dict]:
        text = self.latest()
        section = text.split("\n## Cycles\n", 1)[1].split("\n## ", 1)[0]
        lines = [line for line in section.splitlines() if line.startswith("|")]
        header = [cell.strip() for cell in lines[0].strip("|").split("|")]
        return [dict(zip(header, row)) for row in self.rows("Cycles")]


class CycleFound(AuditCountCase):
    def test_a_record_added_and_then_removed_gives_its_cycle_pin_and_remarks(self):
        product = self.repository()
        remarks = ("- Process remarks on the-way:\n"
                   "  - author, docs/task-cycles/a-task/reports/author.md: the plan named a moved\n"
                   "    file\n"
                   "  - reviewer, docs/task-cycles/a-task/reports/review.md: the check was unclear\n"
                   "    - a sub-item that belongs to the entry above\n"
                   "  - the orchestrator: a remark of its own\n")
        added, _ = product.cycle("a-task", {"cycle.md": record(remarks=remarks)})
        self.write_locations(self.places(product=product))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        cycles = self.cycles()
        self.assertEqual(1, len(cycles), cycles)
        cycle = cycles[0]
        self.assertEqual("product", cycle["Repository"])
        self.assertEqual(added, cycle["Record"])
        self.assertEqual("a-task", cycle["Folder"])
        self.assertEqual(PIN, cycle["Process pin"])
        self.assertEqual("3", cycle["Remarks"])

    def test_a_record_reached_only_through_a_merge_is_found(self):
        # The merge's tree equals its first parent's, so a history simplified to one parent
        # would never reach the branch that added and removed the record.
        product = self.repository()
        start = product.commit({"README.md": "a product\n"}, "Start")
        main = product.commit({"README.md": "a product, changed\n"}, "Change", start)
        added, removed = product.cycle("merged-task", {"cycle.md": record()}, parent=start,
                                       branch=None)
        merge = product.commit({"README.md": "a product, changed\n"}, "Merge", main, removed)
        product.branch("main", merge)
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual([added], [cycle["Record"] for cycle in self.cycles()])

    def test_a_record_on_another_branch_is_found(self):
        product = self.repository()
        start = product.commit({"README.md": "a product\n"}, "Start")
        product.branch("main", start)
        added, _ = product.cycle("open-task", {"cycle.md": record()}, parent=start,
                                 branch="task/open")
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual([added], [cycle["Record"] for cycle in self.cycles()])

    def test_a_cycle_committed_again_after_a_correction_counts_once(self):
        product = self.repository()
        first, removed = product.cycle("fixed-task", {"cycle.md": record()})
        corrected = record(remarks="- Process remarks on the-way:\n  - author: one\n"
                                   "  - reviewer: two\n")
        again, _ = product.cycle("fixed-task", {"cycle.md": corrected}, parent=removed)
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        cycles = self.cycles()
        self.assertEqual(1, len(cycles), cycles)
        self.assertEqual(first, cycles[0]["Record"])
        self.assertEqual(again, cycles[0]["Later copies"])
        self.assertEqual("2", cycles[0]["Remarks"])

    def test_a_cycle_md_outside_a_record_folder_is_no_cycle(self):
        product = self.repository()
        product.cycle("deeper/inside", {"cycle.md": record()})
        start = product.commit({"README.md": "a product\n",
                                "docs/task-cycles/cycle.md": record(),
                                "docs/other/some-task/cycle.md": record()}, "Stray records")
        product.branch("stray", start)
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual([], self.cycles())
        self.assertEqual([["product", "0", "yes"]], self.rows("Repositories"))


class ProcessPin(AuditCountCase):
    def pin_of(self, pin_line: str, key: str = "product") -> tuple[str, list[list[str]]]:
        repository = self.repository(key)
        repository.cycle("a-task", {"cycle.md": record(pin_line=pin_line)})
        self.write_locations(self.places(**{key: repository}))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        return self.cycles()[0]["Process pin"], self.rows("Unknown values")

    def test_a_moved_pin_gives_the_commit_it_moved_to(self):
        pin, _ = self.pin_of("- Process pin: `1111111` at start; moved to `2222222abc` by the "
                             "task branch's first\n  commit `3333333`")
        self.assertEqual("2222222abc", pin)

    def test_a_cycle_of_the_way_itself_takes_the_commit_of_its_target_base(self):
        pin, _ = self.pin_of("- Process pin: not applicable (the-way itself)", key="the-way")
        self.assertEqual(BASE, pin)

    def test_a_product_pin_naming_no_commit_is_unknown(self):
        pin, unknown = self.pin_of("- Process pin: none — defaced")
        self.assertEqual("unknown", pin)
        self.assertEqual("Process pin", unknown[0][2])

    def test_a_doubled_pin_is_unknown(self):
        pin, unknown = self.pin_of(f"- Process pin: `{PIN}`\n- Process pin: `{BASE}`")
        self.assertEqual("unknown", pin)
        self.assertIn("more than once", unknown[0][3])

    def test_a_missing_pin_is_unknown(self):
        pin, unknown = self.pin_of("- Pin of the process: `1234567`")
        self.assertEqual("unknown", pin)
        self.assertIn("no line `Process pin`", unknown[0][3])

    def test_an_earlier_record_joining_the_pin_with_its_base_gives_the_commit(self):
        pin, _ = self.pin_of("- Process pin and target base: `main` at `1234567`")
        self.assertEqual("1234567", pin)

    def test_a_pin_in_a_later_section_is_not_the_header_line(self):
        pin, _ = self.pin_of("- Status: complete")
        self.assertEqual("unknown", pin)


class Remarks(AuditCountCase):
    def remarks_of(self, remarks: str, extra: str = "") -> tuple[str, list[list[str]]]:
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record(remarks=remarks, extra=extra)})
        self.write_locations(self.places(product=product))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        return self.cycles()[0]["Remarks"], self.rows("Unknown values")

    def test_none_gives_zero(self):
        self.assertEqual("0", self.remarks_of("- Process remarks on the-way: `none`.")[0])

    def test_remarks_written_on_the_line_are_unknown(self):
        count, unknown = self.remarks_of("- Process remarks on the-way: (1) a remark; (2) another")
        self.assertEqual("unknown", count)
        self.assertEqual("Remarks", unknown[0][2])

    def test_an_earlier_label_is_unknown_not_zero(self):
        count, unknown = self.remarks_of("- Process remarks: none")
        self.assertEqual("unknown", count)
        self.assertIn("earlier form", unknown[0][3])

    def test_a_doubled_item_is_unknown(self):
        count, _ = self.remarks_of("- Process remarks on the-way:\n  - one\n"
                                   "- Process remarks on the-way:\n  - two\n")
        self.assertEqual("unknown", count)

    def test_an_item_inside_fenced_code_is_not_read(self):
        fenced = "```\n- Process remarks on the-way:\n  - a quoted one\n```\n"
        self.assertEqual("1", self.remarks_of("- Process remarks on the-way:\n  - one\n",
                                              extra=fenced)[0])

    def test_items_after_the_remarks_item_are_not_its_entries(self):
        self.assertEqual("0", self.remarks_of("- Process remarks on the-way: none\n"
                                              "- Another item:\n  - its own entry\n")[0])


class Times(AuditCountCase):
    def times_of(self, stages) -> tuple[dict, list[list[str]]]:
        product = self.repository()
        files = {"cycle.md": record()}
        if stages is not None:
            files["stages.md"] = stages
        product.cycle("a-task", files)
        self.write_locations(self.places(product=product))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        return self.cycles()[0], self.rows("Unknown values")

    WORKING = "Working time without waiting for tools"

    def time_rows(self, unknown: list[list[str]]) -> list[list[str]]:
        """The rows of *Unknown values* about the two times; the cost rows are checked apart."""
        return [row for row in unknown if row[2] in (self.WORKING, "Waiting for tools")]

    def test_the_times_of_stages_md(self):
        cycle, unknown = self.times_of(
            "# Stages\n\n- Working time, orchestrator turns and subagent turns joined: 1:00:05\n"
            "- Waiting for tools: 0:10:05\n- Working time without waiting for tools: 0:50:00\n")
        self.assertEqual("0:50:00", cycle[self.WORKING])
        self.assertEqual("0:10:05", cycle["Waiting for tools"])
        self.assertEqual([], self.time_rows(unknown))

    def test_an_earlier_form_without_the_wait_is_unknown_not_zero(self):
        cycle, unknown = self.times_of(
            "# Stages\n\n- Working time, orchestrator turns and subagent turns joined: 0:30:28\n")
        self.assertEqual("unknown", cycle[self.WORKING])
        self.assertEqual("unknown", cycle["Waiting for tools"])
        self.assertEqual(2, len(self.time_rows(unknown)))

    def test_a_wait_stages_md_gives_as_unknown_is_unknown(self):
        cycle, unknown = self.times_of(
            "- Waiting for tools: unknown — at least 0:01:00; 2 call(s) with no readable result\n"
            "- Working time without waiting for tools: unknown — at most 0:20:00\n")
        self.assertEqual("unknown", cycle[self.WORKING])
        self.assertEqual("unknown", cycle["Waiting for tools"])
        self.assertEqual(["gives the working time without waiting for tools as unknown",
                          "gives the waiting for tools as unknown"],
                         [row[3].split("` ", 1)[1] for row in self.time_rows(unknown)])

    def test_a_doubled_or_malformed_line_is_unknown(self):
        cycle, unknown = self.times_of("- Waiting for tools: 0:01:00\n- Waiting for tools: 0:02:00\n"
                                       "- Working time without waiting for tools: 1h 5m\n")
        self.assertEqual("unknown", cycle[self.WORKING])
        self.assertEqual("unknown", cycle["Waiting for tools"])
        self.assertEqual(["Working time without waiting for tools", "Waiting for tools"],
                         [row[2] for row in self.time_rows(unknown)])

    def test_a_line_inside_a_malformed_table_or_fenced_code_is_not_read(self):
        cycle, _ = self.times_of("| # | Stage |\n|---|\n| - Waiting for tools: 0:01:00 |\n"
                                 "```\n- Working time without waiting for tools: 0:05:00\n```\n")
        self.assertEqual("unknown", cycle[self.WORKING])
        self.assertEqual("unknown", cycle["Waiting for tools"])

    def test_a_missing_stages_md_is_unknown(self):
        cycle, unknown = self.times_of(None)
        self.assertEqual("unknown", cycle["Waiting for tools"])
        self.assertIn("no `stages.md`", unknown[0][3])


class CraftedInput(AuditCountCase):
    def test_control_characters_and_bars_stay_inside_one_cell_of_one_line(self):
        product = self.repository()
        product.cycle("evil\x1b[31m|x\nname", {"cycle.md": record(
            pin_line="- Process pin: \x1b[2J`zzz` \x07 none",
            remarks="- Process remarks on the-way:\n  - \x1b]0;title\x07 a remark\n")})
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        text = self.latest()
        self.assertEqual([], [char for char in text if not char.isprintable() and char != "\n"])
        cycles = self.cycles()
        self.assertEqual(1, len(cycles))
        self.assertEqual(9, len(self.rows("Cycles")[0]))
        self.assertIn("\\x1b", cycles[0]["Folder"])
        self.assertEqual("unknown", cycles[0]["Process pin"])
        self.assertEqual("1", cycles[0]["Remarks"])

    def test_a_symbolic_link_leaving_the_record_is_not_followed(self):
        outside = self.home / "outside.md"
        outside.write_text("- Waiting for tools: 0:01:00\n", encoding="utf-8")
        product = self.repository()
        product.cycle("linked-task", {"cycle.md": record(), "stages.md": (
            "120000", b"../../../../outside.md")})
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual("unknown", self.cycles()[0]["Waiting for tools"])
        self.assertIn("no regular file", self.rows("Unknown values")[0][3])

    def test_a_record_not_in_utf8_gives_unknown_values(self):
        product = self.repository()
        product.cycle("utf16-task", {"cycle.md": record().encode("utf-16"),
                                     "stages.md": b"- Waiting for tools: \xff0:01:00\n"})
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        cycle = self.cycles()[0]
        self.assertEqual(["unknown"] * 3, [cycle["Process pin"], cycle["Remarks"],
                                           cycle["Waiting for tools"]])
        self.assertIn("not UTF-8", self.rows("Unknown values")[0][3])

    def test_a_file_too_large_is_not_read(self):
        product = self.repository()
        product.cycle("large-task", {"cycle.md": record(),
                                     "stages.md": "- Waiting for tools: 0:01:00\n" + "x" * 4_200_000})
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual("unknown", self.cycles()[0]["Waiting for tools"])
        self.assertIn("larger than", self.rows("Unknown values")[0][3])

    def test_a_header_line_of_blanks_does_not_stall_the_count(self):
        # A header line `-`, a long run of blanks and no colon: a pattern that can split the run
        # between the marker's blanks and the label tries every split before it fails.
        product = self.repository()
        product.cycle("blank-task", {"cycle.md": record(
            pin_line="- " + " " * 150_000 + "x\n" + f"- Process pin: `{PIN}`")})
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count(timeout=60).returncode)
        self.assertEqual(PIN, self.cycles()[0]["Process pin"])

    def test_a_long_continuation_of_a_header_line_does_not_stall_the_count(self):
        product = self.repository()
        product.cycle("long-task", {"cycle.md": record(
            pin_line="- Process pin: none" + "\n x" * 800_000)})
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count(timeout=60).returncode)
        self.assertEqual("unknown", self.cycles()[0]["Process pin"])

    def test_a_backslash_before_a_bar_stays_inside_its_cell(self):
        product = self.repository()
        product.cycle("x\\|none\\|7777777\\|99\\|0:00:01\\|0:00:02", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        section = self.latest().split("\n## Cycles\n", 1)[1].split("\n## ", 1)[0]
        [row] = [line for line in section.splitlines() if line.startswith("| product ")]
        # Nine cells whether a reader honours backslash escapes or splits at every bar.
        self.assertEqual(9, len(split_row(row)), row)
        self.assertEqual(10, row.count("|"), row)
        cycle = self.cycles()[0]
        self.assertEqual(PIN, cycle["Process pin"])
        self.assertEqual("0", cycle["Remarks"])

    def test_a_commit_dated_beyond_the_readable_years_leaves_its_date_unknown(self):
        product = self.repository()
        start = product.commit({"README.md": "a product\n"}, "Start")
        added = product.commit_dated({"README.md": "a product\n",
                                      "docs/task-cycles/far-task/cycle.md": record()},
                                     start, "99999999999999")
        removed = product.commit({"README.md": "a product\n"}, "Remove the record", added)
        product.branch("main", removed)
        other = self.repository("other")
        other.cycle("plain-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product, other=other))
        done = self.run_count()
        self.assertEqual(0, done.returncode, done.stderr)
        cycles = {cycle["Repository"]: cycle for cycle in self.cycles()}
        self.assertEqual(added, cycles["product"]["Record"])
        self.assertEqual("unknown", cycles["product"]["Committed"])
        self.assertEqual(PIN, cycles["product"]["Process pin"])
        self.assertIn("other", cycles)
        self.assertIn(["product", added, "Committed"],
                      [row[:3] for row in self.rows("Unknown values")])


class Locations(AuditCountCase):
    def assert_refused(self, done, *words):
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        error = done.stderr.decode("utf-8")
        self.assertTrue(error.startswith("Error: "), error)
        self.assertEqual(1, len(error.strip().splitlines()), error)
        for word in words:
            self.assertIn(word, error)
        self.assertEqual([], list(self.results.iterdir()))

    def product(self) -> Repository:
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        return product

    def test_a_missing_file(self):
        self.assert_refused(self.run_count(), "does not exist")

    def test_a_file_that_is_not_json_or_no_object(self):
        self.write_locations("{\"the-way\": ")
        self.assert_refused(self.run_count(), "is not JSON")
        self.write_locations("[1, 2]")
        self.assert_refused(self.run_count(), "is not a JSON object")

    def test_a_missing_key_or_entry(self):
        product = self.product()
        self.write_locations({"product": {"repository": str(product.root)}})
        self.assert_refused(self.run_count(), "no key `the-way`")
        for entry in ("problem_register", "audit_results"):
            data = self.places(product=product)
            del data["the-way"][entry]
            self.write_locations(data)
            self.assert_refused(self.run_count(), f"no entry `{entry}` under `the-way`")

    def test_a_path_that_does_not_exist(self):
        product = self.product()
        for entry in ("problem_register", "audit_results"):
            data = self.places(product=product)
            data["the-way"][entry] = str(self.home / "missing")
            self.write_locations(data)
            self.assert_refused(self.run_count(), f"`{entry}` under `the-way`", "no existing")
        data = self.places(product=product)
        data["product"]["repository"] = str(self.home / "missing")
        self.write_locations(data)
        self.assert_refused(self.run_count(), "`repository` under `product`")

    def test_an_entry_of_a_wrong_type(self):
        product = self.product()
        data = self.places(product=product)
        data["product"]["repository"] = 42
        self.write_locations(data)
        self.assert_refused(self.run_count(), "`repository` under `product`", "not a path")
        data = self.places(product=product)
        data["the-way"] = str(self.results)
        self.write_locations(data)
        self.assert_refused(self.run_count(), "`the-way`", "not a JSON object")
        data = self.places(product=product)
        data["notes"] = ["tasks"]
        self.write_locations(data)
        self.assert_refused(self.run_count(), "`notes`", "not a JSON object")

    def test_a_relative_path(self):
        data = self.places(product=self.product())
        data["product"]["repository"] = "repos/product"
        self.write_locations(data)
        self.assert_refused(self.run_count(), "not an absolute path")

    def test_a_key_written_twice(self):
        product = self.product()
        text = json.dumps(self.places(product=product))
        self.write_locations(text[:-1] + ", \"product\": {}}")
        self.assert_refused(self.run_count(), "`product` twice")

    def test_a_named_repository_the_file_lacks(self):
        self.write_locations(self.places(product=self.product()))
        self.assert_refused(self.run_count("--repository", "other"), "no key `other`")
        data = self.places(product=self.product())
        data["notes"] = {"tasks": str(self.home)}
        self.write_locations(data)
        self.assert_refused(self.run_count("--repository", "notes"),
                            "no entry `repository` under `notes`")

    def test_no_repository_to_read(self):
        self.write_locations(self.places())
        self.assert_refused(self.run_count(), "--repository")

    def test_a_result_directory_inside_a_repository_to_read(self):
        product = self.product()
        data = self.places(product=product)
        inner = product.root / "results"
        inner.mkdir()
        data["the-way"]["audit_results"] = str(inner)
        self.write_locations(data)
        done = self.run_count()
        self.assertEqual(2, done.returncode)
        self.assertIn("inside the repository `product`", done.stderr.decode("utf-8"))
        self.assertEqual([], list(inner.iterdir()))


FULL_EVENTS = ("| Time | Stage | Actor and model | Handoff, skill and inputs "
               "| Output or full report | Short result and next step |\n"
               "|---|---|---|---|---|---|\n")
# Events as the archived records write a fix round: no path holds the word `report`.
ARCHIVED_EVENTS = ("| 10:00 | fix dispatch | orchestrator | findings | - | dispatched |\n"
                   "| 10:20 | fix returned | author | - | reports/fix.md | done |\n"
                   "| 10:30 | review of the fix | reviewer | - | reports/review-fix.md | PASS |\n")
TEST_PRICES = """# Test prices

- List date: 2026-01-01

## Test provider

| Model id in stages.md | Page name | Input | Cached input | Output |
|---|---|---|---|---|
| model-a | Model A | 2 | 1 | 10 |
| model-b | Model B | 4 | 0.5 | 20 |
"""
STAGES_HEADER = ("# Stages of the cycle run\n\n- Working time without waiting for tools: 0:20:00\n"
                 "- Waiting for tools: 0:05:00\n\n"
                 "## Stages: start, waiting for tools and tokens by model\n\n"
                 "| # | Stage | Start | Waiting for tools | Model | Input | Cached input "
                 "| Output |\n|---|---|---|---|---|---|---|---|\n")


STAGES_HEADER_NAMED = STAGES_HEADER.replace(
    "| Output |\n|---|---|---|---|---|---|---|---|\n",
    "| Output | Files named |\n|---|---|---|---|---|---|---|---|---|\n")


def stage_row(number, name, model, input_, cached, output, files=None) -> str:
    """A row of the stages section; with `files`, the row of the form that names the files each
    turn was given."""
    named = "" if files is None else f" {files} |"
    return (f"| {number} | {name} | 2026-11-11 10:00:00 | 0:00:00 | {model} | {input_} | {cached} "
            f"| {output} |{named}\n")


WHOLE = "reports/review_whole_findings.md"
SLICE = "reports/review_slice2_findings.md"
ONE_ROUND = (f"- Review rounds:\n  - findings `{WHOLE}`: the whole change, range `a1b2c3d..e4f5a6b`,"
             "\n    report `reports/review_whole.md`; fix `reports/fix.md`, its review "
             "`reports/review-fix.md`\n")


def fix_record(rounds=ONE_ROUND, events="") -> str:
    """A cycle record whose item `Review rounds` reads `rounds`."""
    text = record(remarks="- Process remarks on the-way: none\n").replace(
        "| Time | Stage |\n|---|---|\n", FULL_EVENTS + events)
    return text.replace("- Status: request open\n", "- Status: request open\n" + rounds)


def one_fix_round(header=STAGES_HEADER_NAMED, fix_files=f"reports/fix_handoff.md, {WHOLE}",
                  review_files=f"{WHOLE}, reports/fix.md") -> str:
    """Stages of one round of the whole change: the review that found the findings, the fix,
    which ran on two models, and the review of the fix. With the earlier header, the rows have no
    cell of files."""
    named = header == STAGES_HEADER_NAMED

    def files(text):
        return text if named else None

    review = "Review whole change (general-purpose) — turn 1"
    author = "One author (general-purpose) — turn 2"
    reviewer = "Review whole change (general-purpose) — turn 2"
    return (header
            + stage_row(1, "orchestrator", "model-a", 1000, 0, 100, files(""))
            + stage_row(2, review, "model-a", 2000, 1000, 200, files("reports/review_handoff.md"))
            + stage_row(3, author, "model-b", 400, 100, 40, files(fix_files))
            + stage_row(3, author, "model-a", 100, 0, 10, files(fix_files))
            + stage_row(4, reviewer, "model-a", 300, 0, 30, files(review_files)))


class Cost(AuditCountCase):
    def count(self, stages, record_text=None, prices=TEST_PRICES):
        product = self.repository()
        files = {"cycle.md": record_text if record_text is not None else fix_record()}
        if stages is not None:
            files["stages.md"] = stages
        product.cycle("a-task", files)
        self.write_locations(self.places(product=product))
        test_prices = self.home / "prices.md"
        test_prices.write_text(prices, encoding="utf-8")
        return self.run_count("--prices", str(test_prices))

    def cost_row(self) -> list[str]:
        [row] = self.rows("Cost")
        return row

    def unknown_why(self, value: str) -> list[str]:
        return [row[3] for row in self.rows("Unknown values") if row[2] == value]

    def share_of(self, stages, record_text=None) -> tuple[list[str], list[str]]:
        """The cost row and the reasons the share is unknown."""
        done = self.count(stages, record_text)
        self.assertEqual(0, done.returncode, done.stderr)
        return self.cost_row(), self.unknown_why("Fix rounds share")

    def test_a_round_named_by_its_findings_file_gives_the_share_of_the_turns_that_name_it(self):
        # Worked by hand, in millionths of a dollar: stage 1 is 1000*2 + 100*10 = 3000; stage 2 is
        # 1000*2 + 1000*1 + 200*10 = 5000; stage 3 is 300*4 + 100*0.5 + 40*20 = 2050 on model-b
        # and 100*2 + 10*10 = 300 on model-a; stage 4 is 300*2 + 30*10 = 900. The total is 11250.
        # Stages 3 and 4 name the findings file: 3250 of 11250 is 28.89 %.
        row, why = self.share_of(one_fix_round())
        self.assertEqual(["product", "2026-01-01", "0.011250", "1", "28.9%"],
                         [row[0], row[2], row[3], row[4], row[5]])
        self.assertEqual([], why)

    def test_the_stage_report_cycle_stages_writes_gives_the_share(self):
        # Transcripts in Claude Code's form, where the fix and the review of the fix are each a
        # resumed subagent whose message names the findings file. Worked by hand at model-a's
        # prices: the orchestrator 1000*2 + 100*10 = 3000; the author's first turn 3000 and its
        # fix 500*2 + 50*10 = 1500; the reviewer's first turn 2000*2 + 200*10 = 6000 and its review
        # of the fix 250*2 + 25*10 = 750. 2250 of 14250 is 15.79 %.
        def line(kind, clock, **fields):
            entry = {"type": kind, "timestamp": f"2026-11-11T{clock}.000Z"}
            entry.update(fields)
            return json.dumps(entry) + "\n"

        def told(clock, text, meta=False):
            fields = {"message": {"role": "user", "content": text}}
            if meta:
                fields["isMeta"] = True
            return line("user", clock, **fields)

        def answered(clock, ident, input_, output):
            return line("assistant", clock, message={
                "id": ident, "model": "model-a", "stop_reason": "end_turn",
                "content": [{"type": "text"}],
                "usage": {"input_tokens": input_, "cache_creation_input_tokens": 0,
                          "cache_read_input_tokens": 0, "output_tokens": output}})

        project = self.home / "claude" / "projects" / "p"
        agents = project / "sess" / "subagents"
        agents.mkdir(parents=True)
        (project / "sess.jsonl").write_text(
            told("09:00:00", "run the cycle") + answered("09:00:10", "o1", 1000, 100), "utf-8")
        (agents / "agent-f.jsonl").write_text(
            told("09:01:00", "Implement; handoff .runs/task-cycles/t/reports/author_handoff.md")
            + answered("09:02:00", "f1", 1000, 100)
            + told("09:20:00", f"Fix the findings in {WHOLE} by reports/fix_handoff.md", True)
            + answered("09:21:00", "f2", 500, 50), "utf-8")
        (agents / "agent-r.jsonl").write_text(
            told("09:10:00", "Review the change; handoff reports/review_handoff.md")
            + answered("09:11:00", "r1", 2000, 200)
            + told("09:30:00", f"Review the fix of the findings in {WHOLE}", True)
            + answered("09:31:00", "r2", 250, 25), "utf-8")
        for name, description in (("f", "Author"), ("r", "Reviewer")):
            (agents / f"agent-{name}.meta.json").write_text(json.dumps(
                {"agentType": "general-purpose", "description": description}), "utf-8")
        output = self.home / "stages.md"
        written = subprocess.run(
            [sys.executable, "-B", str(HERE.parent / "task-cycle" / "cycle_stages.py"), "sess",
             "--claude-home", str(self.home / "claude"), "--codex-home", str(self.home / "codex"),
             "--output", str(output)], capture_output=True, stdin=subprocess.DEVNULL)
        self.assertEqual(0, written.returncode, written.stderr)
        row, why = self.share_of(output.read_text(encoding="utf-8"))
        self.assertEqual(["0.014250", "1", "15.8%"], row[3:6])
        self.assertEqual([], why)

    def test_the_same_record_with_an_earlier_form_of_stages_md_leaves_the_share_unknown(self):
        row, why = self.share_of(one_fix_round(header=STAGES_HEADER))
        self.assertEqual(["0.011250", "1", "unknown"], row[3:6])
        self.assertTrue(any("no column `Files named`" in reason for reason in why), why)

    def test_review_rounds_reading_none_gives_a_share_of_zero(self):
        stages = one_fix_round(fix_files="reports/author_handoff.md",
                               review_files="reports/review_handoff.md")
        row, why = self.share_of(stages, fix_record(rounds="- Review rounds: none\n"))
        self.assertEqual(["0.011250", "0", "0.0%"], row[3:6])
        self.assertEqual([], why)

    def test_a_turn_naming_the_findings_files_of_two_rounds_counts_once(self):
        # Every stage costs 1000*2 + 100*10 = 3000: 15000 in all. The fix names both findings
        # files, each review one of them: 9000 of 15000 is 60 %; counting the fix once per file
        # would give 80 %.
        stages = (STAGES_HEADER_NAMED
                  + stage_row(1, "orchestrator", "model-a", 1000, 0, 100, "")
                  + stage_row(2, "Fix (general-purpose)", "model-a", 1000, 0, 100,
                              f"{WHOLE}, {SLICE}")
                  + stage_row(3, "Review A (general-purpose)", "model-a", 1000, 0, 100, WHOLE)
                  + stage_row(4, "Review B (general-purpose)", "model-a", 1000, 0, 100, SLICE)
                  + stage_row(5, "Other (general-purpose)", "model-a", 1000, 0, 100,
                              "reports/other_handoff.md"))
        rounds = f"- Review rounds:\n  - findings `{WHOLE}`: one\n  - findings `{SLICE}`: two\n"
        row, why = self.share_of(stages, fix_record(rounds=rounds))
        self.assertEqual(["0.015000", "2", "60.0%"], row[3:6])

    def test_rounds_written_in_prose_leave_the_share_unknown_not_zero(self):
        # The archived form: the fix is named, but by no findings file.
        record_text = fix_record(events=ARCHIVED_EVENTS,
                                 rounds="- Review rounds: one whole-change round, one fix and its "
                                        "review. Closed at 4327974.\n")
        row, why = self.share_of(one_fix_round(), record_text)
        self.assertEqual(["unknown", "unknown"], row[4:6])
        self.assertTrue(any("names no findings file" in reason for reason in why), why)

    def test_a_findings_file_no_turn_names_leaves_the_share_unknown(self):
        stages = one_fix_round(fix_files="reports/fix_handoff.md",
                               review_files="reports/review_fix_handoff.md")
        row, why = self.share_of(stages)
        self.assertEqual(["1", "unknown"], row[4:6])
        self.assertTrue(any("named by 0 subagent turn(s)" in reason for reason in why), why)

    def test_a_findings_file_only_one_turn_names_leaves_the_share_unknown(self):
        # The fix was given its findings file only inside its handoff: the share would leave out
        # the fix itself.
        row, why = self.share_of(one_fix_round(fix_files="reports/fix_handoff.md"))
        self.assertEqual(["1", "unknown"], row[4:6])
        self.assertTrue(any("named by 1 subagent turn(s)" in reason for reason in why), why)

    def test_none_beside_a_turn_naming_a_findings_file_leaves_the_share_unknown(self):
        row, why = self.share_of(one_fix_round(), fix_record(rounds="- Review rounds: none\n"))
        self.assertEqual(["0", "unknown"], row[4:6])
        self.assertTrue(any("do not agree" in reason for reason in why), why)

    def test_a_findings_file_the_record_does_not_name_leaves_the_share_unknown(self):
        stages = one_fix_round(review_files=f"{WHOLE}, {SLICE}")
        row, why = self.share_of(stages)
        self.assertEqual(["1", "unknown"], row[4:6])
        self.assertTrue(any("do not agree" in reason for reason in why), why)

    def test_a_doubled_review_rounds_line_leaves_the_share_unknown(self):
        rounds = ONE_ROUND + f"- Review rounds:\n  - findings `{SLICE}`: another\n"
        row, why = self.share_of(one_fix_round(), fix_record(rounds=rounds))
        self.assertEqual(["unknown", "unknown"], row[4:6])
        self.assertTrue(any("more than once" in reason for reason in why), why)

    def test_an_entry_of_review_rounds_without_its_findings_file_leaves_the_share_unknown(self):
        rounds = ONE_ROUND + "  - the return step: fix `reports/return_fix.md`\n"
        row, why = self.share_of(one_fix_round(), fix_record(rounds=rounds))
        self.assertEqual(["unknown", "unknown"], row[4:6])
        self.assertTrue(any("names no findings file" in reason for reason in why), why)

    def test_review_rounds_that_contradict_themselves_leave_the_share_unknown(self):
        cases = {
            "none beside entries": ("- Review rounds: none\n"
                                    + ONE_ROUND.split("\n", 1)[1], "beside its entries"),
            "a findings file twice": (ONE_ROUND + f"  - findings `{WHOLE}`: again\n", "twice"),
        }
        for label, (rounds, words) in cases.items():
            with self.subTest(label):
                row, why = self.share_of(one_fix_round(), fix_record(rounds=rounds))
                self.assertEqual(["unknown", "unknown"], row[4:6])
                self.assertTrue(any(words in reason for reason in why), why)

    def test_a_record_without_a_review_rounds_line_leaves_the_share_unknown(self):
        row, why = self.share_of(one_fix_round(), fix_record(rounds=""))
        self.assertEqual(["unknown", "unknown"], row[4:6])
        self.assertTrue(any("no item `Review rounds`" in reason for reason in why), why)

    def test_crafted_cells_of_files_leave_the_share_unknown_and_one_row_per_cycle(self):
        for files in (f"{WHOLE}, reports/../secret.md", f"{WHOLE}, reports/a..b.md",
                      f"{WHOLE}, reports/x.md\x1b[2J",
                      "reports/" + "a" * 200_000 + ".md", f"{WHOLE},, reports/.hidden.md"):
            with self.subTest(files=files[:40]):
                row, why = self.share_of(one_fix_round(fix_files=files))
                self.assertEqual(["0.011250", "1", "unknown"], row[3:6])
                self.assertTrue(any("not a list of files of `reports/`" in reason
                                    for reason in why), why)
                self.assertEqual(1, len(self.rows("Cost")))

    def test_findings_files_in_review_rounds_are_read_only_in_their_form(self):
        for path in ("reports/../x_findings.md", "reports/" + "f" * 200_000 + ".md",
                     "reports/a|b.md"):
            with self.subTest(path=path[:40]):
                rounds = f"- Review rounds:\n  - findings `{path}`: crafted\n"
                row, why = self.share_of(one_fix_round(), fix_record(rounds=rounds))
                self.assertEqual(["unknown", "unknown"], row[4:6])

    def test_a_stage_with_no_token_usage_leaves_the_cost_unknown(self):
        # cycle_stages.py writes the model mark `—` with zero counts for a stage it found no usage
        # for; where no row of the section is priced, that is not a cost of zero.
        stages = STAGES_HEADER + stage_row(1, "orchestrator", "—", 0, 0, 0)
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("no token usage" in why for why in self.unknown_why("Cost")))

    def test_an_orchestrator_stretch_with_no_token_usage_costs_nothing(self):
        # A stretch of the orchestrator's own work with time and no response: the subagent
        # stages are priced, so the cycle's cost is known.
        stages = one_fix_round() + stage_row(5, "orchestrator", "—", 0, 0, 0, "")
        row, why = self.share_of(stages)
        self.assertEqual(["0.011250", "1", "28.9%"], row[3:6])
        self.assertEqual([], self.unknown_why("Cost"))

    def test_a_subagent_stage_with_no_token_usage_leaves_the_cost_unknown(self):
        stages = one_fix_round() + stage_row(5, "Idle (general-purpose)", "—", 0, 0, 0, "")
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("Idle" in why for why in self.unknown_why("Cost")))

    def test_a_model_the_list_lacks_leaves_the_cost_and_the_share_unknown(self):
        stages = one_fix_round().replace("| model-b |", "| model-c |")
        self.assertEqual(0, self.count(stages).returncode)
        row = self.cost_row()
        self.assertEqual(["unknown", "unknown"], [row[3], row[5]])
        reasons = self.unknown_why("Cost")
        self.assertTrue(any("no price for model `model-c`" in why for why in reasons), reasons)

    def test_stages_md_without_the_per_model_section_leaves_the_cost_unknown(self):
        stages = ("# Stages of the cycle run\n\n- Working time, orchestrator turns and subagent "
                  "turns joined: 1:00:00\n")
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("earlier form" in why for why in self.unknown_why("Cost")))

    def test_cached_input_above_input_leaves_the_cost_unknown(self):
        stages = one_fix_round().replace("| 2000 | 1000 | 200 |", "| 2000 | 5000 | 200 |")
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("above its input" in why for why in self.unknown_why("Cost")))

    def test_a_token_count_of_sixteen_digits_leaves_the_cost_unknown(self):
        stages = one_fix_round().replace("| 400 |", "| " + "9" * 16 + " |")
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("token count" in why for why in self.unknown_why("Cost")))

    def test_a_cost_at_the_command_limit_is_unknown_not_written_with_overrun_digits(self):
        # 1,200 rows of 999,999,999,999,999 input tokens at 999,999.999999 dollars per million come
        # to about 1.2 * 10^18 dollars, above the limit of 10^18.
        row = stage_row(1, "Stage of a large count", "model-b", 999999999999999, 0, 0)
        stages = STAGES_HEADER + row * 1200
        prices = TEST_PRICES.replace("| model-b | Model B | 4 | 0.5 | 20 |",
                                     "| model-b | Model B | 999999.999999 | 0.5 | 20 |")
        self.assertEqual(0, self.count(stages, prices=prices).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("limit" in why for why in self.unknown_why("Cost")))

    def test_a_price_list_naming_a_model_twice_refuses_the_run(self):
        doubled = TEST_PRICES + "| model-a | Model A again | 2 | 1 | 10 |\n"
        done = self.count(one_fix_round(), prices=doubled)
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("twice", done.stderr.decode("utf-8"))
        self.assertEqual([], list(self.results.iterdir()))


class RegisterCount(AuditCountCase):
    """The register of problems counted against the cycles (WAY-329, WAY-332 to WAY-335)."""

    def use_register(self, **rows) -> None:
        self.register.write_text(register_text(**rows), encoding="utf-8")

    def the_way_with_a_fix(self):
        """A checkout of the-way: the fix commit, a commit that holds it, and one that does not."""
        way = self.repository("the-way")
        start = way.commit({"README.md": "the-way\n"}, "Start")
        fix = way.commit({"README.md": "the-way, fixed\n"}, "Fix the process", start)
        with_fix = way.commit({"README.md": "the-way, later\n"}, "Later change", fix)
        without = way.commit({"README.md": "the-way, other\n"}, "Other change", start)
        way.branch("main", with_fix)
        return way, fix, with_fix, without

    def test_a_fixed_issue_counts_apart_the_cycles_whose_pin_holds_the_fix(self):
        way, fix, with_fix, without = self.the_way_with_a_fix()
        product = self.repository()
        holding, removed = product.cycle(
            "holds-task", {"cycle.md": record(pin_line=f"- Process pin: `{with_fix}`")})
        lacking, _ = product.cycle(
            "lacks-task", {"cycle.md": record(pin_line=f"- Process pin: `{without}`")},
            parent=removed)
        self.use_register(issues=[issue_row("fixed-one", "fixed", fix)],
                          problems=[problem_row("product", holding, "fixed-one"),
                                    problem_row("product", lacking, "fixed-one")])
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["fixed-one", fix, "1", "1", "0", "0"]], self.rows("Fixed issues"))

    def test_the_template_with_no_rows_counts_nothing_and_refuses_nothing(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["product", added, "none", "0", "0", "0", "0"]],
                         self.rows("Problems by cycle"))
        self.assertEqual([], self.rows("Fixed issues"))
        self.assertEqual([], [row for row in self.rows("Unknown values")
                              if row[2].startswith("row ")])

    def test_a_problem_whose_repository_is_not_read_stays_unknown(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(problems=[problem_row("ghost", added)])
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertIn(["ghost", added, "row 1 of `Problems`"],
                      [row[:3] for row in self.rows("Unknown values")])
        self.assertEqual([["product", added, "none", "0", "0", "0", "0"]],
                         self.rows("Problems by cycle"))

    def test_crafted_rows_of_the_register_are_refused_with_a_reason_and_the_rest_counted(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(
            classes=["| Not Lower | x | start | none |", "| dated-class | x | 2026-02-30 | none |",
                     "| evil\x1b[2J-class | x | start | none |",
                     "| " + "a" * 200_000 + " | x | start | none |"],
            issues=[issue_row("good-issue"), "| bad-fix | the matter | fixed | 1234567 |"],
            problems=[problem_row("product", added, "good-issue"),
                      problem_row("product", added, "good-issue", cls="no-such-class"),
                      problem_row("product", "nothex", "good-issue"),
                      problem_row("product", added, "good-issue", weight="Blocker"),
                      problem_row("product", added, "bad-fix"),
                      problem_row("product", added, "missing-issue"),
                      problem_row("r" * 200_000, added, "good-issue")])
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        text = self.latest()
        self.assertEqual([], [char for char in text if not char.isprintable() and char != "\n"])
        unknown = self.rows("Unknown values")
        self.assertEqual([f"row {number} of `Classes`" for number in range(1, 5)],
                         [row[2] for row in unknown if row[2].endswith("`Classes`")])
        self.assertIn("row 2 of `Issues`", [row[2] for row in unknown])
        self.assertEqual([f"row {number} of `Problems`" for number in range(2, 8)],
                         [row[2] for row in unknown if row[2].endswith("`Problems`")])
        self.assertTrue(all(len(cell) < 1000 for row in unknown for cell in row), unknown)
        self.assertEqual([[ "product", added, "process-remark", "0", "1", "0", "0"]],
                         self.rows("Problems by cycle"))
        self.assertEqual(["good-issue"], [row[0] for row in self.rows("Open issues")])

    def test_a_class_named_in_two_rows_refuses_both_and_its_problems_with_it(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(classes=["| process-remark | again | start | none |"],
                          problems=[problem_row("product", added)])
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(["row 1 of `Classes`", "row 8 of `Classes`"],
                         [row[2] for row in self.rows("Unknown values")
                          if row[2].endswith("`Classes`")])
        self.assertEqual([["product", added, "none", "0", "0", "0", "0"]],
                         self.rows("Problems by cycle"))
        self.assertIn(["product", added, "row 1 of `Problems`",
                       "the class is not in the list of classes"],
                      [row[:4] for row in self.rows("Unknown values")])

    def test_a_long_run_of_blanks_in_a_class_name_does_not_stall_the_count(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.use_register(classes=["| a" + " " * 150_000 + "b | x | start | none |"])
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11", timeout=60)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["product", added, "none", "0", "0", "0", "0"]],
                         self.rows("Problems by cycle"))

    def test_a_table_missing_from_the_register_is_an_error_of_the_register(self):
        product = self.repository()
        added, _ = product.cycle("a-task", {"cycle.md": record()})
        self.assertEqual(1, TEMPLATE.count("## Issues\n"))
        self.register.write_text(TEMPLATE.replace("## Issues\n", "## Issue list\n"), encoding="utf-8")
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(1, done.returncode, done.stderr)
        error = done.stderr.decode("utf-8")
        self.assertIn("Error: the register of problems", error)
        self.assertIn("## Issues", error)
        self.assertIn(["the-way", "none", "table `Issues`"],
                      [row[:3] for row in self.rows("Unknown values")])
        self.assertEqual([["product", added, "none", "0", "0", "0", "0"]],
                         self.rows("Problems by cycle"))

    def test_a_register_larger_than_the_cap_stops_the_run_with_nothing_written(self):
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        self.register.write_text(TEMPLATE + "x" * 4_200_000, encoding="utf-8")
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(2, done.returncode)
        self.assertIn(b"Error: ", done.stderr)
        self.assertEqual([], list(self.results.iterdir()))

    def test_open_issues_wait_from_the_cycle_commit_to_the_day_of_the_run(self):
        product = self.repository()
        start = product.commit({"README.md": "a product\n"}, "Start")
        # 1760000000 is 2025-10-09 in UTC.
        added = product.commit_dated({"README.md": "a product\n",
                                      "docs/task-cycles/slow-task/cycle.md": record()},
                                     start, "1760000000")
        removed = product.commit({"README.md": "a product\n"}, "Remove the record", added)
        product.branch("main", removed)
        self.use_register(issues=[issue_row("slow-one")],
                          problems=[problem_row("product", added, "slow-one")])
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2025-10-19")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["slow-one", "1", "1", "0", "10"]], self.rows("Open issues"))
        done = self.run_count("--today", "2025-10-08")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual("unknown", self.rows("Open issues")[0][4])

    def test_open_issues_are_listed_in_the_register_order_not_by_their_returns(self):
        product = self.repository()
        first, removed = product.cycle("a-task", {"cycle.md": record()})
        second, removed = product.cycle("b-task", {"cycle.md": record()}, parent=removed)
        third, _ = product.cycle("c-task", {"cycle.md": record()}, parent=removed)
        self.use_register(issues=[issue_row("first-issue"), issue_row("second-issue")],
                          problems=[problem_row("product", first, "first-issue"),
                                    problem_row("product", second, "second-issue"),
                                    problem_row("product", third, "second-issue")])
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["first-issue", "1", "1", "0"], ["second-issue", "2", "2", "0"]],
                         [row[:4] for row in self.rows("Open issues")])

    def test_a_cycle_committed_again_counts_its_problem_once(self):
        product = self.repository()
        first, removed = product.cycle("fixed-task", {"cycle.md": record()})
        again, _ = product.cycle("fixed-task", {"cycle.md": record(
            remarks="- Process remarks on the-way:\n  - author: one\n")}, parent=removed)
        self.use_register(problems=[problem_row("product", again)])
        self.write_locations(self.places(product=product))
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["product", first, "process-remark", "0", "1", "0", "0"]],
                         self.rows("Problems by cycle"))

    def test_an_unknown_pin_or_a_pin_the_history_lacks_is_unknown_for_its_side(self):
        way, fix, with_fix, _ = self.the_way_with_a_fix()
        product = self.repository()
        no_pin, removed = product.cycle("no-pin-task",
                                        {"cycle.md": record(pin_line="- Process pin: none")})
        lacking, removed = product.cycle(
            "lacking-task", {"cycle.md": record(
                pin_line="- Process pin: `fedcba9876543210fedcba9876543210fedcba98`")},
            parent=removed)
        holding, _ = product.cycle("holding-task",
                                   {"cycle.md": record(pin_line=f"- Process pin: `{with_fix}`")},
                                   parent=removed)
        self.use_register(issues=[issue_row("fixed-one", "fixed", fix)],
                          problems=[problem_row("product", no_pin, "fixed-one"),
                                    problem_row("product", lacking, "fixed-one"),
                                    problem_row("product", holding, "fixed-one")])
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["fixed-one", fix, "1", "0", "2", "0"]], self.rows("Fixed issues"))
        reasons = [row[3] for row in self.rows("Unknown values")
                   if row[:3] == ["product", lacking, "Process pin"]]
        self.assertEqual(1, len(reasons), reasons)
        self.assertIn("lacks commit", reasons[0])

    def test_a_fix_the_history_lacks_leaves_its_issue_unknown(self):
        way, _, with_fix, _ = self.the_way_with_a_fix()
        missing = "1234567890abcdef1234567890abcdef12345678"
        product = self.repository()
        holding, _ = product.cycle("holding-task",
                                   {"cycle.md": record(pin_line=f"- Process pin: `{with_fix}`")})
        self.use_register(issues=[issue_row("fixed-one", "fixed", missing)],
                          problems=[problem_row("product", holding, "fixed-one")])
        data = self.places(product=product)
        data["the-way"]["repository"] = str(way.root)
        self.write_locations(data)
        done = self.run_count("--today", "2026-11-11")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual([["fixed-one", missing, "unknown", "unknown", "0", "0"]],
                         self.rows("Fixed issues"))
        reasons = [row[3] for row in self.rows("Unknown values")
                   if row[2] == "the fix of issue `fixed-one`"]
        self.assertEqual(1, len(reasons), reasons)
        self.assertIn("lacks commit", reasons[0])


class Run(AuditCountCase):
    def test_it_reads_nothing_from_stdin(self):
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        # stdin stays open and empty: a command that read it would wait until the timeout.
        with subprocess.Popen([sys.executable, "-B", str(SCRIPT), "--locations",
                               str(self.locations)], stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            try:
                process.wait(timeout=60)
            except subprocess.TimeoutExpired:
                process.kill()
                self.fail("the command waited on stdin")
            self.assertEqual(0, process.returncode, process.stderr.read())

    def test_the_same_input_gives_the_same_bytes_in_both_files(self):
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        self.write_locations(self.places(product=product))
        self.assertEqual(0, self.run_count().returncode)
        first = (self.results / "count-latest.md").read_bytes()
        self.assertEqual(0, self.run_count().returncode)
        names = sorted(path.name for path in self.results.iterdir())
        self.assertEqual(2, len(names), names)
        self.assertRegex(names[0], r"^count-\d{4}-\d{2}-\d{2}\.md$")
        self.assertEqual(first, (self.results / names[0]).read_bytes())
        self.assertEqual(first, (self.results / "count-latest.md").read_bytes())
        self.assertNotIn(b"\r", first)
        self.assertNotIn(str(self.home).encode("utf-8"), first)

    def test_without_a_name_it_reads_every_key_with_a_repository(self):
        first, second = self.repository("first"), self.repository("second")
        first.cycle("one", {"cycle.md": record()})
        second.cycle("two", {"cycle.md": record()})
        data = self.places(first=first, second=second)
        data["notes"] = {"tasks": str(self.home)}
        self.write_locations(data)
        self.assertEqual(0, self.run_count().returncode)
        self.assertEqual([["first", "1", "yes"], ["second", "1", "yes"]],
                         self.rows("Repositories"))
        self.assertEqual(0, self.run_count("--repository", "second").returncode)
        self.assertEqual([["second", "1", "yes"]], self.rows("Repositories"))

    def test_a_repository_git_cannot_read_is_named_and_the_rest_written(self):
        product = self.repository()
        product.cycle("a-task", {"cycle.md": record()})
        plain = self.home / "plain"
        plain.mkdir()
        data = self.places(product=product)
        data["plain"] = {"repository": str(plain)}
        self.write_locations(data)
        done = self.run_count()
        self.assertEqual(1, done.returncode, done.stderr)
        self.assertIn("Error: repository `plain`", done.stderr.decode("utf-8"))
        rows = self.rows("Repositories")
        self.assertEqual(["plain", "0"], rows[0][:2])
        self.assertTrue(rows[0][2].startswith("no: "), rows[0])
        self.assertEqual(["product", "1", "yes"], rows[1])

    def test_the_way_without_a_repository_entry_is_this_checkout(self):
        self.write_locations(self.places())
        done = self.run_count("--repository", "the-way")
        self.assertEqual(0, done.returncode, done.stderr)
        [row] = self.rows("Repositories")
        self.assertEqual("the-way", row[0])
        self.assertTrue(row[2].startswith("yes"), row)


if __name__ == "__main__":
    unittest.main()
