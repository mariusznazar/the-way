"""Tests of task-cycle/image_files_check.py on directories and files written for the tests.

An image is recognized by the end of its file name, so the fixtures are files with that name and
any content; one test writes the bytes of a real image header to show that the content is never
read. Expected listings are written out here, never taken from the script.
"""

from __future__ import annotations

import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import image_files_check  # noqa: E402

SCRIPT = HERE / "image_files_check.py"
EXTENSIONS = [".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".ico", ".svg",
              ".avif", ".heic"]


def run_main(arguments: list[str]) -> tuple[int, str, str]:
    stdout, stderr = io.StringIO(), io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        code = image_files_check.main(arguments)
    return code, stdout.getvalue(), stderr.getvalue()


class ImageFilesCheckTest(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, name: str, data: bytes = b"x") -> Path:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def listing(self, out: str) -> list[str]:
        return [line for line in out.splitlines() if not line.startswith("checked: ")]

    # invariant: record-copy-image-check
    def test_a_record_copy_with_an_image_file_is_listed_and_exits_one(self) -> None:
        self.write("record/cycle.md", b"# Record\n")
        self.write("record/reports/screen.png", b"\x89PNG\r\n\x1a\n")
        code, out, err = run_main([str(self.root / "record")])
        base = (self.root / "record").as_posix()
        self.assertEqual((code, err), (1, ""))
        self.assertEqual(self.listing(out), [f"{base}/reports/screen.png: image file"])
        self.assertEqual(out.splitlines()[-1], "checked: 2 files, 1 listed")

    # invariant: record-copy-image-check
    def test_a_record_copy_with_no_image_file_lists_nothing_and_exits_zero(self) -> None:
        self.write("record/cycle.md", b"# Record\n")
        self.write("record/reports/01-report.md", b"The screenshot lies elsewhere.\n")
        code, out, err = run_main([str(self.root / "record")])
        self.assertEqual((code, err, out), (0, "", "checked: 2 files, 0 listed\n"))

    # invariant: record-copy-image-check
    def test_every_extension_of_the_list_is_an_image_in_either_case(self) -> None:
        for extension in EXTENSIONS:
            for name in ("shot" + extension, "Shot" + extension.upper()):
                with self.subTest(name=name):
                    path = self.write(f"one/{name}")
                    code, out, _ = run_main([str(path.parent)])
                    self.assertEqual(code, 1)
                    self.assertEqual(self.listing(out), [f"{path.as_posix()}: image file"])
                    path.unlink()

    def test_files_that_only_look_like_an_image_name_are_no_image(self) -> None:
        for name in ("notes.png.md", "png", "a.pngx", "photo.jpg.txt", "image", "x.svgz.md",
                     "report-png.md"):
            self.write(f"record/{name}", b"text\n")
        code, out, _ = run_main([str(self.root / "record")])
        self.assertEqual((code, out), (0, "checked: 7 files, 0 listed\n"))

    def test_a_directory_named_like_an_image_is_no_file_and_its_text_is_no_image(self) -> None:
        self.write("record/gallery.png/index.md", b"text\n")
        code, out, _ = run_main([str(self.root / "record")])
        self.assertEqual((code, out), (0, "checked: 1 files, 0 listed\n"))

    def test_images_are_listed_in_the_order_of_their_paths_at_any_depth(self) -> None:
        self.write("record/reports/b/two.png")
        self.write("record/zz.gif")
        self.write("record/reports/a/deep/one.jpg")
        self.write("record/reports/a/note.md", b"text\n")
        _, out, _ = run_main([str(self.root / "record")])
        base = (self.root / "record").as_posix()
        self.assertEqual(self.listing(out), [
            f"{base}/reports/a/deep/one.jpg: image file",
            f"{base}/reports/b/two.png: image file",
            f"{base}/zz.gif: image file"])
        self.assertEqual(out.splitlines()[-1], "checked: 4 files, 3 listed")

    def test_a_single_file_is_checked_alone(self) -> None:
        self.write("other.png")
        image = self.write("one.webp")
        text = self.write("one.md", b"text\n")
        self.assertEqual(run_main([str(image)])[:2],
                         (1, f"{image.as_posix()}: image file\nchecked: 1 files, 1 listed\n"))
        self.assertEqual(run_main([str(text)])[:2], (0, "checked: 1 files, 0 listed\n"))

    def test_the_content_of_a_file_is_never_read(self) -> None:
        # A text that is no valid UTF-8 and a text named like an image: only the name counts.
        self.write("record/late.md", "zażółć".encode("cp1250"))
        self.write("record/shot.png", "plain text".encode("utf-8"))
        code, out, err = run_main([str(self.root / "record")])
        self.assertEqual((code, err), (1, ""))
        self.assertEqual(self.listing(out), [f"{(self.root / 'record').as_posix()}/shot.png: image file"])

    def test_an_empty_directory_lists_nothing(self) -> None:
        (self.root / "empty").mkdir()
        self.assertEqual(run_main([str(self.root / "empty")])[:2], (0, "checked: 0 files, 0 listed\n"))

    def test_a_missing_path_or_a_wrong_argument_exits_two_with_nothing_listed(self) -> None:
        path = self.write("one.md", b"x\n")
        for arguments in ([str(self.root / "absent")], [], [str(path), "extra"]):
            code, out, err = run_main(arguments)
            self.assertEqual(code, 2, arguments)
            self.assertEqual(out, "")
            self.assertTrue(err.startswith("Error: "), err)

    def test_the_script_changes_nothing(self) -> None:
        self.write("record/cycle.md", b"# Record\n")
        image = self.write("record/shot.png", b"data")
        before = sorted((p.name, p.read_bytes()) for p in self.root.rglob("*") if p.is_file())
        run_main([str(self.root / "record")])
        after = sorted((p.name, p.read_bytes()) for p in self.root.rglob("*") if p.is_file())
        self.assertEqual(after, before)
        self.assertTrue(image.exists())

    def test_a_control_character_in_a_file_name_is_shown_escaped(self) -> None:
        self.write("record/a" + chr(0x85) + "b.png")
        _, out, _ = run_main([str(self.root / "record")])
        self.assertEqual(self.listing(out),
                         [f"{(self.root / 'record').as_posix()}/a" + chr(92) + "x85b.png: image file"])

    # invariant: record-copy-image-check
    def test_the_command_ends_with_the_exit_code_of_the_check(self) -> None:
        self.write("record/shot.png")
        listed = subprocess.run([sys.executable, "-B", str(SCRIPT), str(self.root / "record")],
                                capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(listed.returncode, 1)
        self.assertEqual(listed.stdout.splitlines()[-1], "checked: 1 files, 1 listed")
        self.write("clean/cycle.md", b"# Record\n")
        clean = subprocess.run([sys.executable, "-B", str(SCRIPT), str(self.root / "clean")],
                               capture_output=True, text=True, encoding="utf-8")
        self.assertEqual((clean.returncode, clean.stdout), (0, "checked: 1 files, 0 listed\n"))


if __name__ == "__main__":
    unittest.main()
