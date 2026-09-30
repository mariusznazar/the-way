"""Probe and watch of the fact `git-path-patterns`: git matches a path pattern of an attributes file
by the rules of `.gitignore` patterns, except that a negative pattern is forbidden and a pattern
that matches a directory does not match the paths inside it.

The probe asks `git -c core.ignorecase=false check-attr` in a temporary repository; the watch reads
the passages of the fact's *Source* at their address. Expected values are written out (WAY-69).
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fact_probes  # noqa: E402

IDENTIFIER = "git-path-patterns"


def differences(repository, attributes, expected):
    """Every (path, attribute) whose value `git check-attr` gives otherwise than expected."""
    names = sorted({name for _, name in expected})
    paths = sorted({path for path, _ in expected})
    repository.write(".gitattributes", attributes)
    answered = repository.attributes(names, paths)
    return ["`%s` on %s is %s, not %s" % (name, path, answered.get((path, name), "missing"),
                                          value)
            for (path, name), value in sorted(expected.items())
            if answered.get((path, name)) != value]


class GitPathPatternsProbe(fact_probes.FactCheck):

    def test_patterns_match_by_the_gitignore_rules(self):
        # fact: git-path-patterns/1
        repository = self.repository()
        found = differences(repository, "\n".join([
            "*.txt glob",                # no slash: matches at any depth
            "/anchored.md anchored",     # a leading slash anchors it to the file's directory
            "doc/*.md middle",           # a slash in the middle: relative to that directory
            "a/**/z deep",               # `/**/` matches zero or more directories
            "*.TXT case",                # letter case counts under core.ignorecase=false
            "file?.c question",          # `?` matches one character other than `/`
            "[ab].h range",              # a range matches one character of the set
        ]) + "\n", {
            ("a.txt", "glob"): "set", ("deep/dir/b.txt", "glob"): "set",
            ("anchored.md", "anchored"): "set", ("sub/anchored.md", "anchored"): "unspecified",
            ("doc/x.md", "middle"): "set", ("doc/sub/x.md", "middle"): "unspecified",
            ("sub/doc/x.md", "middle"): "unspecified",
            ("a/z", "deep"): "set", ("a/b/c/z", "deep"): "set",
            ("a.txt", "case"): "unspecified", ("A.TXT", "case"): "set",
            ("file1.c", "question"): "set", ("file12.c", "question"): "unspecified",
            ("a.h", "range"): "set", ("c.h", "range"): "unspecified",
        })
        self.judge_release(IDENTIFIER, "git", repository.release(), found)

    def test_a_negative_pattern_is_forbidden(self):
        # fact: git-path-patterns/1
        repository = self.repository()
        found = differences(repository, "*.txt probe\n!keep.txt -probe\n!odd.md other\n", {
            # a negative line has no effect: keep.txt keeps the attribute the line above set,
            # and the line matches neither the path it names nor one spelled with its `!`
            ("keep.txt", "probe"): "set", ("other.txt", "probe"): "set",
            ("odd.md", "other"): "unspecified", ("!odd.md", "other"): "unspecified",
        })
        self.judge_release(IDENTIFIER, "git", repository.release(), found)

    def test_a_directory_pattern_does_not_match_the_paths_inside_it(self):
        # fact: git-path-patterns/1
        repository = self.repository()
        for path in ("build/app.o", "out/app.o", "logs/app.log", "logs/old/app.log"):
            repository.write(path)
        found = differences(repository, "build name\nout/ slash\nlogs/** stars\n", {
            ("build", "name"): "set",                   # the directory itself matches
            ("build/app.o", "name"): "unspecified",     # a path inside it does not
            ("out/app.o", "slash"): "unspecified",
            ("logs/app.log", "stars"): "set",           # `path/**` reaches inside, as advised
            ("logs/old/app.log", "stars"): "set",
        })
        self.judge_release(IDENTIFIER, "git", repository.release(), found)


class GitPathPatternsWatch(fact_probes.FactCheck):

    def test_the_passages_stand(self):
        # fact: git-path-patterns/1
        self.watch_passages(IDENTIFIER)


if __name__ == "__main__":
    unittest.main()
