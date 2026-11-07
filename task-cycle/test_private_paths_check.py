"""Tests of task-cycle/private_paths_check.py on texts, records and descriptions written for the tests.

The fixtures use made-up names (`alice`, `proj`, `Meetings`) and write a backslash as `BS`, since a
backslash in a plain Python literal silently becomes another character. Expected hits are written
out here, never taken from the script.
"""

from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import private_paths_check  # noqa: E402

BS = chr(92)


def hits(text: str) -> list[tuple[int, str, str]]:
    return private_paths_check.find_in_text(text)


def shown(text: str) -> list[str]:
    return [hit[2] for hit in hits(text)]


class WindowsPathTest(unittest.TestCase):
    def test_a_drive_path_with_backslashes_is_listed(self) -> None:
        text = "The worktree is C:" + BS + "Work" + BS + "proj" + BS + "wt, as the log says."
        self.assertEqual(hits(text), [(1, "absolute path", "C:" + BS + "Work" + BS + "proj" + BS + "wt")])

    def test_a_drive_path_with_slashes_is_listed_in_either_case_of_the_letter(self) -> None:
        self.assertEqual(shown("at C:/Work/proj and d:/data/x"), ["C:/Work/proj", "d:/data/x"])

    def test_the_home_directory_of_windows_is_listed(self) -> None:
        text = "C:" + BS + "Users" + BS + "alice" + BS + ".config" + BS + "tool.json"
        self.assertEqual(shown(text), [text])

    def test_a_home_directory_without_its_drive_is_listed(self) -> None:
        text = "under " + BS + "Users" + BS + "alice" + BS + "Documents"
        self.assertEqual(shown(text), [BS + "Users" + BS + "alice" + BS + "Documents"])

    def test_a_path_in_a_json_string_with_doubled_backslashes_is_listed(self) -> None:
        text = '{"path": "C:' + BS + BS + "Work" + BS + BS + 'proj"}'
        self.assertEqual([hit[1] for hit in hits(text)], ["absolute path"])

    def test_a_path_ends_before_a_space_a_quote_a_bracket_or_closing_punctuation(self) -> None:
        for text, expected in (
                ("`C:/Work/proj/a.md`", "C:/Work/proj/a.md"),
                ("(C:/Work/proj/a.md)", "C:/Work/proj/a.md"),
                ('"C:/Work/proj/a.md"', "C:/Work/proj/a.md"),
                ("see C:/Work/proj/a.md.", "C:/Work/proj/a.md"),
                ("C:/Work/proj, then", "C:/Work/proj"),
                ("C:/Work/The Brain/x", "C:/Work/The")):
            self.assertEqual(shown(text), [expected], text)

    def test_a_letter_that_ends_a_word_starts_no_drive(self) -> None:
        # A match there would list every URL and every `Note:` of prose.
        for text in ("https://example.com/a/b", "http://host/c/d", "ftp://h/x", "Status: ok",
                     "Note: a / b", "see Q: and A: b","key:" + BS + "n and ab:" + BS + "x"):
            self.assertEqual(hits(text), [], text)


class PosixPathTest(unittest.TestCase):
    def test_the_posix_form_of_a_drive_is_listed(self) -> None:
        self.assertEqual(shown("/c/Work/proj and /d/data"), ["/c/Work/proj", "/d/data"])

    def test_the_wsl_and_cygwin_forms_of_a_drive_are_listed(self) -> None:
        self.assertEqual(shown("/mnt/c/Work/proj, /cygdrive/d/data"),
                         ["/mnt/c/Work/proj", "/cygdrive/d/data"])

    def test_the_home_directories_of_linux_and_macos_are_listed(self) -> None:
        self.assertEqual(shown("/home/alice/work and /Users/alice/Library/x"),
                         ["/home/alice/work", "/Users/alice/Library/x"])

    def test_a_home_directory_with_no_name_or_a_placeholder_is_no_hit(self) -> None:
        for text in ("the /home/ directory", "write /home/<you>/x", "the /Users/ folder"):
            self.assertEqual(hits(text), [], text)

    def test_text_that_only_looks_like_a_drive_or_a_home_is_no_hit(self) -> None:
        for text in ("and/or", "w/o/x", "2026/11/07", "s/a/b/", "https://host/c/path",
                     "https://example.com/home/alice", "x/home/alice", "../home/alice",
                     "~/home/alice", "src/c/main.py", "a /cd/x", "/ab/x"):
            self.assertEqual(hits(text), [], text)

    def test_a_home_path_reached_through_tilde_or_a_relative_path_is_not_listed(self) -> None:
        for text in ("~/.claude/x", "../x/y", "./a/b", "task-cycle/remarks_check.py",
                     BS + BS + "host" + BS + "share"):
            self.assertEqual(hits(text), [], text)


class NoteLinkTest(unittest.TestCase):
    def test_a_link_with_a_title_an_alias_a_heading_or_an_embed_is_listed(self) -> None:
        text = "[[Meetings]] [[Meetings|the notes]] [[Meetings#Plan]] ![[photo.png]]"
        self.assertEqual(hits(text), [
            (1, "note link", "[[Meetings]]"), (1, "note link", "[[Meetings|the notes]]"),
            (1, "note link", "[[Meetings#Plan]]"), (1, "note link", "[[photo.png]]")])

    def test_a_link_in_front_matter_is_listed(self) -> None:
        text = '---\ntitle: "x"\nrelated: "[[(P) Project]]"\n---\n'
        self.assertEqual(hits(text), [(3, "note link", "[[(P) Project]]")])

    def test_the_form_used_to_write_about_the_link_is_no_hit(self) -> None:
        for text in ("a link written `[[...]]` in the text", "`[[…]]`", "[[ ]]", "[[]]", "[[__]]"):
            self.assertEqual(hits(text), [], text)

    def test_the_shells_double_bracket_test_is_no_hit(self) -> None:
        self.assertEqual(hits('if [[ -f "$file" ]]; then echo yes; fi'), [])

    def test_a_link_that_breaks_over_a_line_is_no_hit(self) -> None:
        self.assertEqual(hits("[[Meetings\nand more]]"), [])

    def test_single_brackets_and_markdown_links_are_no_hit(self) -> None:
        self.assertEqual(hits("[a note](notes/a.md) and [b] and [[c]"), [])


class PlaceTest(unittest.TestCase):
    def test_the_line_of_each_hit_counts_from_one_in_any_line_ending(self) -> None:
        for end in ("\n", "\r\n", "\r"):
            text = end.join(["first", "path C:/Work/a", "", "link [[Note]] and /home/alice/x", ""])
            self.assertEqual([hit[0] for hit in hits(text)], [2, 4, 4], repr(end))

    def test_a_hit_inside_fenced_code_or_a_code_span_is_listed(self) -> None:
        text = "```\nC:/Work/proj\n```\n`[[Note]]`\n"
        self.assertEqual(hits(text), [(2, "absolute path", "C:/Work/proj"),
                                      (4, "note link", "[[Note]]")])

    def test_two_hits_on_one_line_are_two_hits(self) -> None:
        self.assertEqual(shown("C:/a/x and /home/bob/y [[Z]]"), ["C:/a/x", "/home/bob/y", "[[Z]]"])


def run_main(arguments: list[str]) -> tuple[int, str, str]:
    stdout, stderr = io.StringIO(), io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        code = private_paths_check.main(arguments)
    return code, stdout.getvalue(), stderr.getvalue()


class CommandTest(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, name: str, text: str) -> Path:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))
        return path

    def listing(self, out: str) -> list[str]:
        return [line for line in out.splitlines() if not line.startswith("checked: ")]

    def test_a_clean_directory_gives_exit_zero_and_only_the_summary(self) -> None:
        self.write("record/cycle.md", "# Record\n\nThe path is task-cycle/x.py.\n")
        self.write("record/reports/01-report.md", "Nothing here: https://example.com/a\n")
        code, out, err = run_main([str(self.root / "record")])
        self.assertEqual((code, err), (0, ""))
        self.assertEqual(out, "checked: 2 files, 0 listed\n")

    def test_a_hit_is_listed_with_its_file_and_line_and_exit_one(self) -> None:
        self.write("record/cycle.md", "# Record\n\n- Task source: C:/Work/proj/task.md\n")
        code, out, err = run_main([str(self.root / "record")])
        self.assertEqual((code, err), (1, ""))
        base = (self.root / "record").as_posix()
        self.assertEqual(self.listing(out),
                         [f"{base}/cycle.md:3: absolute path: C:/Work/proj/task.md"])
        self.assertEqual(out.splitlines()[-1], "checked: 1 files, 1 listed")

    def test_every_file_below_the_directory_is_read_in_the_order_of_its_path(self) -> None:
        self.write("record/reports/b/x.md", "[[B]]\n")
        self.write("record/cycle.md", "/home/alice/c\n")
        self.write("record/reports/a/z.md", "[[A]]\n")
        self.write("record/sub/deep/notes.txt", "D:/d\n")
        _, out, _ = run_main([str(self.root / "record")])
        self.assertEqual([line.rsplit(": ", 1)[1] for line in self.listing(out)],
                         ["/home/alice/c", "[[A]]", "[[B]]", "D:/d"])

    def test_a_single_file_is_read_alone(self) -> None:
        self.write("other.md", "[[Not read]]\n")
        path = self.write("request.md", "**State: ready** - ok\n\nsee [[Note]]\n")
        code, out, _ = run_main([str(path)])
        self.assertEqual(code, 1)
        self.assertEqual(self.listing(out), [f"{path.as_posix()}:3: note link: [[Note]]"])
        self.assertEqual(out.splitlines()[-1], "checked: 1 files, 1 listed")

    def test_a_block_in_another_language_is_read_like_the_rest(self) -> None:
        text = ("**State: ready** - ok\n\n<details>\n<summary>W Twoim jezyku</summary>\n\n"
                "Zadanie jest w [[Notatka zadania]].\n\n</details>\n")
        path = self.write("request.md", text)
        code, out, _ = run_main([str(path)])
        self.assertEqual(code, 1)
        self.assertEqual(self.listing(out), [f"{path.as_posix()}:6: note link: [[Notatka zadania]]"])

    def test_a_text_that_is_not_ascii_is_listed_as_it_stands(self) -> None:
        path = self.write("request.md", "zob. [[Zażółć gęślą]] i C:/Praca/żółw\n")
        _, out, _ = run_main([str(path)])
        self.assertEqual(self.listing(out), [
            f"{path.as_posix()}:1: note link: [[Zażółć gęślą]]",
            f"{path.as_posix()}:1: absolute path: C:/Praca/żółw"])

    def test_a_binary_file_is_not_read_and_is_counted(self) -> None:
        self.write("record/cycle.md", "# Record\n")
        (self.root / "record" / "shot.png").write_bytes(b"\x89PNG\r\n\x1a\n\0\0C:/Work/x\0")
        code, out, _ = run_main([str(self.root / "record")])
        self.assertEqual(code, 0)
        self.assertEqual(out, "checked: 1 files, 0 listed, 1 binary files not read\n")

    def test_a_directory_with_no_file_lists_nothing(self) -> None:
        (self.root / "empty").mkdir()
        code, out, _ = run_main([str(self.root / "empty")])
        self.assertEqual((code, out), (0, "checked: 0 files, 0 listed\n"))

    def test_a_missing_path_or_a_wrong_argument_exits_two(self) -> None:
        path = self.write("request.md", "x\n")
        for arguments in ([str(self.root / "absent")], [], [str(path), "extra"]):
            code, out, err = run_main(arguments)
            self.assertEqual(code, 2, arguments)
            self.assertEqual(out, "")
            self.assertTrue(err.startswith("Error: "), err)

    def test_a_file_that_is_not_utf8_exits_two_with_nothing_listed(self) -> None:
        self.write("record/cycle.md", "C:/Work/x\n")
        (self.root / "record" / "late.md").write_bytes("zażółć".encode("cp1250"))
        code, out, err = run_main([str(self.root / "record")])
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertTrue(err.startswith("Error: "), err)

    def test_the_script_rewrites_nothing(self) -> None:
        path = self.write("record/cycle.md", "C:/Work/x and [[Note]]\n")
        before = (path.read_bytes(), sorted(p.name for p in self.root.rglob("*")))
        run_main([str(self.root / "record")])
        self.assertEqual((path.read_bytes(), sorted(p.name for p in self.root.rglob("*"))), before)

    def test_a_control_character_in_a_hit_is_shown_escaped(self) -> None:
        path = self.write("request.md", "C:/Work/x\x1by\n")
        _, out, _ = run_main([str(path)])
        self.assertEqual(self.listing(out),
                         [f"{path.as_posix()}:1: absolute path: C:/Work/x" + BS + "x1by"])


if __name__ == "__main__":
    unittest.main()
