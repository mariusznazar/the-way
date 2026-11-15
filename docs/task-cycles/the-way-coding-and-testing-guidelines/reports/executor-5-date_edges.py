from datetime import datetime, timezone

CASES = [
    "2026-10-06T09:00:00.000Z",
    "2026-10-06T09:00:00Z",
    "2026-10-06T09:00:00+02:00",
    "2026-10-06T09:00:00",
    "2026-10-06T09:00Z",
    "2026-10-06T09:00:00z",
    "Z2026-10-06T09:00:00",
    "2026-10-06Z09:00:00",
    "2026-10-06T09:00:00.000ZZ",
    "2026-10-06T09:00:00Z.000",
    "",
    "not a time",
]


def old(value):
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return "ValueError"


def new(value):
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return "ValueError"


for case in CASES:
    a, b = old(case), new(case)
    same = a == b and (a == "ValueError" or a.utcoffset() == b.utcoffset())
    print(f"{case!r:36} old={a!s:40} new={b!s:40} same={same}")
