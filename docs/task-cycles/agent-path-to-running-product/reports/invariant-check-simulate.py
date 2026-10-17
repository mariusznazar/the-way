"""Run project-level tests against readiness_check with the invariant's mark clause patched in.

A throwaway model of the sentence, only to show the new checks pass once the rule is met."""
import os
import sys
import unittest

root = sys.argv[1]
sys.path.insert(0, os.path.join(root, "project-level"))
import readiness_check  # noqa: E402

MARKS = ("logs:", "interface:", "development data:")
original = readiness_check.check


def technology_items(text):
    lines = text.replace("\r\n", "\n").split("\n")
    inside, items = False, []
    for line in lines:
        if line.startswith("## "):
            inside = line.strip() == "## Technology"
            continue
        if inside and line.startswith("- "):
            items.append(line[2:])
    return items


def check(text, before_approval=False):
    findings = list(original(text, before_approval))
    items = technology_items(text)
    for mark in MARKS:
        if not any(item.startswith(mark) for item in items):
            findings.append(readiness_check.Finding("g", 0, "no choice item begins with " + mark))
    return findings


readiness_check.check = check
os.chdir(os.path.join(root, "project-level"))
names = sys.argv[2:]
suite = unittest.defaultTestLoader.loadTestsFromNames(names)
result = unittest.TextTestRunner(verbosity=1).run(suite)
sys.exit(0 if result.wasSuccessful() else 1)
