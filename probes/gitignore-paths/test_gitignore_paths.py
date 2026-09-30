"""Probe and watch of the fact `gitignore-paths`: within one level of precedence of its gitignore
sources, the last pattern that matches a path decides whether git ignores it, and a file whose
parent directory is excluded cannot be re-included.

The probe asks `git -c core.ignorecase=false check-ignore` in a temporary repository; the watch
reads the passages of the fact's *Source* at their address. Expected values are written out
(WAY-69).
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "gitignore-paths"


def differences(repository, expected):
    """Every path `git check-ignore` answers otherwise than expected: True where it is ignored."""
    for path in expected:
        repository.write(path)
    ignored = repository.ignored(sorted(expected))
    return ["%s is %s, not %s" % (path, "ignored" if path in ignored else "not ignored",
                                  "ignored" if wanted else "not ignored")
            for path, wanted in sorted(expected.items()) if (path in ignored) != wanted]


class GitignorePathsProbe(fact_probes.FactCheck):

    def test_the_last_matching_pattern_of_a_level_decides(self):
        # fact: gitignore-paths/1
        repository = self.repository()
        repository.write("first/.gitignore", "*.log\n!keep.log\n")
        repository.write("second/.gitignore", "!keep.log\n*.log\n")
        repository.write(".git/info/exclude", "*.tmp\n!keep.tmp\n")
        found = differences(repository, {
            "first/other.log": True, "first/keep.log": False,     # the negation comes last
            "second/other.log": True, "second/keep.log": True,    # the pattern comes last
            "other.tmp": True, "keep.tmp": False,                 # the same in info/exclude
        })
        self.judge_release(IDENTIFIER, "git", repository.release(), found)

    def test_a_file_under_an_excluded_directory_cannot_be_re_included(self):
        # fact: gitignore-paths/1
        repository = self.repository()
        repository.write(".gitignore", "build/\n!build/keep.txt\ncache/*\n!cache/keep.txt\n"
                                       "vendor/\n")
        repository.write("vendor/.gitignore", "!keep.txt\n")
        found = differences(repository, {
            "build/keep.txt": True,           # its parent directory is excluded
            "vendor/keep.txt": True,          # also by a pattern in the excluded directory
            "cache/keep.txt": False,          # only the contents are excluded, not the directory
            "cache/other.txt": True,
        })
        self.judge_release(IDENTIFIER, "git", repository.release(), found)


class GitignorePathsWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: gitignore-paths/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()
