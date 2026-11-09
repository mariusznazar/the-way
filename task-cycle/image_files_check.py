"""The image files in the copy of a cycle record (WAY-316).

Usage:

    python -B task-cycle/image_files_check.py TARGET

In a product, the path starts with `.the-way/`. TARGET is the copy of a cycle record, the directory
`docs/task-cycles/<task-slug>/`, or a single file. A directory is read through every file below it;
a file is checked alone.

The script lists, one per line as `<file>: image file`, each file whose name ends, in either case
of its letters, in one of `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.bmp`, `.tif`, `.tiff`,
`.ico`, `.svg`, `.avif` or `.heic`, in the order of the paths, then a last line,
`checked: ... files, ... listed`. Exit code: 0 when nothing is listed; 1 with the files listed; 2
with `Error: <message>` on stderr when the argument is wrong.

It recognizes an image by the end of its name alone and never opens a file, so it does not catch
an image saved under another name or none, or one written into a text, such as a `data:` URL, an
archive that holds an image or a file named like an image that holds text. It writes no file and
runs nothing. It is a separate script from `private_paths_check.py`, which reads the text of the
files for paths and links, skipping as binary a file with a NUL byte near its start, which most
images have.

Standard library only.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path

IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".ico",
                    ".svg", ".avif", ".heic")


class ImageFilesError(Exception):
    """An argument that is wrong."""


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # type: ignore[override]
        raise ImageFilesError(message)


def display(value: object) -> str:
    """Keep text taken from the file names inside one report line."""
    return "".join(char if char.isprintable() else ascii(char)[1:-1] for char in str(value))


@dataclass
class Result:
    listed: list[str] = field(default_factory=list)
    files: int = 0


def is_image_name(name: str) -> bool:
    return name.lower().endswith(IMAGE_EXTENSIONS)


def check(target: Path) -> Result:
    """The image files of a file, or of every file below a directory."""
    result = Result()
    if target.is_dir():
        paths = sorted((path for path in target.rglob("*") if path.is_file()),
                       key=lambda found: found.as_posix())
    elif target.is_file():
        paths = [target]
    else:
        raise ImageFilesError(f"{display(target)} is no file or directory; give the copy of the "
                              f"record")
    for path in paths:
        result.files += 1
        if is_image_name(path.name):
            result.listed.append(path.as_posix())
    return result


def main(argv: list[str] | None = None) -> int:
    parser = Parser(description=__doc__.split("\n\n")[0])
    parser.add_argument("target", type=Path, metavar="TARGET")
    try:
        args = parser.parse_args(argv)
        result = check(args.target)
    except ImageFilesError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    for path in result.listed:
        sys.stdout.write(f"{display(path)}: image file\n")
    sys.stdout.write(f"checked: {result.files} files, {len(result.listed)} listed\n")
    return 1 if result.listed else 0


if __name__ == "__main__":
    sys.exit(main())
