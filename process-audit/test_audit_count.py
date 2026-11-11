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
        self.register.write_text("# Register of problems\n", encoding="utf-8")
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
FIX_EVENTS = ("| 10:00 | fix dispatch | orchestrator | findings | - | dispatched |\n"
              "| 10:20 | fix returned | author | - | reports/07-fix-1-report.md | done |\n"
              "| 10:30 | review of the fix | reviewer | - "
              "| reports/08-review-fix-1-report.md | PASS |\n")
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


def stage_row(number, name, model, input_, cached, output) -> str:
    return (f"| {number} | {name} | 2026-11-11 10:00:00 | 0:00:00 | {model} | {input_} | {cached} "
            f"| {output} |\n")


FIX_ROUNDS = ("- Review rounds: one, fix `fbea390` (report `reports/07-fix-1-report.md`), review "
              "of the fix (report `reports/08-review-fix-1-report.md`)\n")


def fix_record(events=FIX_EVENTS, rounds=None) -> str:
    """A cycle record whose Events table has the output column the fix rounds are read from, and
    whose line `Review rounds` names the rounds the Events name (or none, without events)."""
    if rounds is None:
        rounds = FIX_ROUNDS if events else "- Review rounds: none yet\n"
    text = record(remarks="- Process remarks on the-way: none\n").replace(
        "| Time | Stage |\n|---|---|\n", FULL_EVENTS + events)
    return text.replace("- Status: request open\n", "- Status: request open\n" + rounds)


def one_fix_round() -> str:
    review = "Review whole change (general-purpose) — turn 1"
    fix = "Fix 1 of the findings (general-purpose) — turn 1"
    fix_review = "Review of the fix 1 (general-purpose) — turn 1"
    return (STAGES_HEADER
            + stage_row(1, "orchestrator", "model-a", 1000, 0, 100)
            + stage_row(2, review, "model-a", 2000, 1000, 200)
            + stage_row(3, fix, "model-b", 400, 100, 40)
            + stage_row(4, fix_review, "model-a", 300, 0, 30))


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

    def test_a_fix_round_at_a_test_price_list_gives_the_cost_and_no_share(self):
        done = self.count(one_fix_round())
        self.assertEqual(0, done.returncode, done.stderr)
        # Worked by hand, in millionths of a dollar: stage 1 is 1000*2 + 100*10 = 3000; stage 2 is
        # 1000*2 + 1000*1 + 200*10 = 5000; stage 3 is 300*4 + 100*0.5 + 40*20 = 2050; stage 4 is
        # 300*2 + 30*10 = 900. The total is 10950. The share is unknown: stages.md names the
        # subagents, which cannot be tied to the round reliably.
        row = self.cost_row()
        self.assertEqual(["product", "2026-01-01", "0.010950", "1", "unknown"],
                         [row[0], row[2], row[3], row[4], row[5]])
        self.assertTrue(any("cannot be tied to the rounds reliably" in why
                            for why in self.unknown_why("Fix rounds share")))

    def test_resumed_turns_named_with_fix_do_not_give_a_share(self):
        # The archived form: the author is one subagent with a fix in its second turn, and its
        # name holds the word `fix`. Counting whole stages by name gave the whole author as the
        # fix round (99.6 % in the review's run); the share must be unknown.
        stages = (STAGES_HEADER
                  + stage_row(1, "Author: fix the login bug (general-purpose) — turn 1",
                              "model-a", 1000, 0, 100)
                  + stage_row(2, "Author: fix the login bug (general-purpose) — turn 2",
                              "model-a", 400, 0, 40)
                  + stage_row(3, "Reviewer: review the fix of the login bug (general-purpose) "
                                 "— turn 1", "model-a", 2000, 0, 200)
                  + stage_row(4, "Reviewer: review the fix of the login bug (general-purpose) "
                                 "— turn 2", "model-a", 300, 0, 30))
        self.assertEqual(0, self.count(stages).returncode)
        row = self.cost_row()
        self.assertEqual(["unknown"], [row[5]])

    def test_orchestrator_rows_naming_fix_subagents_are_in_no_fix_round(self):
        # Two rows of the orchestrator's work while subagents run in parallel name a fix and a
        # review; no subagent of the cycle was a fix. Counting their names gave a share of 49.7 %.
        stages = (STAGES_HEADER
                  + stage_row(1, "orchestrator", "model-a", 1000, 0, 100)
                  + stage_row(2, "orchestrator while in parallel: Fix typos (general-purpose), "
                                 "One author (general-purpose)", "model-a", 2000, 0, 200)
                  + stage_row(3, "orchestrator while in parallel: Review the fix "
                                 "(general-purpose), Other (general-purpose)", "model-a", 300, 0, 30))
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual(["unknown"], [self.cost_row()[5]])

    def test_a_cycle_naming_no_fix_round_and_no_fix_stage_has_a_share_of_zero(self):
        stages = (STAGES_HEADER
                  + stage_row(1, "orchestrator", "model-a", 1000, 0, 100)
                  + stage_row(2, "orchestrator while in parallel: Fix typos (general-purpose), "
                                 "Other (general-purpose)", "model-a", 2000, 0, 200)
                  + stage_row(3, "Review whole change (general-purpose) — turn 1", "model-a",
                              300, 0, 30))
        done = self.count(stages, record_text=fix_record(events=""))
        self.assertEqual(0, done.returncode, done.stderr)
        row = self.cost_row()
        self.assertEqual(["0", "0.0%"], [row[4], row[5]])

    def test_review_rounds_naming_a_fix_the_events_lack_leave_the_share_unknown(self):
        record_text = fix_record(events="", rounds="- Review rounds: one, fix `x` "
                                                   "(report `reports/07-fix-1-report.md`)\n")
        stages = STAGES_HEADER + stage_row(1, "orchestrator", "model-a", 1000, 0, 100)
        done = self.count(stages, record_text=record_text)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(["unknown"], [self.cost_row()[5]])
        self.assertTrue(any("do not agree" in why for why in self.unknown_why("Fix rounds share")))

    def test_a_record_without_a_review_rounds_line_leaves_the_share_unknown(self):
        stages = STAGES_HEADER + stage_row(1, "orchestrator", "model-a", 1000, 0, 100)
        done = self.count(stages, record_text=fix_record(events="", rounds=""))
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(["unknown"], [self.cost_row()[5]])
        self.assertTrue(any("no line `Review rounds`" in why
                            for why in self.unknown_why("Fix rounds share")))

    def test_a_stage_with_no_token_usage_leaves_the_cost_unknown(self):
        # cycle_stages.py writes the model mark `—` with zero counts for a stage it found no usage
        # for; that is not a cost of zero.
        stages = STAGES_HEADER + stage_row(1, "orchestrator", "—", 0, 0, 0)
        self.assertEqual(0, self.count(stages).returncode)
        self.assertEqual("unknown", self.cost_row()[3])
        self.assertTrue(any("no token usage" in why for why in self.unknown_why("Cost")))

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

    def test_fix_stages_the_record_does_not_name_leave_only_the_share_unknown(self):
        done = self.count(one_fix_round(), record_text=fix_record(events=""))
        self.assertEqual(0, done.returncode, done.stderr)
        row = self.cost_row()
        self.assertEqual(["0.010950", "unknown"], [row[3], row[5]])
        self.assertTrue(any("the record names no fix round" in why
                            for why in self.unknown_why("Fix rounds share")))

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
