"""The counting command of the audit of the process: the cycles whose records the user's
repositories hold in their history, and for each the version of the-way it ran on, its number of
process remarks and its times (WAY-330); and the problems of the user's
register of problems counted against those cycles (WAY-330).

Usage:

    python -B process-audit/audit_count.py [--locations FILE] [--repository KEY ...] [--today DATE]
                                           [--prices FILE]

In a product, the path starts with `.the-way/`. The command asks nothing and reads nothing from
stdin, and git runs with its terminal prompt off, so that a system scheduler can start it with no
human present and stdin closed or empty. DATE, written YYYY-MM-DD, is the day of the run, which
the days of waiting count to; the default is today in UTC, so that the same input and the same
DATE give the same bytes.

The places it needs are entries of the user's locations file (WAY-320), read as
`project-level/backlog_place.md` reads an entry; FILE defaults to `~/.the-way/locations.json`:

- under the key `the-way`, the entry `problem_register`, the file of the register of problems
  (`process-audit/problem_register.md` is its template), and the entry `audit_results`, the
  directory where the result is written;
- under the key of each repository whose cycles it reads — the name of a product, as the
  register's *Repository* column gives it — the entry `repository`, the path of that product's
  checkout. Each `--repository KEY` names a repository to read; without one, it reads every key
  that holds an entry `repository`. The-way's own checkout is the entry `repository` under
  `the-way`, and where that entry is missing, the checkout this script lies in.
  The command finds every place it needs by itself, since it runs with no human present, and the
  session that reads its result finds the same places by the same names.

A path is absolute or starts with `~`. Where the file, a key, an entry or the path an entry holds
is missing, or an entry is not a path, the command writes nothing and names it in an `Error:` line
on stderr, so that the skill of the audit asks the human; it never asks itself.

The price list is the file `price_list.md` beside this script (`--prices FILE` names another, as the
tests do). It holds the line `- List date: <YYYY-MM-DD>`, the date its prices were read, and a table
per provider whose header has the columns *Model id in stages.md*, *Input*, *Cached input*,
*Output*, *Cache write (5 minutes)* and *Cache write (1 hour)*, per million tokens; a table that
lacks one of them refuses the list, with its `Error:` naming the column. A `—` in *Input*, *Cached
input* or *Output* is a model with no price at all. A `—` in a write column is no price for that
lifetime: a model so marked is priced while the row of `stages.md` holds no writes of that
lifetime, and the cost of a row that holds some is `unknown`, never priced at the price of another
column. A cell that is neither a number nor `—` refuses the list (WAY-337, WAY-339). An error about
the locations file or the price list names its option, `--locations` or `--prices`, never the path
it was given (WAY-320).

A cycle is found where a commit adds the copy of its record, `docs/task-cycles/<folder>/cycle.md`
(`task-cycle/record_template.md`), in the history of every branch and remote branch, merges
followed into each of their parents. A cycle committed more than once, after a correction, counts
once: it is named by its repository and the first commit that adds a copy in its folder, the later
ones noted, and its values are read from the last copy, the most complete. For each cycle:

- *Process pin*: the version of the-way the cycle ran on — the commit the record's header line
  `Process pin` names (in earlier records `Process pin and ...`), or the commit it moved to where
  the line says the pin moved; for a cycle of the-way's own history, whose line names no commit,
  the commit of its line `Target branch and base`; the agents of such a cycle read the process from
  the worktree the cycle changes, which begins at that commit, so that commit is the process the
  cycle started under;
- *Remarks*: the number of entries under the record's item `Process remarks on the-way`, `0`
  where the item reads `none`;
- the agents' working time without waiting for tools, and the time they waited for tools, from the
  lines of the copy's `stages.md` that `task-cycle/cycle_stages.py` writes, as h:mm:ss;
- the cost at constant prices (WAY-337), from the copy's `stages.md` in either of its two
  forms. The newer form is known by its heading: each row of the section *Stages: start, waiting
  for tools and tokens by model* is priced at the list's prices, its input that is neither read
  from a cache nor written to one at the *Input* price, its cached input at the *Cached input*
  price, its cache writes of 5 minutes and of 1 hour each at its own write price, and its output at
  the *Output* price (the form with the two columns of the writes, *Cache write (5 minutes)* and
  *Cache write (1 hour)*; a form without them has no writes to price, and its row is priced by the
  other three). The older form has no such section: it is known by its table of tokens by model,
  the one table whose header row begins with *Model* and has the columns *Model*, *Total tokens*,
  *Input*, *Cached input* and *Output*, found exactly once, and each of its rows is priced in the
  same way.
  The older form is the form most cycles have, so a count that passed it over would leave most
  cycles with no cost.
  The cache writes are inside *Input* (`task-cycle/cycle_stages.py` folds them in). In the form
  with the two columns of the writes they are priced each at its own price; in the earlier forms of
  the section and in the older table, which have no such columns, they are priced as input: an
  approximation. A Codex row has `0` in both columns and is priced as a row with no writes. A model
  the list gives no price for, a model whose write price for a lifetime is `—` where the row holds
  writes of that lifetime, a row that does not read, a cached input above its input or cached
  input and writes together above it, a subagent stage with no token usage (the model `—`), a
  stage or a row whose usage the stage report could not read (the model `unknown`), a section where
  no stage has any, a table of the older form with no row, or such a table written twice, gives the
  cost `unknown`, never zero; a row of the orchestrator with no token usage, time it worked with no
  response of a model, costs nothing;
- *Fix rounds*: the number of findings files the record's item `Review rounds` names, `0` where it
  reads `none`. A fix round is the fix of a review's findings and the review of that fix; the
  orchestrator gives both the findings file, by its path in `reports/`, and the item names each
  round by that path: one entry for each round under the item, opening with the word `findings`
  and the path between backticks (`task-cycle/record_template.md`). An entry of a review that passed
  with no fix opens with the word `review` and holds the path of its report and the result `PASS`:
  it is no fix round, and it is not counted (WAY-337);
- the share of the cost spent in fix rounds (WAY-337): the cost of the subagent turns whose cell
  *Files named* in that section of `stages.md` names a findings file of a round the record names,
  each turn counted once, over the cycle's cost. It is `0.0%` only where the item reads `none` and
  no subagent turn was given a findings file, told by the word `findings` in its name as the check
  of process remarks tells one (WAY-294). It is `unknown`, with the reason, where the item is
  missing, doubled or names a round otherwise than by its findings file, where `stages.md` has no
  column *Files named* (an earlier form of the section), where `stages.md` is of the older form,
  whose table of tokens by model gives no turns (the number of fix rounds is still read from the
  record's item, as for the newer form), where a cell of it is not a list of files of `reports/`,
  where the rows of one turn disagree in their stage or their files, where a subagent turn's cell
  reads `unknown`, since that turn may serve a round, where a findings file the record names is
  named by fewer than two subagent turns, the fix and the review of that fix, or where a turn was
  given a findings file the record does not name: a wrong figure is worse than `unknown`. The cost
  is still given.

The process versions (WAY-339): each cycle is grouped by the version of the-way its
*Process pin* resolves to, the full commit that `git rev-parse --disambiguate` names in the
checkout of the-way. A cycle whose pin is unknown, does not resolve, is ambiguous, or whose commit
has no readable date stands apart as *no version*, with its reason, and is in no series. Versions
are ordered by their commit's date (`git log -1 --format=%ct`), ties by the full hash. The versions
are cut into series of two kinds, and a measure is compared only inside a series of its own kind:
no cell sets a number of one kind of series beside a number of the other, and each series is its own
subsection of the result, with the reason it begins where it does (WAY-339).

A series of the cost, in which the median cost and the answer Q3 are compared, is a run of
consecutive versions between which neither of these changes:

- the price list the costs are priced by (one list per run, so this never splits a run);
- `task-cycle/cycle_stages.py`, the script that measures the cost, and no other script
  (`git diff --quiet`; exit 1, or any other failure, counts as changed).

A series of the count of remarks, in which the answers Q1 and Q2 are compared, ends wherever a
series of the cost ends, and also at either of these changes:

- the register's list of classes: a date of *Added* or *Withdrawn* on or between the days of the
  two versions, or a list the register does not give in full, which splits at every version;
- the form of a stage report or the instructions of the reviewer, taken as the files of the-way
  under `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` and `task-cycle/spec`, and
  `task-cycle/agent-types/the-way-stage.md`, whose text the reviewer receives as its instruction
  (the same `git diff --quiet`). Any change of those files ends the series, whether or not it alters
  that form or those instructions: the count of remarks compares less, and the series of the cost,
  which none of these changes ends, compares across them.

The cost and the count of remarks are split apart because a change of the reviewer's instructions
is a change of the process: a series of the cost that it ended would never hold the two sides to
compare. The price: after such a change the cost cannot tell "the reviewer found more" from "the
process got dearer", while the count of remarks, whose meaning changes with the reviewer, has a
series that ends there.

Per version of a series of the cost: the median cost at constant prices of its cycles with a known
cost, and the answer Q3. Per version of a series of the count of remarks: the answers Q1 and Q2.
Each answer is `yes`, `no` or `unknown`. Q1, a contradiction with the product's settlements
that came out only after code was written: from two marks of the cycle's record, never from the
words of a reviewer's remarks or from the text of an item (WAY-403, WAY-404). It is yes where an
entry of *Review rounds* opens with the path of its findings file and `, contradiction yes`, or the
item *Discarded attempt* opens with `reason: ` and the marker `open design choice` in backticks, or
any of its entries does, where a cycle that discarded more than one attempt writes one entry for each
(the markers are `open design choice`, `reserved choice` and `size`, and only the start of the item,
or of the first line of each entry, is read; the entries are read only as a list: nothing stands
beside the colon, the first line under the item is an entry at the indent of the others and no plain
line stands at that indent or less; any other lines under the item are the details of one attempt,
read for a second `reason: ` followed by a backtick alone, whatever word stands there; a line at
the left margin ends the item). It is no where
every entry of *Review rounds* gives its mark, `contradiction no` or the form
of a review that passed with no fix, and *Discarded attempt* reads `none` or opens with the marker
`reserved choice` or `size` (each of its entries does, where it holds several). Each yes stands over
the unknown that the other item gives, but the mark of an entry is read only where *Review rounds*
is held once and in its form (no entry in neither form, no findings file named twice, nothing
beside its colon), and the marker only where *Discarded attempt* is held once. It is unknown,
with the one reason `the entry of a round does not say whether there was a contradiction` for a
round of any record, older or newer, where a fix round's entry carries no mark; with its own reason where *Discarded attempt* opens with no marker and does
not read `none`, where its lines are no entries at one indent alone or text stands beside its
colon and the whole text, which does not read `none`, holds a second `reason: ` followed by a
backtick or opens with no marker, where it is missing or doubled, or where *Review rounds* is
missing, doubled or in neither form. Q2, more than one third of the slices of the plans came
back too large: from the item
*Plan* (`none` on the one-author route leaves the cycle out; otherwise the figure written just
before the word `slices`, as in `8 slices`, and where there is none or more than one, unknown)
and the entries of *Slices returned too large* (`none` is 0); the answer is yes where three times
the sum of too-large slices is above the sum of planned slices, and unknown where the plan of a
cycle that has one is not read, since its slices could change the answer. Q3, the cost falls: the
median against the previous version of the same series, yes where lower, unknown where there is
none.

The measure versions (WAY-339, WAY-350): the same versions, in their own series, one kind of
series for each instrument. The count reads these measures and shows them with a median and a
comparison for each version, because the numbers lie in the records of cycles, which the session
of the audit does not open, and a comparison of before and after made by hand cannot say that a
change to the process worked. A series of the mechanism measures of `mechanism_measures.md`
begins at a version whose `task-cycle/cycle_measures.py` differs from the previous version's, and a
series of
the gate times of `gate_times.md` at one whose `task-cycle/gate_times.py` or `gate/run_tests.py`
differs, by the same test as the series of the cost (`git diff --quiet`; exit 1, or any failure,
counts as changed). No other change splits them: not the price list, a date of the register's list
of classes, a change under `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` or
`task-cycle/spec`, nor one of `task-cycle/agent-types/the-way-stage.md` or
`task-cycle/cycle_stages.py`, and neither script splits a series of the cost. The section
*Measure versions* gives, for each version of a series and each cycle-level measure, the number of
cycles that give a value, their median (the rule of the median of the cost) and whether it falls
against the previous version of the series, and for the gate times the total of the run and each
directory any run of the version has: the median and *Falls* take only the runs that passed (exit
code 0) during which no other gate run was going, and the runs not compared, those with another
gate, with an unknown count, that failed or whose exit code is unknown, are counted and their median
shown apart, never compared (WAY-350). A version in which no run passed alone, or no cycle gave a
value, has no comparison; a version in which no cycle gives a value or no run a time has one row,
with `—` for the measure, and a value in *Unknown values*. The values are kept as `Decimal` and a
median that is a half is written with its decimal.

A value a record or a `stages.md` does not give — an earlier form, a missing, doubled or malformed
line, a file that is no regular file, too large or not UTF-8 — is `unknown`, never zero, and the
result says why. A field of `stages.md` that the form the file's own signs name needs and the file
lacks is a missing field (WAY-344, which gives this command its own way to end): the values that
need it are `unknown`, the result is written, and the run ends with exit 1 and, for each missing
field, a line on stderr `Error: repository `<key>`: cycle `<folder>`: the file `stages.md` of the
copy lacks the field `<field>``. The fields are: the columns `#`, `Stage`, `Start`, `Waiting for tools`,
`Model`, `Input`, `Cached input` and `Output` of the table of the newer form's section, and that
table itself, which a heading with no table misses (the column `Files named` is never missing: a
section without it is the earlier form of the section; the columns `Cache write (5 minutes)` and
`Cache write (1 hour)` are a pair, never missing when neither stands, and where one stands the
other is the field missing); the columns `Input`, `Cached input` and
`Output` of the older form's table, `Model` being its sign; the section and the table both, where
the file has neither the heading nor a table beginning with `Model`; and, where the file has one of
the lines `- Working time without waiting for tools:` and `- Waiting for tools:`, the other (a file
with neither is an earlier form, read with both times unknown and no error). Every field of
`stages.md` is under this check, since this reading of the file is reworked. Where every field
stands in a table but in another order, or another column stands beside them, none is missing: the
table is refused with a reason, as before. The records, the `stages.md` files and the locations
file are untrusted input:
their text reaches the result only as a commit, a number or a time it was read as, and a folder,
a key or a name in a reason on one line, cut to 200 characters, with each control character and
each bar written as `\\x..`, so that no cell of a table holds a bar; a bar and the text `\\x7c`
then read alike. No path written in them is followed, and nothing of them is run. A commit dated
outside the years the platform reads gives *Committed* `unknown`. Git runs only to read, with no
`GIT_` variable of the environment it is started in and no signature shown: `rev-parse`, `log`,
`diff`, `diff-tree`, `ls-tree`, `cat-file` and `merge-base`.

A cycle of the-way whose own change changes a tool that wrote a file of its copy gives the values
that tool wrote as `unknown`, with the reason that the cycle changed the tool that wrote them, and
its other values as they stand, under the version it ran on (WAY-339). The tools are those that
start the series of what they measure: `task-cycle/cycle_stages.py` for the times, the cost and the
share of the cost in fix rounds, read from `stages.md`; `task-cycle/cycle_measures.py` for
`mechanism_measures.md`; `task-cycle/gate_times.py` and `gate/run_tests.py` for `gate_times.md`. The
cycle changed a tool where its files differ between the version it ran on and the commit of the last
copy of its record in the-way's own history (`git diff --quiet`; exit 1, or any other failure,
counts as changed). Only a cycle of `the-way` is read so: the change of a cycle of another
repository lies in that repository, which holds none of these tools. A copy that holds no such file
is of an earlier form and a cycle whose version does not resolve has none to compare, so neither is
put in doubt. The file of a changed tool is not read for the cycle, so no field of it is missing,
and the number of fix rounds, which the record gives, stands.

The two other files of a copy are read in the form their scripts write, `mechanism_measures.md` by
`task-cycle/cycle_measures.py` (WAY-339) and `gate_times.md` by `task-cycle/gate_times.py`.
A copy that holds neither is of an earlier cycle or of one whose script failed, and a copy
with no `gate_times.md` may also be of a cycle whose final gate ran in CI (WAY-160), and the
record's *Verification* says which: their values are `unknown`, with that reason, and no error. `mechanism_measures.md` is read by the cycle-level lines it opens with, each
by its label; a label it lacks is a missing field, and then every value of the file is `unknown`. A
label written twice, a value that is not what its label gives and a value `unknown` are `unknown`
with a reason, and the count goes on. `gate_times.md` is read from its table of runs: the table
itself and each of its columns `Started (UTC)`, `Exit code`, `Total seconds`, `Other gate runs at
the same time`, `Directory` and `Directory seconds` are fields, and a file lacking one gives no
runs and is a missing field. A row of the table is a run, its consecutive rows of the same four
first cells being the directories of that run; a row of the wrong number of cells is a run of its
own with every value `unknown`, and a cell of the form its column does not give is `unknown` with a
reason. At most 500 runs of a file, 50 directories of a run and 200 characters of a directory are
read, and a row after a line that is no row of the table is not read; each says so in *Unknown
values*. Both are under the check of WAY-344, since their reading is new, and they end the run
with exit 1 and an `Error:` line that names the file and the field, as `stages.md` does.

The register of problems is read as untrusted input, in the form `process-audit/problem_register.md`
gives: five tables, *Classes*, *Weights*, *Costs of an occurrence*, *Issues* and *Problems*, found
by their headings and header rows. A heading, a table or a column of a header row the register lacks
is a missing field (WAY-344): the run ends with exit 2, nothing written, and the `Error:` line names
every field missing, never reading its absence as an empty value. Where every column stands in the
header row but not in the template's order, or another stands beside them, or a heading is written
twice, no field is missing: the table is refused. A row that does not read, an unknown class,
weight or cost of an occurrence, an issue in no row of *Issues*, a doubled name, a *Fix* that is no
commit or a date that is no date refuses that row or table with a reason. A table of *Weights* or of
*Costs of an occurrence* that does not name each of its levels once is refused: its `Error:` line of
the register on stderr names the level it lacks or writes twice, and the command gives exit 1. A
refused row of *Problems* still belongs to the
cycle and the issue it names: each count of that cycle or issue reads `at least n`, as the row is
not in it. What else depends on a refused row or table is `unknown`. A problem whose cycle no named
repository holds is `unknown`, not dropped, and so is a
problem whose *Record* is a commit that adds the records of more than one cycle, whose counts then
read `at least n`. A problem is counted once, by its row; a cycle copied again after a
correction is one cycle, and its problems are counted once. *Unknown values* is described below.

For each cycle, its problems by class and weight. For each issue whose *Fate* is `fixed`, its
problems in the cycles whose *Process pin* holds the fix, and apart those in the cycles whose pin
does not hold it, never by date: the holding is `git merge-base --is-ancestor <fix> <pin>` in the
checkout of the-way (the entry `repository` under `the-way`, or this checkout), a pin written as a
short hash resolved there, and a pin or a fix that checkout lacks, an ambiguous short hash or a
pin `unknown` gives `unknown` with its reason. For each issue whose *Fate* is `open`, the
number of cycles its problems came back in, and the days it has waited: the cycles in which a
problem of the issue stands, except the first of them, so `0` where it stands in one cycle only,
and `at least n` where a refused row or a problem of a cycle not read may belong to a cycle not
counted; and from the earliest commit date of the copies its problems' *Record* names to the day
of the run, `unknown` where a problem's cycle is not known. An issue `dropped` is counted apart,
with no waiting. The issues are listed in the order of the
register, never ranked by their counts. For each issue, whatever its fate, how many of its
problems stand on each of the five levels of the cost of an occurrence: a cost
counted by the issue and never by the cycle, and a different thing from the cost of a cycle in
money, which the section *Cost* gives (WAY-337). A level counts the issue's problems by their rows,
whether or not their cycles are read.

The result is Markdown in UTF-8 with LF line ends, the same bytes for the same input, written to
`count-<YYYY-MM-DD>.md`, the date of the run, and `count-latest.md` in the directory of
`audit_results`, never inside a repository it reads or the checkout of the-way, read or not:
a section *Repositories*, a table of each
repository read and its cycles; a section *Cycles*, a table of one row per cycle; and a section
*Unknown values*, a table of every value the count did not establish, one line for each field and
reason: how many values the pair has and its first three examples, each as repository, record and
value, where a name or number of one value (a row's number, an issue's name, a version's commit) is
no part of the field. The result keeps no more of a pair, and no option of the count lists the rest.
The full list of a pair's values stands where they are read: the register's own values (its refused
rows and the problems of a cycle it names) in the register, and the cycles' values in the copies of
the cycles' records in the history of git. The values about an issue or a version are made by the
count from the register and from those copies, and have no list of their own. A section *Cost*, a
table of one row per cycle with its price list's date (the series the cost belongs to), its cost in
USD, its number of fix rounds and the share of the cost in them. A section *Mechanism measures*, a
table of one row per cycle with its measures, and a section *Gate runs*, a table of one row per run
of its gate times; the section *Measure versions* gives them per version. The sections *Problems by
cycle*, *Fixed
issues*, *Open issues*, *Dropped issues* and *Cost of an occurrence by issue* give the register's
counts, and sit before *Unknown values*. On stdout it names the two files and the counts.

Exit code: 0 with the result written; 1 with the result written but a repository that could not be
read, a table of the register refused as a whole, or a field missing in a `stages.md`, a
`mechanism_measures.md` or a `gate_times.md`, named in the
result and in an `Error:` line on stderr, which for a table of levels of the register names the
level it lacks or writes twice; 2 with `Error: <message>` on stderr and nothing written,
when an argument is wrong, the locations file, the price list, the register or an entry it needs is
missing or wrong, the register lacks a heading, a table or a column it needs, the register is
larger than 4 MiB or not UTF-8, the result directory lies inside a repository to read or the
checkout of the-way, or the result cannot be written.

Standard library only.
"""

from __future__ import annotations

import argparse
import bisect
import json
import os
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path

sys.dont_write_bytecode = True
from stage_pricing import (  # noqa: E402  the price of a stage's rows, in the directory of this file
    NO_MODEL, TEXT_CAP, UNKNOWN, ModelPrice, Prices, StageTokens, is_orchestrator_row, priced,
    priced_older)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-cycle"))
import remarks_check  # noqa: E402  the cutting of a record's lines, shared with its check
from record_items import (  # noqa: E402  the reading of the items of a record
    ITEM_DISCARDED, header_field, is_report_file, item_count_reason, item_texts, item_words,
    read_contradiction, reads_none_first, review_rounds)

display = remarks_check.display

DEFAULT_LOCATIONS = "~/.the-way/locations.json"
THE_WAY = "the-way"
REGISTER_ENTRY = "problem_register"
RESULTS_ENTRY = "audit_results"
REPOSITORY_ENTRY = "repository"
# The checkout of the-way this script lies in, used where `the-way` has no entry `repository`.
OWN_CHECKOUT = Path(__file__).resolve().parent.parent
# The price list of this part, read as a file of the-way (`--prices` names another one).
PRICES = Path(__file__).resolve().parent / "price_list.md"

RECORDS = "docs/task-cycles/"
RECORD_PATHSPEC = ":(glob)docs/task-cycles/*/cycle.md"
LATEST = "count-latest.md"
# A copy's file larger than this is not read: no record or `stages.md` comes near it.
MAX_BYTES = 4 * 1024 * 1024
GIT_TIMEOUT = 120

# A commit as a record writes it: 7 to 40 hexadecimal characters, a digit among them, so that an
# English word written in the letters a-f is not taken for one, standing apart from other letters
# and digits.
COMMIT = r"(?<![0-9A-Za-z])(?=[0-9a-fA-F]*[0-9])[0-9a-fA-F]{7,40}(?![0-9A-Za-z])"
COMMIT_IN_TEXT = re.compile(COMMIT)
MOVED_PIN = re.compile(r"moved to `?(" + COMMIT + r")`?", re.I)
REMARKS_OPENER = re.compile(r"(?P<indent>[ \t]*)[-*+][ \t]+Process remarks on the-way(?![\w-])"
                            r"[ \t]*:?[ \t]*(?P<rest>.*)")
DURATION = re.compile(r"(\d{1,7}):([0-5]\d):([0-5]\d)")
WORKING_LINE = "- Working time without waiting for tools:"
WAITING_LINE = "- Waiting for tools:"
SECTION_TITLE = "Stages: start, waiting for tools and tokens by model"
STAGES_HEADING = "## " + SECTION_TITLE
STAGE_COLUMNS = ["#", "Stage", "Start", "Waiting for tools", "Model", "Input", "Cached input",
                 "Output"]
FILES_COLUMN = "Files named"
# The two columns of the cache writes of each lifetime, a pair that follows *Files named* in the
# newest form of the section and is never missing when neither stands (WAY-344).
WRITE_5M_COLUMN = "Cache write (5 minutes)"
WRITE_1H_COLUMN = "Cache write (1 hour)"
WRITE_COLUMNS = [WRITE_5M_COLUMN, WRITE_1H_COLUMN]
# The three forms of the header of the section, each a prefix of the next.
SECTION_FORMS = (STAGE_COLUMNS, STAGE_COLUMNS + [FILES_COLUMN],
                 STAGE_COLUMNS + [FILES_COLUMN] + WRITE_COLUMNS)
# The table of tokens by model, which every form of `stages.md` has and the older form is read
# from: the table whose header row begins with `Model`.
MODEL_COLUMN = "Model"
OLDER_COLUMNS = [MODEL_COLUMN, "Total tokens", "Input", "Cached input", "Output"]
OLDER_NEEDED = ("Input", "Cached input", "Output")
# The fields of `stages.md` a form needs, as an `Error:` line names them (WAY-344): no backtick
# stands in a name, since the line writes the name between backticks.
FIELD_SECTION = f"section {SECTION_TITLE}"
FIELD_SECTION_TABLE = f"table of the section {SECTION_TITLE}"
FIELD_OLDER_TABLE = f"table with the first cell {MODEL_COLUMN}"
OLDER_NO_TURNS = ("`stages.md` is of the older form, whose table of tokens by model gives no turns, "
                  "so no round is tied to the turns that served it")
# A findings file is told by the word in its name, as the check of process remarks tells it
# (WAY-294); used only to find a turn given a findings file the record does not name.
FINDINGS_WORD = "findings"
PRICE_HEADING = "List date"
PRICE_MODEL = "Model id in stages.md"
PRICE_COLUMNS = ("Input", "Cached input", "Output", WRITE_5M_COLUMN, WRITE_1H_COLUMN)
# A token count longer than this is not a count of tokens: no model's input comes near it.
TOKEN_DIGITS = 15
PRICE = re.compile(r"[0-9]{1,6}(?:\.[0-9]{1,6})?")
TURN_SUFFIX = re.compile(r" — turn [0-9]{1,6}$")
MONEY = Decimal("0.000001")
SHARE = Decimal("0.1")
# A cost at or above this many dollars is not given: a crafted count would otherwise overrun the
# precision the cost is written with.
COST_CEILING = Decimal(10) ** 18
# The script that measures the cost, and no other: a change of it between two versions starts a
# series of the cost (and so of the count of remarks), with a new price list (WAY-339).
COST_SCRIPT = "task-cycle/cycle_stages.py"
COST_SCRIPTS = (COST_SCRIPT,)
# The files of the-way that give the form of a stage report and the instructions of the reviewer: a
# change of any of them between two versions starts a series of the count of remarks and none of the
# cost. The type of agent `the-way-stage.md` is here because the reviewer receives its text as its
# instruction.
COUNT_PATHS = ("task-cycle/change", "task-cycle/plan", "task-cycle/review", "task-cycle/spec",
               "task-cycle/agent-types/the-way-stage.md")
# The items of the record the questions of a process version read (task-cycle/record_template.md).
ITEM_PLAN = "Plan"
ITEM_TOO_LARGE = "Slices returned too large"
SLICES_WORD = re.compile(r"slices", re.I)
# The count of slices written just before the word, as `8 slices`: a figure standing alone, no
# letter or digit before it, so `F1a` and `F1–F4` give none. Every repetition is bounded.
SLICES_COUNT = re.compile(r"(?<![A-Za-z0-9])([0-9]{1,6})[ \t]{1,8}slices(?![A-Za-z0-9])", re.I)
# The locations file and the price list are named by their options in an error, never by their
# path, which is the user's (WAY-320).
LOCATIONS_LABEL = "the locations file (`--locations`)"
PRICES_LABEL = "the price list (`--prices`)"
# *Unknown values* gives every value the count did not establish one line for each field and
# reason: the number of values of the pair and its first EXAMPLES values, each as its repository,
# record and value, and the field is the value with the number of its row, the name of its issue
# and the commit of its version taken out (WAY-330).
EXAMPLES = 3
ROW_NUMBER = re.compile(r"^row [0-9]+ of ")
ISSUE_VALUE = re.compile(r"^(the fix|waiting) of issue `.*`$")
VERSION_SUFFIX = re.compile(r"\bversion \S+$")
UNKNOWN_HEADER = ["Field", "Values", "Why", "First examples"]
# The two files of a cycle's record that the count reads (WAY-339), each written by its
# script: `mechanism_measures.md` by task-cycle/cycle_measures.py, `gate_times.md` by
# task-cycle/gate_times.py. A copy that holds neither is of an earlier cycle or of one whose script
# failed; the causes are named in ABSENCE_CAUSES below.
MEASURES_FILE = "mechanism_measures.md"
GATE_FILE = "gate_times.md"
# The causes of a copy's lacking the file of a script. `gate_times.md` is written only by a gate
# run on the cycle's own system, so a cycle whose final gate ran in CI may hold none (WAY-160).
ABSENCE_CAUSES = {MEASURES_FILE: "an earlier cycle, or a script that failed",
                  GATE_FILE: "an earlier cycle, a final gate that ran in CI, or a script that failed"}
MEASURE_LABELS = (
    "Calls in all", "Calls of the orchestrator", "Calls of subagents", "Mean context per call",
    "Mean context per call of the orchestrator",
    "Share of the context in calls above 200000 tokens",
    "Context of the orchestrator's first call", "Context of the orchestrator's middle call",
    "Context of the orchestrator's last call", "Cache written, 5 minutes", "Cache written, 1 hour",
    "Cache written again by the orchestrator", "Calls of the orchestrator with a cache write again",
    "Cache written again by subagents", "Calls of subagents with a cache write again",
)
SHARE_LABEL = "Share of the context in calls above 200000 tokens"
MEASURE_WHOLE = re.compile(r"[0-9]{1,15}")
MEASURE_SHARE = re.compile(r"([0-9]{1,3}\.[0-9])%")
GATE_COLUMNS = ["Started (UTC)", "Exit code", "Total seconds", "Other gate runs at the same time",
                "Directory", "Directory seconds"]
GATE_RUN_COLUMNS = GATE_COLUMNS[:4]
GATE_TABLE_FIELD = "table of the runs"
GATE_STARTED = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}")
GATE_CODE = re.compile(r"[0-9]{1,10}")
GATE_TOTAL = re.compile(r"[0-9]{1,9}\.[0-9]{3}")
GATE_OTHERS = re.compile(r"[0-9]{1,6}")
GATE_SECONDS = re.compile(r"[0-9]{1,9}(?:\.[0-9]{1,9})?")
# The runs and the directories of one run read from `gate_times.md`, the rest not read and said so.
MAX_RUNS = 500
MAX_DIRECTORIES = 50
GATE_NONE = "—"
DIRECTORY_SEPARATOR = " · "
# The instruments that start a series of the measures they give (WAY-339): a change of the one
# starts a series of the mechanism measures, a change of one of the gate's scripts a series of the
# gate times, and nothing else does. The test runner of the gate is one of them: its output gives
# the time of each directory. The measures of a gate time are the total and each directory (WAY-350).
MEASURES_SCRIPT = "task-cycle/cycle_measures.py"
GATE_SCRIPT = "task-cycle/gate_times.py"
GATE_TEST_RUNNER = "gate/run_tests.py"
GATE_SCRIPTS = (GATE_SCRIPT, GATE_TEST_RUNNER)
TOTAL_MEASURE = "Total time of the run"
DIRECTORY_MEASURE = "Directory: "
# The three groups of tools that write the files of a cycle's copy, each as the file and the paths
# of the tools that wrote it: the paths are those that start the series of what they measure
# (COST_SCRIPTS, MEASURES_SCRIPT and GATE_SCRIPTS above), not a second list. A cycle of the-way
# whose own change changes one of them gives the values of that file as unknown (WAY-339).
STAGES_FILE = "stages.md"
WORKING_NAME = "Working time without waiting for tools"
WAITING_NAME = "Waiting for tools"
STAGES_VALUES = (WORKING_NAME, WAITING_NAME, "Cost", "Fix rounds share")
TOOL_GROUPS = ((STAGES_FILE, COST_SCRIPTS), (MEASURES_FILE, (MEASURES_SCRIPT,)),
               (GATE_FILE, GATE_SCRIPTS))


class AuditCountError(Exception):
    """A wrong argument, a missing or wrong entry of the locations file, or a result that cannot
    be written: nothing is written."""


class GitError(Exception):
    pass


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # type: ignore[override]
        raise AuditCountError(message)


# The locations file


def read_locations(name: str) -> dict:
    """The locations file as a JSON object; a key or an entry written twice is an error, since
    JSON readers disagree on which of the two counts."""
    path = Path(name).expanduser()
    label = LOCATIONS_LABEL
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        raise AuditCountError(f"{label} does not exist") from None
    except OSError as error:
        raise AuditCountError(f"cannot read {label}: {display(error.strerror or error)}") from None
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise AuditCountError(f"{label} is not UTF-8") from None

    def unique(pairs: list[tuple[str, object]]) -> dict:
        seen: dict[str, object] = {}
        for key, value in pairs:
            if key in seen:
                raise AuditCountError(f"{label} holds the key or entry "
                                      f"`{display(key[:TEXT_CAP])}` twice in one object")
            seen[key] = value
        return seen

    try:
        data = json.loads(text, object_pairs_hook=unique)
    except json.JSONDecodeError as error:
        raise AuditCountError(f"{label} is not JSON: line {error.lineno}, column "
                              f"{error.colno}") from None
    except ValueError:
        # A number of more digits than Python converts is no JSONDecodeError.
        raise AuditCountError(f"{label} is not JSON: it holds a number too long to read") from None
    except RecursionError:
        raise AuditCountError(f"{label} is nested too deeply") from None
    if not isinstance(data, dict):
        raise AuditCountError(f"{label} is not a JSON object")
    return data


def key_object(locations: dict, key: str) -> dict:
    if key not in locations:
        raise AuditCountError(f"the locations file holds no key `{display(key)}`")
    value = locations[key]
    if not isinstance(value, dict):
        raise AuditCountError(f"the key `{display(key)}` of the locations file is not a JSON "
                              f"object")
    return value


def entry_path(locations: dict, key: str, entry: str, kind: str) -> Path:
    """The path the entry `entry` under `key` holds, which must exist as a `kind`: "file" or
    "directory". The path itself is never printed: an error names the entry (WAY-320)."""
    where = f"the entry `{display(entry)}` under `{display(key)}`"
    entries = key_object(locations, key)
    if entry not in entries:
        raise AuditCountError(f"the locations file holds no entry `{display(entry)}` under "
                              f"`{display(key)}`")
    value = entries[entry]
    if not isinstance(value, str) or not value.strip():
        raise AuditCountError(f"{where} of the locations file is not a path written as a string")
    try:
        path = Path(value).expanduser()
        if not path.is_absolute():
            raise AuditCountError(f"{where} of the locations file is not an absolute path or a "
                                  f"path from `~`")
        exists = path.is_dir() if kind == "directory" else path.is_file()
    except (OSError, ValueError, RuntimeError):
        exists = False
    if not exists:
        raise AuditCountError(f"the path of {where} of the locations file is no existing {kind}")
    return path


def the_way_checkout(locations: dict) -> Path:
    """The checkout of the-way: the entry `repository` under `the-way`, or this script's own."""
    if REPOSITORY_ENTRY in key_object(locations, THE_WAY):
        return entry_path(locations, THE_WAY, REPOSITORY_ENTRY, "directory")
    return OWN_CHECKOUT


def repositories(locations: dict, named: list[str]) -> dict[str, Path]:
    """The repositories to read, by key, in the order of their keys."""
    found: dict[str, Path] = {}
    if named:
        for key in dict.fromkeys(named):
            if key == THE_WAY:
                found[key] = the_way_checkout(locations)
            else:
                found[key] = entry_path(locations, key, REPOSITORY_ENTRY, "directory")
    else:
        for key in locations:
            if REPOSITORY_ENTRY in key_object(locations, key):
                found[key] = entry_path(locations, key, REPOSITORY_ENTRY, "directory")
    if not found:
        raise AuditCountError("no key of the locations file holds an entry `repository`; add one "
                              "or name a repository with --repository")
    return dict(sorted(found.items()))


def inside(path: Path, folder: Path) -> bool:
    child = os.path.normcase(os.path.abspath(os.path.realpath(path)))
    parent = os.path.normcase(os.path.abspath(os.path.realpath(folder)))
    return child == parent or child.startswith(parent.rstrip(os.sep) + os.sep)


# Git


class Git:
    """Git run to read only, with no prompt, no pager and nothing on stdin."""

    def __init__(self, repository: Path):
        self.repository = repository

    def execute(self, arguments: tuple[str, ...]) -> subprocess.CompletedProcess:
        # A `GIT_` variable of the environment the command starts in, such as GIT_DIR set by a
        # hook, would point git at another repository or add configuration: none is passed on.
        environment = {name: value for name, value in os.environ.items()
                       if not name.upper().startswith("GIT_")}
        environment.update(GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never",
                           GIT_OPTIONAL_LOCKS="0")
        try:
            return subprocess.run(
                ["git", "--no-pager", "-c", "core.fsmonitor=false", "-c", "log.showSignature=false",
                 "-C", str(self.repository), *arguments], stdin=subprocess.DEVNULL,
                capture_output=True,
                timeout=GIT_TIMEOUT, env=environment)
        except (OSError, subprocess.TimeoutExpired) as error:
            raise GitError(f"git {arguments[0]}: {display(error)}") from None

    def run(self, *arguments: str) -> bytes:
        result = self.execute(arguments)
        if result.returncode != 0:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise GitError(f"git {arguments[0]} failed ({result.returncode}): "
                           f"{display(detail)}")
        return result.stdout

    def code(self, *arguments: str) -> int:
        """The exit code of git run to read, for a command whose exit code is its answer."""
        return self.execute(arguments).returncode


# Reading a cycle


@dataclass
class GateRun:
    """A run of `gate_times.md` as numbers, for the medians of a version: the count of other gate
    runs at the same time, the total seconds, the seconds of each directory and the exit code, each
    None where the file gives it as unknown or in a form that is not its column's."""
    others: int | None
    total: Decimal | None
    directories: list[tuple[str, Decimal | None]] = field(default_factory=list)
    code: int | None = None  # the exit code of the run, None where the file gives it as unknown


@dataclass
class Cycle:
    repository: str
    folder: str
    record: str
    committed: str
    later: list[str] = field(default_factory=list)
    # The commit date of each copy, the first and the later ones, by its commit; `unknown` where
    # the date cannot be read.
    copies: dict[str, str] = field(default_factory=dict)
    pin: str | None = None
    remarks: int | None = None
    working: int | None = None
    waiting: int | None = None
    cost: Decimal | None = None
    rounds: int | None = None
    share: Decimal | None = None
    # The questions of the process version: Q1 as yes, no or unknown; the plan's slices, and the
    # slices returned too large, each None where unknown; and whether the plan is left out (the
    # one-author route).
    contradiction: str | None = None
    plan_left_out: bool = False
    planned: int | None = None
    too_large: int | None = None
    unknown: list[tuple[str, str]] = field(default_factory=list)
    # The fields of `stages.md` a form needs that the copy lacks, as an `Error:` line names them
    # (WAY-344): the run ends with exit code 1 where any cycle has one.
    missing: list[str] = field(default_factory=list)
    # The values of `mechanism_measures.md` by label, each as the file writes it; a label not here
    # is unknown.
    measures: dict[str, str] = field(default_factory=dict)
    # The runs of `gate_times.md`, each as the cells after the repository and the record.
    gate_runs: list[list[str]] = field(default_factory=list)
    # The same runs as numbers, one for each of `gate_runs`, in the same order (WAY-350).
    gate_timed: list[GateRun] = field(default_factory=list)
    # The fields of the two files that the copy lacks, as (file, field), for the `Error:` line.
    missing_in: list[tuple[str, str]] = field(default_factory=list)
    # The files of the copy that held a text to read (`stages.md`, `mechanism_measures.md`,
    # `gate_times.md`): a copy that holds no such file is of an earlier form and is not put in
    # doubt by a change of the tool that would write it.
    held: set[str] = field(default_factory=set)


@dataclass
class Read:
    key: str
    cycles: list[Cycle] = field(default_factory=list)
    error: str | None = None
    shallow: bool = False


def header_fields(lines: list[str], fenced: list[bool], label: str) -> list[str]:
    """The values of the record's header lines `- <label>: ...`, or `- <label> and ...: ...` as
    earlier records join two fields, before its first `## ` heading, each with the indented lines
    that continue it joined to it."""
    values: list[list[str]] = []
    collecting = False
    for line, inside_fence in zip(lines, fenced):
        if inside_fence:
            collecting = False
            continue
        if line.startswith("## "):
            break
        found = header_field(line)
        if found:
            collecting = found[0] == label or found[0].startswith(label + " and ")
            if collecting:
                values.append([found[1]])
        elif collecting and line.strip() and line[:1] in " \t":
            values[-1].append(line.strip())
        else:
            collecting = False
    return [" ".join(part for part in parts if part) for parts in values]


def process_pin(text_lines, fenced, own: bool) -> tuple[str | None, str | None]:
    """The version of the-way the record names, or None with the reason."""
    pins = header_fields(text_lines, fenced, "Process pin")
    if len(pins) > 1:
        return None, "the record holds the line `Process pin` more than once"
    if pins:
        moved = MOVED_PIN.search(pins[0])
        if moved:
            return moved.group(1).lower(), None
        found = COMMIT_IN_TEXT.search(pins[0])
        if found:
            return found.group(0).lower(), None
        if not own:
            return None, "the line `Process pin` names no commit"
    elif not own:
        return None, "the record holds no line `Process pin`"
    bases = header_fields(text_lines, fenced, "Target branch and base")
    if len(bases) != 1:
        return None, ("the line `Process pin` names no commit, and the line "
                      "`Target branch and base` is " + ("doubled" if bases else "missing"))
    found = COMMIT_IN_TEXT.search(bases[0])
    if not found:
        return None, "neither the line `Process pin` nor `Target branch and base` names a commit"
    return found.group(0).lower(), None


def remarks_count(lines: list[str], fenced: list[bool]) -> tuple[int | None, str | None]:
    """The number of entries under the item `Process remarks on the-way`, or None with the
    reason."""
    openers = [index for index, line in enumerate(lines)
               if not fenced[index] and REMARKS_OPENER.fullmatch(line)]
    if not openers:
        return None, "the record holds no item `Process remarks on the-way`: an earlier form"
    if len(openers) > 1:
        return None, "the record holds the item `Process remarks on the-way` more than once"
    start = openers[0]
    opener = REMARKS_OPENER.fullmatch(lines[start])
    base = remarks_check.indent_of(lines[start])
    markers: list[int] = []
    for line, inside_fence in zip(lines[start + 1:], fenced[start + 1:]):
        if not line.strip():
            continue
        indent = remarks_check.indent_of(line)
        if indent <= base or (not inside_fence and remarks_check.HEADING.fullmatch(line)):
            break
        if not inside_fence and remarks_check.MARKER.fullmatch(line):
            markers.append(indent)
    if markers:
        return markers.count(min(markers)), None
    if remarks_check.reads_none(opener.group("rest")):
        return 0, None
    return None, ("the item `Process remarks on the-way` holds no entries under it and does not "
                  "read `none`: an earlier form")


def stages_time(lines: list[str], fenced: list[bool], prefix: str,
                what: str) -> tuple[int | None, str | None]:
    """The seconds a line of `stages.md` gives, or None with the reason."""
    values = [line[len(prefix):].strip() for line, inside_fence in zip(lines, fenced)
              if not inside_fence and line.startswith(prefix)]
    if not values:
        return None, f"`stages.md` holds no line `{prefix[2:-1]}`: an earlier form"
    if len(values) > 1:
        return None, f"`stages.md` holds the line `{prefix[2:-1]}` more than once"
    if values[0].casefold().startswith(UNKNOWN):
        return None, f"`stages.md` gives the {what} as unknown"
    match = DURATION.fullmatch(values[0])
    if not match:
        return None, f"`stages.md` gives the {what} in a form that is not h:mm:ss"
    hours, minutes, seconds = (int(part) for part in match.groups())
    return hours * 3600 + minutes * 60 + seconds, None


def has_line(lines: list[str], fenced: list[bool], prefix: str) -> bool:
    """Whether a line of `stages.md` outside code fences begins with `prefix`."""
    return any(not inside and line.startswith(prefix) for line, inside in zip(lines, fenced))


def missing_line(cycle: Cycle, prefix: str) -> str:
    """Record the time line `prefix` as a field `stages.md` lacks, and give the reason."""
    name = f"line {prefix[2:-1]}"
    cycle.missing.append(name)
    return missing_reason(name)


# Tables and the price list


def table_cells(line: str) -> list[str]:
    """The cells of a table row; a backslash escapes the character after it, so that an escaped
    bar stays inside its cell. Linear in the length of the line."""
    text = line.strip()
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in text:
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
    cells.append("".join(current).strip())
    if text.startswith("|") and cells[0] == "":
        cells.pop(0)
    if text.endswith("|") and cells and cells[-1] == "":
        cells.pop()
    return cells


def is_separator(cells: list[str]) -> bool:
    return all(cell and set(cell) <= set("-:") for cell in cells)


def read_prices(name: str) -> Prices:
    """The price list, read as a file of the-way: a missing or wrong list stops the run with
    nothing written, as a wrong entry of the locations file does."""
    path = Path(name).expanduser()
    label = PRICES_LABEL
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        raise AuditCountError(f"{label} does not exist") from None
    except OSError as error:
        raise AuditCountError(f"cannot read {label}: {display(error.strerror or error)}") from None
    if len(raw) > MAX_BYTES:
        raise AuditCountError(f"{label} is larger than {MAX_BYTES} bytes")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise AuditCountError(f"{label} is not UTF-8") from None
    lines = remarks_check.split_lines(text)
    fenced = remarks_check.fenced_flags(lines)
    dates = header_fields(lines, fenced, PRICE_HEADING)
    if len(dates) != 1:
        raise AuditCountError(f"{label} "
                              + ("holds the line `List date` more than once" if dates
                                 else "holds no line `List date`"))
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", dates[0]):
        raise AuditCountError(f"the line `List date` of {label} is no date written YYYY-MM-DD")
    try:
        date.fromisoformat(dates[0])
    except ValueError:
        raise AuditCountError(f"the line `List date` of {label} is no date") from None
    table: dict[str, ModelPrice | None] = {}
    columns: list[int] | None = None
    for line, inside in zip(lines, fenced):
        if inside or not line.startswith("|"):
            columns = None
            continue
        cells = table_cells(line)
        if columns is None:
            if cells[:1] == [PRICE_MODEL]:
                lacking = [name_of for name_of in PRICE_COLUMNS if name_of not in cells]
                if lacking:
                    raise AuditCountError(f"a table of {label} lacks the column "
                                          f"{', '.join(lacking)}")
                columns = [cells.index(name_of) for name_of in PRICE_COLUMNS]
            continue
        if is_separator(cells):
            continue
        if not cells or max(columns) >= len(cells) or not cells[0]:
            raise AuditCountError(f"a row of a table of {label} has fewer cells than its header")
        model = cells[0]
        if model in table:
            raise AuditCountError(f"{label} names model `{display(model[:TEXT_CAP])}` twice")
        numbers: list[Decimal | None] = []
        for index in columns:
            if cells[index] == NO_MODEL:
                numbers.append(None)
            elif PRICE.fullmatch(cells[index]):
                numbers.append(Decimal(cells[index]))
            else:
                # A typo would otherwise leave the model unpriced, and every cycle that used it
                # would point away from the list.
                raise AuditCountError(f"a price of model `{display(model[:TEXT_CAP])}` in {label} "
                                      "is neither a number nor `—`")
        # A `—` in *Input*, *Cached input* or *Output* is a model with no price at all; one in a
        # write column leaves only that lifetime with no price.
        table[model] = None if any(number is None for number in numbers[:3]) else ModelPrice(
            numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])
    if not table:
        raise AuditCountError(f"{label} names no model")
    return Prices(dates[0], table)


def token_count(text: str) -> int | None:
    digits = text.replace(",", "")
    if digits.isascii() and digits.isdigit() and len(digits) <= TOKEN_DIGITS:
        return int(digits)
    return None


def files_cell(text: str) -> tuple[frozenset[str] | None, bool]:
    """The files a cell *Files named* gives, and whether it reads as such: empty, `unknown`, or
    files of `reports/` joined by `, `."""
    if not text:
        return frozenset(), True
    if text == UNKNOWN:
        return None, True
    files = [part.strip() for part in text.split(",")]
    if not all(is_report_file(path) for path in files):
        return None, False
    return frozenset(files), True


@dataclass
class StageTable:
    """What `stages.md` gives for its cost, in the form its own signs name (WAY-337): the
    rows of the section of the newer form, or of the table of tokens by model of the older form
    (`older`); `named` is whether the section's table has the column *Files named*. `rows` is None
    with the `reason` where they cannot be read; `missing` holds the fields the form needs that the
    file lacks (WAY-344), which are no refusal of the form but a field not found."""
    rows: list[StageTokens] | None = None
    named: bool = False
    older: bool = False
    reason: str | None = None
    missing: list[str] = field(default_factory=list)


def missing_columns(found: list[str], needed, where: str) -> list[str]:
    """The fields that name each column of `needed` that the header row `found` lacks, in the
    order of `needed`."""
    return [f"column {name} of the table {where}" for name in needed if name not in found]


def stage_table(lines: list[str], fenced: list[bool]) -> StageTable:
    """The rows `stages.md` gives for the cost. The newer form is known by the heading of its
    section, and is read from the table of that section; without the heading the file is of the
    older form, read from its table of tokens by model. A file with neither lacks the section and
    the table (WAY-344)."""
    headings = [index for index, (line, inside) in enumerate(zip(lines, fenced))
                if not inside and line.strip() == STAGES_HEADING]
    if len(headings) > 1:
        return StageTable(reason="`stages.md` holds that section more than once")
    if headings:
        return section_table(lines, fenced, headings[0])
    return older_table(lines, fenced)


def section_table(lines: list[str], fenced: list[bool], heading: int) -> StageTable:
    """The newer form: the rows of the table under the heading of the section. A heading with no
    table, or a table whose header row lacks one of the columns the form needs, is a field missing;
    the column *Files named* is never one: a section without it is the earlier form of the
    section. The two columns of the cache writes are a pair: with neither the table is of an earlier
    form, and with one the other is a field missing."""
    table: list[list[str]] = []
    for line, inside in zip(lines[heading + 1:], fenced[heading + 1:]):
        if inside:
            continue
        if line.startswith("#"):
            break
        if line.startswith("|"):
            table.append(table_cells(line))
    if not table:
        return StageTable(reason="the section in `stages.md` holds no table",
                          missing=[FIELD_SECTION_TABLE])
    where = f"of the section {SECTION_TITLE}"
    absent = missing_columns(table[0], STAGE_COLUMNS, where)
    written = [name for name in WRITE_COLUMNS if name in table[0]]
    if len(written) == 1:
        absent += missing_columns(table[0], [name for name in WRITE_COLUMNS if name not in written],
                                  where)
    if absent:
        return StageTable(reason="the table of the section in `stages.md` lacks a column",
                          missing=absent)
    if table[0] not in SECTION_FORMS:
        return StageTable(reason=("the table of the section in `stages.md` is not of the form the "
                                  "stage report gives"))
    named = len(table[0]) > len(STAGE_COLUMNS)
    writes = len(table[0]) > len(STAGE_COLUMNS) + 1
    columns = len(table[0])
    body = [cells for cells in table[1:] if not is_separator(cells)]
    if not body:
        return StageTable(reason="the section in `stages.md` holds no stage row")
    rows: list[StageTokens] = []
    for cells in body:
        if len(cells) != columns:
            return StageTable(reason=(f"a row of the section in `stages.md` has {len(cells)} "
                                      f"cells, not {columns}"))
        counts = [token_count(cells[index]) for index in (5, 6, 7)]
        if writes:
            counts += [token_count(cells[index]) for index in (9, 10)]
        if any(count is None for count in counts):
            return StageTable(reason=("a token count in the section of `stages.md` is not a number "
                                      f"of at most {TOKEN_DIGITS} digits"))
        row = StageTokens(cells[0], cells[1], cells[4], *counts[:3])
        if writes:
            row.write_5m, row.write_1h = counts[3], counts[4]
        if named:
            row.files, row.files_read = files_cell(cells[8])
        rows.append(row)
    return StageTable(rows=rows, named=named)


def older_table(lines: list[str], fenced: list[bool]) -> StageTable:
    """The older form: the rows of the table of tokens by model, the one table of `stages.md`
    whose header row begins with `Model`, found exactly once. Without it the file lacks the section
    and the table; written twice, no row is chosen and the cost is unknown with no field missing;
    a header row without one of the columns the cost needs is a field missing, and in another
    order, or with another column beside them, none is and the table is refused."""
    starts = [index for index, (line, inside) in enumerate(zip(lines, fenced))
              if not inside and line.startswith("|") and table_cells(line)[:1] == [MODEL_COLUMN]
              and (index == 0 or fenced[index - 1] or not lines[index - 1].startswith("|"))]
    if not starts:
        return StageTable(reason=("`stages.md` holds neither the section `" + SECTION_TITLE
                                  + "` nor a table of tokens by model"),
                          missing=[FIELD_SECTION, FIELD_OLDER_TABLE])
    if len(starts) > 1:
        return StageTable(reason="`stages.md` holds the table of tokens by model more than once")
    start = starts[0]
    header = table_cells(lines[start])
    absent = missing_columns(header, OLDER_NEEDED, f"with the first cell {MODEL_COLUMN}")
    if absent:
        return StageTable(reason="the table of tokens by model in `stages.md` lacks a column",
                          missing=absent)
    form = "the table of tokens by model in `stages.md` is not of the form the stage report gives"
    if header != OLDER_COLUMNS:
        return StageTable(reason=form)
    if (start + 1 >= len(lines) or fenced[start + 1] or not lines[start + 1].startswith("|")
            or not is_separator(table_cells(lines[start + 1]))):
        return StageTable(reason=form)
    body: list[list[str]] = []
    for index in range(start + 2, len(lines)):
        if fenced[index] or not lines[index].startswith("|"):
            break
        body.append(table_cells(lines[index]))
    if not body:
        return StageTable(reason="the table of tokens by model in `stages.md` holds no model row")
    rows: list[StageTokens] = []
    for number, cells in enumerate(body, 1):
        if len(cells) != len(OLDER_COLUMNS):
            return StageTable(reason=(f"a row of the table of tokens by model in `stages.md` has "
                                      f"{len(cells)} cells, not {len(OLDER_COLUMNS)}"))
        counts = [token_count(cells[index]) for index in range(1, len(OLDER_COLUMNS))]
        if any(count is None for count in counts):
            return StageTable(reason=("a token count in the table of tokens by model in "
                                      f"`stages.md` is not a number of at most {TOKEN_DIGITS} "
                                      "digits"))
        rows.append(StageTokens(str(number), cells[0], cells[0], counts[1], counts[2], counts[3]))
    return StageTable(rows=rows, older=True)


def read_plan(lines: list[str], fenced: list[bool]) -> tuple[bool, int | None, str | None]:
    """The item *Plan* of a record: whether the plan is left out (the one-author route), the
    slices it made, or None with the reason. The count is the figure written just before the word
    `slices`, as in `8 slices`; with no such figure or with more than one, the count is not
    read."""
    items = item_texts(lines, fenced, ITEM_PLAN)
    if len(items) != 1:
        return False, None, item_count_reason(ITEM_PLAN, items)
    text = item_words(items[0][0], items[0][1])
    if reads_none_first(text):
        return True, None, None
    if SLICES_WORD.search(text) is None:
        return False, None, "the item `Plan` names no count of slices"
    figures = SLICES_COUNT.findall(text)
    if len(figures) != 1:
        return False, None, ("the item `Plan` does not give one count of slices before the word "
                             "`slices`")
    return False, int(figures[0]), None


def read_too_large(lines: list[str], fenced: list[bool]) -> tuple[int | None, str | None]:
    """The item *Slices returned too large*: 0 where it reads `none`, the number of its entries
    where it lists them, or None with the reason."""
    items = item_texts(lines, fenced, ITEM_TOO_LARGE)
    if len(items) != 1:
        return None, item_count_reason(ITEM_TOO_LARGE, items)
    rest, below = items[0]
    if reads_none_first(rest) and not any(text.strip() for text, _ in below):
        return 0, None
    markers = [remarks_check.indent_of(text) for text, inside in below
               if not inside and remarks_check.MARKER.fullmatch(text)]
    if rest.strip() or not markers:
        return None, ("the item `Slices returned too large` reads neither none nor an entry "
                      "per slice")
    base = min(markers)
    return sum(1 for indent in markers if indent == base), None


def process_questions(cycle: Cycle, lines: list[str] | None, fenced: list[bool] | None,
                      reason: str | None) -> None:
    """Read the questions of a process version from the cycle's record; a value that cannot be
    read is `unknown` with its reason, and the record missing makes all of them unknown."""
    if lines is None or fenced is None:
        cycle.unknown += [(ITEM_DISCARDED, reason), (ITEM_PLAN, reason),
                          (ITEM_TOO_LARGE, reason)]
        return
    cycle.contradiction, why = read_contradiction(lines, fenced)
    if why:
        cycle.unknown.append((ITEM_DISCARDED, why))
    cycle.plan_left_out, cycle.planned, why = read_plan(lines, fenced)
    if cycle.plan_left_out:
        return
    if why:
        cycle.unknown.append((ITEM_PLAN, why))
    cycle.too_large, why = read_too_large(lines, fenced)
    if why:
        cycle.unknown.append((ITEM_TOO_LARGE, why))
    elif cycle.planned is not None and cycle.too_large > cycle.planned:
        cycle.too_large = None
        cycle.unknown.append((ITEM_TOO_LARGE,
                              "more slices are returned too large than the plan made"))


def missing_reason(name: str, file: str = "stages.md") -> str:
    return f"the file `{file}` of the copy lacks the field `{name}`"


def add_cost(cycle: Cycle, record_lines: list[str] | None, record_fenced: list[bool] | None,
             record_reason: str | None, stages_lines: list[str], stages_fenced: list[bool],
             prices: Prices) -> None:
    """The cycle's cost at the list's prices and the share of its fix rounds in it; a value that
    cannot be given is `unknown` with its reason, never zero. A field the form of `stages.md` needs
    and the file lacks is also put on the cycle's `missing`, for the `Error:` line (WAY-344)."""
    table = stage_table(stages_lines, stages_fenced)
    if table.rows is None:
        if table.missing:
            for name in table.missing:
                cycle.missing.append(name)
                cycle.unknown += [("Cost", missing_reason(name)),
                                  ("Fix rounds share", missing_reason(name))]
        else:
            cycle.unknown += [("Cost", table.reason), ("Fix rounds share", table.reason)]
        return
    costs, reason = (priced_older if table.older else priced)(table.rows, prices)
    if costs is None:
        cycle.unknown += [("Cost", reason), ("Fix rounds share", reason)]
        return
    total = sum(costs, Decimal(0))
    if total >= COST_CEILING:
        cycle.unknown += [("Cost", "the cost is at or above the command's limit of 10^18 USD"),
                          ("Fix rounds share", "the cost is at or above the command's limit")]
        return
    cycle.cost = total
    if table.older:
        # The table of tokens by model ties no round to the turns that served it: the share is
        # unknown, but the number of rounds stands in the record.
        cycle.unknown.append(("Fix rounds share", OLDER_NO_TURNS))
    if record_lines is None:
        cycle.unknown.append(("Fix rounds share", record_reason))
        return
    findings, reason = review_rounds(record_lines, record_fenced)
    if findings is None:
        cycle.unknown.append(("Fix rounds share", reason))
        return
    cycle.rounds = len(findings)
    if table.older:
        return
    reason = fix_rounds_share(table.rows, costs, total, table.named, findings, cycle)
    if reason:
        cycle.unknown.append(("Fix rounds share", reason))


def fix_rounds_share(rows: list[StageTokens], costs: list[Decimal], total: Decimal, named: bool,
                     findings: list[str], cycle: Cycle) -> str | None:
    """Set the share of the cost spent in the fix rounds whose findings files the record names:
    the cost of the subagent turns given one of those files, each turn once, over the cycle's
    cost (WAY-337). Returns the reason where it cannot be given."""
    if not named:
        return f"`stages.md` has no column `{FILES_COLUMN}`: an earlier form"
    if total == 0:
        return "the stages hold no tokens"
    turns: dict[str, tuple[frozenset[str] | None, Decimal]] = {}
    names: dict[str, str] = {}
    for row, cost in zip(rows, costs):
        if is_orchestrator_row(row.name):
            continue
        if not row.files_read:
            return (f"the cell `{FILES_COLUMN}` of stage `{row.name[:TEXT_CAP]}` is not a list of "
                    "files of `reports/`")
        if row.number in turns:
            # The model rows of one turn repeat its stage and its files; rows that disagree do
            # not tell which of them the turn was given.
            files, spent = turns[row.number]
            if names[row.number] != row.name or files != row.files:
                return (f"the rows of stage number {row.number[:TEXT_CAP]} disagree in their stage "
                        f"or in their cell `{FILES_COLUMN}`")
            turns[row.number] = (files, spent + cost)
        else:
            turns[row.number] = (row.files, cost)
            names[row.number] = row.name
    given = [files for files, _ in turns.values() if files is not None]
    unread = len(turns) - len(given)
    extra = sorted({path for files in given for path in files
                    if FINDINGS_WORD in path.rsplit("/", 1)[-1]} - set(findings))
    if extra:
        return (f"{len(extra)} findings file(s) the subagent turns were given are not named by "
                f"the item `Review rounds`, which names {len(findings)}: the record and "
                "`stages.md` do not agree")
    if unread:
        # Such a turn may be a fix or the review of a fix: neither `none` nor a share without it
        # can be told.
        return (f"the message of {unread} subagent turn(s) could not be read, so whether they "
                "serve a fix round is not known")
    for path in findings:
        count = sum(1 for files in given if path in files)
        if count < 2:
            return (f"the findings file `{path}` that the item `Review rounds` names is named by "
                    f"{count} subagent turn(s), and a round has a fix and the review of that fix")
    spent = sum((cost for files, cost in turns.values()
                 if files is not None and files & set(findings)), Decimal(0))
    cycle.share = spent / total * 100
    return None


def tree_entries(git: Git, commit: str) -> dict[bytes, tuple[bytes, bytes, str, str]]:
    """Every file under docs/task-cycles/ at a commit: its mode, type, object and size."""
    raw = git.run("ls-tree", "-r", "-z", "-l", "--full-tree", commit, "--", ":(literal)" + RECORDS)
    found = {}
    for entry in raw.split(b"\0"):
        if entry:
            metadata, path = entry.split(b"\t", 1)
            mode, kind, sha, size = metadata.split()
            found[path] = (mode, kind, sha.decode("ascii"), size.decode("ascii"))
    return found


def read_file(git: Git, entries: dict, path: bytes) -> tuple[str | None, str | None]:
    """The text of a file of the copy, or None with the reason; a symbolic link or a submodule
    is not followed."""
    name = path.rsplit(b"/", 1)[-1].decode("ascii")
    if path not in entries:
        return None, f"the copy holds no `{name}`"
    mode, kind, sha, size = entries[path]
    if kind != b"blob" or not mode.startswith(b"100"):
        return None, f"`{name}` of the copy is no regular file"
    if not size.isdigit() or int(size) > MAX_BYTES:
        return None, f"`{name}` of the copy is larger than {MAX_BYTES} bytes"
    data = git.run("cat-file", "blob", sha)
    try:
        return data.decode("utf-8-sig"), None
    except UnicodeDecodeError:
        return None, f"`{name}` of the copy is not UTF-8"


def read_optional(git: Git, entries: dict, prefix: bytes,
                  name: str) -> tuple[str | None, str | None]:
    """The text of a file of the copy that an earlier form lacks, or None with the reason: the
    copy may be of an earlier cycle or of one whose script failed, and for `gate_times.md` of one
    whose final gate ran in CI."""
    path = prefix + name.encode("ascii")
    if path not in entries:
        return None, (f"the copy holds no `{name}`: {ABSENCE_CAUSES[name]} "
                      "(the record's *Verification* says which)")
    return read_file(git, entries, path)


def guarded_optional(git: Git, entries: dict, prefix: bytes,
                     name: str) -> tuple[str | None, str | None]:
    """`read_optional`, with a failure of git on this file given as its reason."""
    try:
        return read_optional(git, entries, prefix, name)
    except (GitError, ValueError, UnicodeError) as error:
        return None, f"git could not read the copy: {display(error)}"


def measure_fits(label: str, value: str) -> bool:
    """Whether a value of `mechanism_measures.md` is what its label gives: a whole number, and for
    the share a number of percent up to 100."""
    if label == SHARE_LABEL:
        found = MEASURE_SHARE.fullmatch(value)
        return found is not None and Decimal(found.group(1)) <= 100
    return MEASURE_WHOLE.fullmatch(value) is not None


def read_measures(cycle: Cycle, text: str | None, reason: str | None) -> None:
    """Read the cycle-level lines of `mechanism_measures.md` by their labels. A label the
    file lacks is a missing field: then every value of the file is unknown, and the field is named
    for the `Error:` line (WAY-344). A label written twice, a value that is not what its label gives
    or `unknown` is unknown with its reason, and the count goes on."""
    if text is None:
        cycle.unknown.append(("Mechanism measures", reason))
        return
    lines = remarks_check.split_lines(text)
    fenced = remarks_check.fenced_flags(lines)
    found = {label: header_fields(lines, fenced, label) for label in MEASURE_LABELS}
    absent = [label for label in MEASURE_LABELS if not found[label]]
    if absent:
        for label in MEASURE_LABELS:
            if label in absent:
                cycle.missing_in.append((MEASURES_FILE, label))
                cycle.unknown.append((label, missing_reason(label, MEASURES_FILE)))
            else:
                cycle.unknown.append((label, f"`{MEASURES_FILE}` lacks a field, so its values "
                                             "are unknown"))
        return
    for label in MEASURE_LABELS:
        values = found[label]
        if len(values) > 1:
            cycle.unknown.append((label, f"`{MEASURES_FILE}` holds the line `{label}` more than "
                                         "once"))
        elif values[0] == UNKNOWN:
            cycle.unknown.append((label, f"`{MEASURES_FILE}` gives it as unknown"))
        elif measure_fits(label, values[0]):
            cycle.measures[label] = values[0]
        else:
            cycle.unknown.append((label, f"`{MEASURES_FILE}` gives it in a form that is not what "
                                         "its label gives"))


def gate_value(reasons: list[tuple[str, str]], column: str, value: str, pattern: re.Pattern,
               why: str) -> str:
    """A cell of a run in `gate_times.md` as written where it has the form of its column, else
    `unknown` with the reason kept in `reasons` under the value `Gate runs: <column>`."""
    if pattern.fullmatch(value):
        return value
    reasons.append((f"Gate runs: {column}",
                    f"`{GATE_FILE}` gives it as unknown" if value == UNKNOWN else why))
    return UNKNOWN


def read_gate(cycle: Cycle, text: str | None, reason: str | None) -> None:
    """Read the runs of `gate_times.md` from its table. A table lacking one of its six
    columns, or lacking the table, is a missing field, and the runs are not read; a row of the wrong
    number of cells is a run of its own with unknown values; the runs and the directories beyond the
    limits are not read, and the reason is given."""
    if text is None:
        cycle.unknown.append(("Gate runs", reason))
        return
    lines = remarks_check.split_lines(text)
    fenced = remarks_check.fenced_flags(lines)
    header = next((index for index, (line, inside) in enumerate(zip(lines, fenced))
                   if not inside and line.startswith("|")), None)
    if header is None:
        cycle.missing_in.append((GATE_FILE, GATE_TABLE_FIELD))
        cycle.unknown.append(("Gate runs", missing_reason(GATE_TABLE_FIELD, GATE_FILE)))
        return
    names = table_cells(lines[header])
    absent = [name for name in GATE_COLUMNS if name not in names]
    if absent:
        for name in absent:
            field_name = f"column {name} of the table"
            cycle.missing_in.append((GATE_FILE, field_name))
            cycle.unknown.append(("Gate runs", missing_reason(field_name, GATE_FILE)))
        return
    at = {name: names.index(name) for name in GATE_COLUMNS}
    reasons: list[tuple[str, str]] = []
    # Each run: its four run cells, or None for a row of the wrong number of cells, and its
    # directories as (name, seconds).
    runs: list[tuple[list[str] | None, list[tuple[str, str]]]] = []
    last: list[str] | None = None
    cut_directories = False
    table_end = len(lines)
    for index in range(header + 1, len(lines)):
        if fenced[index] or not lines[index].startswith("|"):
            table_end = index
            break
        cells = table_cells(lines[index])
        if is_separator(cells):
            continue
        # A row of the wrong number of cells is a run of its own, and the limit counts it too.
        wide = len(cells) != len(names)
        key = None if wide else [cells[at[name]] for name in GATE_RUN_COLUMNS]
        if wide or last is None or key != last:
            if len(runs) >= MAX_RUNS:
                reasons.append(("Gate runs", f"`{GATE_FILE}` holds more than {MAX_RUNS} runs: the "
                                             "rest are not read"))
                break
            if wide:
                reasons.append(("Gate runs", f"a row of the table in `{GATE_FILE}` has "
                                             f"{len(cells)} cells, not {len(names)}"))
                runs.append((None, []))
                last = None
                continue
            runs.append((key, []))
            last = key
        directory, seconds = cells[at["Directory"]], cells[at["Directory seconds"]]
        if directory == GATE_NONE and seconds == GATE_NONE:
            continue
        directories = runs[-1][1]
        if len(directories) >= MAX_DIRECTORIES:
            cut_directories = True
            continue
        directories.append((directory, seconds))
    if any(not fenced[index] and lines[index].startswith("|")
           for index in range(table_end, len(lines))):
        reasons.append(("Gate runs", f"`{GATE_FILE}` holds a row after a line that is not a row of "
                                     "the table: the rows after it are not read"))
    if cut_directories:
        reasons.append(("Gate runs: Directories", f"a run in `{GATE_FILE}` lists more than "
                                                  f"{MAX_DIRECTORIES} directories: the rest are "
                                                  "not listed"))
    for key, directories in runs:
        if key is None:
            cycle.gate_runs.append([UNKNOWN] * 5)
            cycle.gate_timed.append(GateRun(None, None))
            continue
        started, code, total, others = [
            gate_value(reasons, column, value, pattern, why)
            for column, value, pattern, why in zip(
                GATE_RUN_COLUMNS, key,
                (GATE_STARTED, GATE_CODE, GATE_TOTAL, GATE_OTHERS),
                ("a start is not written YYYY-MM-DD HH:MM:SS.mmm",
                 "an exit code is not a whole number",
                 "a total is not written as seconds to three decimals",
                 "a count of other gate runs is not a whole number"))]
        listed = []
        # The numbers of the run: a directory written twice in it counts once, at its first time.
        timed = GateRun(None if others == UNKNOWN else int(others),
                        None if total == UNKNOWN else Decimal(total),
                        code=None if code == UNKNOWN else int(code))
        named: set[str] = set()
        for name, seconds in directories:
            seconds = gate_value(reasons, "Directory seconds", seconds, GATE_SECONDS,
                                 "the seconds of a directory are not a number")
            listed.append(f"{name[:TEXT_CAP]} " + (seconds if seconds == UNKNOWN
                                                   else seconds + " s"))
            if name[:TEXT_CAP] in named:
                reasons.append(("Gate runs: Directories",
                                f"a run in `{GATE_FILE}` lists a directory twice: only its first "
                                "time is counted in the medians"))
                continue
            named.add(name[:TEXT_CAP])
            timed.directories.append((name[:TEXT_CAP],
                                      None if seconds == UNKNOWN else Decimal(seconds)))
        cycle.gate_runs.append([started, code, total, others,
                                DIRECTORY_SEPARATOR.join(listed) or GATE_NONE])
        cycle.gate_timed.append(timed)
    cycle.unknown.extend(dict.fromkeys(reasons))


def fill(cycle: Cycle, git: Git, commit: str, folder: bytes, own: bool, prices: Prices) -> None:
    """Read the values of a cycle from the copy its commit holds."""
    prefix = RECORDS.encode("ascii") + folder + b"/"
    try:
        entries = tree_entries(git, commit)
        record, record_reason = read_file(git, entries, prefix + b"cycle.md")
        stages, stages_reason = read_file(git, entries, prefix + b"stages.md")
    except (GitError, ValueError, UnicodeError) as error:
        reason = f"git could not read the copy: {display(error)}"
        record = stages = None
        record_reason = stages_reason = reason
        measures = gate = (None, reason)
    else:
        # Each of the two optional files stands in a `try` of its own: a git failure on one leaves
        # the files that were read.
        measures, gate = (guarded_optional(git, entries, prefix, name)
                          for name in (MEASURES_FILE, GATE_FILE))
    record_lines = record_fenced = None
    if record is None:
        cycle.unknown += [("Process pin", record_reason), ("Remarks", record_reason)]
    else:
        record_lines = remarks_check.split_lines(record)
        record_fenced = remarks_check.fenced_flags(record_lines)
        cycle.pin, reason = process_pin(record_lines, record_fenced, own)
        if reason:
            cycle.unknown.append(("Process pin", reason))
        cycle.remarks, reason = remarks_count(record_lines, record_fenced)
        if reason:
            cycle.unknown.append(("Remarks", reason))
    process_questions(cycle, record_lines, record_fenced, record_reason)
    cycle.held = {name for name, text in ((STAGES_FILE, stages), (MEASURES_FILE, measures[0]),
                                          (GATE_FILE, gate[0])) if text is not None}
    # The two files after the record's own values, so that the rows of *Unknown values* of a
    # cycle keep their order.
    read_measures(cycle, *measures)
    read_gate(cycle, *gate)
    if stages is None:
        cycle.unknown += [(name, stages_reason) for name in STAGES_VALUES]
        return
    lines = remarks_check.split_lines(stages)
    fenced = remarks_check.fenced_flags(lines)
    # A file with one of the two time lines and not the other lacks the other (WAY-344); a file with
    # neither is an earlier form, whose two times are unknown with no field missing.
    has_working = has_line(lines, fenced, WORKING_LINE)
    has_waiting = has_line(lines, fenced, WAITING_LINE)
    cycle.working, reason = stages_time(lines, fenced, WORKING_LINE,
                                        "working time without waiting for tools")
    if has_waiting and not has_working:
        reason = missing_line(cycle, WORKING_LINE)
    if reason:
        cycle.unknown.append((WORKING_NAME, reason))
    cycle.waiting, reason = stages_time(lines, fenced, WAITING_LINE, "waiting for tools")
    if has_working and not has_waiting:
        reason = missing_line(cycle, WAITING_LINE)
    if reason:
        cycle.unknown.append((WAITING_NAME, reason))
    add_cost(cycle, record_lines, record_fenced, record_reason, lines, fenced, prices)


def committed_date(stamp: str) -> str | None:
    """The UTC date of a commit's timestamp as `git log` gives it, or None where the commit holds
    a value outside the years the platform can read: a commit's date is written by whoever made
    it, and one such commit must not end the count of every repository."""
    try:
        return datetime.fromtimestamp(int(stamp), timezone.utc).date().isoformat()
    except (OSError, OverflowError, ValueError):
        return None


def read_repository(key: str, path: Path, prices: Prices) -> Read:
    """The cycles whose records the history of one repository holds."""
    result = Read(key)
    git = Git(path)
    try:
        git.run("rev-parse", "--git-dir")
        result.shallow = git.run("rev-parse", "--is-shallow-repository").strip() == b"true"
        listed = git.run("log", "--full-history", "--branches", "--remotes", "--diff-filter=A",
                         "--no-renames", "--topo-order", "--reverse", "--format=%H %ct", "--",
                         RECORD_PATHSPEC).decode("ascii")
        copies: dict[bytes, list[tuple[str, str]]] = {}
        for line in listed.splitlines():
            commit, _, stamp = line.partition(" ")
            added = git.run("diff-tree", "--root", "--no-commit-id", "-r", "-z", "--no-renames",
                            "--diff-filter=A", "--name-only", commit, "--", RECORD_PATHSPEC)
            for name in added.split(b"\0"):
                parts = name.split(b"/")
                if len(parts) == 4 and parts[3] == b"cycle.md" and parts[2]:
                    copies.setdefault(parts[2], []).append((commit, stamp))
    except (GitError, ValueError, UnicodeError) as error:
        result.error = display(error)
        return result
    for folder, commits in copies.items():
        first, stamp = commits[0]
        committed = committed_date(stamp)
        cycle = Cycle(key, display(folder.decode("utf-8", errors="replace")), first,
                      committed or UNKNOWN, [commit for commit, _ in commits[1:]],
                      {commit: committed_date(when) or UNKNOWN for commit, when in commits})
        if committed is None:
            cycle.unknown.append(("Committed", "the commit's date lies outside the years the "
                                               "command can read"))
        fill(cycle, git, commits[-1][0], folder, key == THE_WAY, prices)
        result.cycles.append(cycle)
    result.cycles.sort(key=lambda cycle: (cycle.committed, cycle.folder, cycle.record))
    return result


# The register of problems

COSTS_TITLE = "Costs of an occurrence"
# The five tables of the register, each under its heading, with the header row the template gives.
REGISTER_TABLES = (
    ("Classes", ["Class", "Meaning", "Added", "Withdrawn"]),
    ("Weights", ["Weight", "Meaning"]),
    (COSTS_TITLE, ["Cost of an occurrence", "Meaning"]),
    ("Issues", ["Issue", "What", "Fate", "Fix"]),
    ("Problems", ["Repository", "Record", "Stages", "What", "Class", "Weight",
                  "Cost of an occurrence", "Issue"]),
)
# The scale of weight has these four levels and no other.
LEVELS = ["no problem", "Minor", "Important", "Critical"]
# The scale of the cost of an occurrence has these five levels, each dearer than the one before, and
# no other. It is a different thing from the cost of a cycle in money (WAY-337).
COST_LEVELS = ["nothing", "steps", "stage", "round", "human"]
FATES = ["open", "fixed", "dropped"]
FIXED = "fixed"
START = "start"
NONE = "none"
NAME_LENGTH = 80
# Lower-case letters and digits in words joined by single hyphens: each hyphen must stand between
# two runs of them, so the pattern takes one way through any text and cannot backtrack.
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
DATE_TEXT = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
FULL_HASH = re.compile(r"[0-9a-fA-F]{40}")
# A commit as the records write it, in lower-case hexadecimal characters only, so that no value
# given to git begins with `-`.
SHORT_HASH = re.compile(r"[0-9a-f]{7,40}")


@dataclass
class Problem:
    """A row of the table *Problems* that the checks accept."""
    number: int
    repository: str
    record: str
    cls: str
    weight: str
    cost: str
    issue: str


@dataclass
class Register:
    """What the register gives: its classes and issues in the order of their tables, the problems
    that pass the checks, and each refused row or table with its reason."""
    classes: list[str] = field(default_factory=list)
    issues: list[tuple[str, str, str]] = field(default_factory=list)
    problems: list[Problem] = field(default_factory=list)
    # The Repository, Record and Issue texts of each refused row of *Problems*, as the row gives them
    # (Issue empty where the row is too short to have one): a refused row still belongs to the cycle
    # and the issue it names, and the counts that include it say so.
    refused_problems: list[tuple[str, str, str]] = field(default_factory=list)
    refused: list[tuple[str, str, str, str]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    # The dates of *Added* and *Withdrawn* of the valid rows of *Classes*, sorted as text (they are
    # written YYYY-MM-DD); unknown where a row or the table does not read, so that a change of the
    # list cannot be ruled out.
    class_dates: list[str] = field(default_factory=list)
    class_dates_unknown: bool = False

    def refuse(self, value: str, why: str, repository: str = THE_WAY, record: str = "none") -> None:
        self.refused.append(tuple(text[:TEXT_CAP] for text in (repository, record, value, why)))


def valid_name(text: str) -> bool:
    return len(text) <= NAME_LENGTH and NAME.fullmatch(text) is not None


def valid_date(text: str) -> bool:
    if DATE_TEXT.fullmatch(text) is None:
        return False
    try:
        date.fromisoformat(text)
    except ValueError:
        return False
    return True


def check_class(cells: list[str]) -> tuple[str, str | None]:
    name = cells[0]
    if not valid_name(name) or name == NONE:
        return name, "the class name is not lower-case letters, digits and hyphens, or it is `none`"
    if cells[2] != START and not valid_date(cells[2]):
        return name, "the column Added is neither `start` nor a date written YYYY-MM-DD"
    if cells[3] != NONE and not valid_date(cells[3]):
        return name, "the column Withdrawn is neither `none` nor a date written YYYY-MM-DD"
    return name, None


def check_weight(cells: list[str]) -> tuple[str, str | None]:
    if cells[0] not in LEVELS:
        return cells[0], "the weight is not one of the four levels"
    return cells[0], None


def check_cost_level(cells: list[str]) -> tuple[str, str | None]:
    if cells[0] not in COST_LEVELS:
        return cells[0], "the cost of an occurrence is not one of the five levels"
    return cells[0], None


def check_issue(cells: list[str]) -> tuple[str, str | None]:
    name, fate, fix = cells[0], cells[2], cells[3]
    if not valid_name(name) or name == NONE:
        return name, "the issue name is not lower-case letters, digits and hyphens, or it is `none`"
    if fate not in FATES:
        return name, "the fate is not `open`, `fixed` or `dropped`"
    if fate == FIXED and FULL_HASH.fullmatch(fix) is None:
        return name, "the Fix of a fixed issue is no commit of 40 hexadecimal characters"
    if fate != FIXED and fix != NONE:
        return name, "the Fix of an issue that is not fixed must read `none`"
    return name, None


def named_rows(register: Register, title: str, rows: list[list[str]], width: int,
               check) -> list[tuple[str, int, list[str]]]:
    """The rows of one table that pass `check`, as (name, row number, cells) in table order. A row
    of the wrong width or refused by `check` is refused with its reason; a name written in two
    rows refuses both of them."""
    kept = []
    for number, cells in enumerate(rows, 1):
        value = f"row {number} of `{title}`"
        if len(cells) != width:
            register.refuse(value, f"the row has {len(cells)} cells, not {width}")
            continue
        name, why = check(cells)
        if why:
            register.refuse(value, why)
            continue
        kept.append((name, number, cells))
    count = Counter(name for name, _, _ in kept)
    valid = []
    for name, number, cells in kept:
        if count[name] > 1:
            register.refuse(f"row {number} of `{title}`", "the name is written in two rows")
        else:
            valid.append((name, number, cells))
    return valid


def level_faults(rows: list[list[str]], levels: list[str]) -> str | None:
    """What a table of levels lacks, in words the `Error:` line can name: each level that none of
    its rows of the right width names, and each written in two rows; None where each is named
    once. A row of the wrong width is refused on its own and counts for no level."""
    width = 2
    names = [cells[0] for cells in rows if len(cells) == width]
    missing = [level for level in levels if level not in names]
    doubled = [level for level in levels if names.count(level) > 1]
    parts = []
    if missing:
        parts.append("lacks " + ", ".join(f"`{level}`" for level in missing))
    if doubled:
        parts.append("writes " + ", ".join(f"`{level}`" for level in doubled) + " in two rows")
    return " and ".join(parts) or None


def check_levels(register: Register, title: str, rows: list[list[str]], levels: list[str],
                 check) -> None:
    """Refuse the rows of a table of levels that `check` refuses, and where the table does not name
    each of its levels once, add an `Error:` of the register that names the level it lacks or
    writes twice (WAY-344). The result is still written: what depends on the table is unknown."""
    named_rows(register, title, rows, 2, check)
    fault = level_faults(rows, levels)
    if fault is not None:
        why = f"the table `{title}` must name each level once: it {fault}"
        register.errors.append(why)
        register.refuse(f"table `{title}`", why)


def register_table(lines: list[str], fenced: list[bool], title: str, columns: list[str],
                   missing: list[str]) -> tuple[list[list[str]] | None, str | None]:
    """The rows of the table under the heading `## <title>`, or None with the reason. The table
    starts at the first line that begins with `|` before the next heading, and its header row must
    be `columns`; its rows run on until a line that does not begin with `|`. A heading, a table or
    a column the register lacks is a field missing (WAY-344): it is added to `missing`, in words
    that name it, as well as returned as the reason."""
    headings = [index for index, (line, inside) in enumerate(zip(lines, fenced))
                if not inside and line.strip() == f"## {title}"]
    if len(headings) != 1:
        if not headings:
            missing.append(f"the heading `## {title}`")
        return None, (f"the register holds the heading `## {title}` "
                      + ("more than once" if headings else "not at all"))
    start = None
    for index in range(headings[0] + 1, len(lines)):
        if fenced[index]:
            continue
        if lines[index].startswith("## "):
            break
        if lines[index].startswith("|"):
            start = index
            break
    if start is None:
        missing.append(f"the table under the heading `## {title}`")
        return None, f"the table `{title}` is missing"
    found = table_cells(lines[start])
    if found != columns:
        # A column absent from the header row, or standing under another name, is a field missing;
        # the columns all there in another order, or with another beside them, are not.
        absent = [name for name in columns if name not in found]
        missing.extend(f"the column `{name}` of the table `{title}`" for name in absent)
        return None, f"the table `{title}` does not have the header row the template gives"
    separator = start + 1
    if (separator >= len(lines) or not lines[separator].startswith("|")
            or not is_separator(table_cells(lines[separator]))):
        return None, f"the table `{title}` lacks its separator row"
    rows = []
    for index in range(separator + 1, len(lines)):
        if fenced[index] or not lines[index].startswith("|"):
            break
        rows.append(table_cells(lines[index]))
    return rows, None


def read_register(path: Path) -> Register:
    """The register of problems at `path`, read as untrusted input. A file larger than the cap, or
    not UTF-8, stops the run with nothing written. A table or a row that does not read is refused
    with its reason, and what depends on it is unknown; a missing table is also an error of the
    register."""
    try:
        with open(path, "rb") as handle:
            raw = handle.read(MAX_BYTES + 1)
    except OSError as error:
        raise AuditCountError("cannot read the register of problems: "
                              f"{display(error.strerror or error)}") from None
    if len(raw) > MAX_BYTES:
        raise AuditCountError(f"the register of problems is larger than {MAX_BYTES} bytes")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise AuditCountError("the register of problems is not UTF-8") from None
    lines = remarks_check.split_lines(text)
    fenced = remarks_check.fenced_flags(lines)
    register = Register()
    tables: dict[str, list[list[str]] | None] = {}
    missing: list[str] = []
    for title, columns in REGISTER_TABLES:
        rows, why = register_table(lines, fenced, title, columns, missing)
        if why:
            register.errors.append(why)
            register.refuse(f"table `{title}`", why)
        tables[title] = rows
    if missing:
        # The register is a file a human or a tool writes, and a field the count looks for data by
        # that it cannot find ends the run; the absence is never read as no rows (WAY-344).
        raise AuditCountError("the register of problems lacks " + ", ".join(missing))
    if tables["Classes"] is None:
        register.class_dates_unknown = True
    else:
        register.classes = [name for name, _, _ in
                            named_rows(register, "Classes", tables["Classes"], 4, check_class)]
        for cells in tables["Classes"]:
            if len(cells) != 4 or check_class(cells)[1] is not None:
                register.class_dates_unknown = True
                continue
            register.class_dates += [text for text in (cells[2], cells[3]) if valid_date(text)]
        register.class_dates.sort()
    if tables["Weights"] is not None:
        check_levels(register, "Weights", tables["Weights"], LEVELS, check_weight)
    if tables[COSTS_TITLE] is not None:
        check_levels(register, COSTS_TITLE, tables[COSTS_TITLE], COST_LEVELS, check_cost_level)
    if tables["Issues"] is not None:
        register.issues = [(name, cells[2], cells[3].lower()) for name, _, cells in
                           named_rows(register, "Issues", tables["Issues"], 4, check_issue)]
    if tables["Problems"] is not None:
        class_names = set(register.classes)
        issue_names = {name for name, _, _ in register.issues}
        for number, cells in enumerate(tables["Problems"], 1):
            value = f"row {number} of `Problems`"
            if len(cells) != 8:
                register.refuse(value, f"the row has {len(cells)} cells, not 8",
                                cells[0] if cells else "", cells[1] if len(cells) > 1 else "")
                register.refused_problems.append((cells[0] if cells else "",
                                                  cells[1] if len(cells) > 1 else "", ""))
                continue
            repository, record, _, _, cls, weight, cost, issue = cells
            why = None
            if not repository:
                why = "the row names no repository"
            elif FULL_HASH.fullmatch(record) is None:
                why = "the Record is no commit of 40 hexadecimal characters"
            elif cls not in class_names:
                why = "the class is not in the list of classes"
            elif weight not in LEVELS:
                why = "the weight is not one of the four levels"
            elif cost not in COST_LEVELS:
                why = "the cost of an occurrence is not one of the five levels"
            elif issue != NONE and issue not in issue_names:
                why = "the issue is in no valid row of Issues"
            if why:
                register.refuse(value, why, repository, record)
                register.refused_problems.append((repository, record, issue))
                continue
            register.problems.append(Problem(number, repository, record.lower(), cls, weight,
                                             cost, issue))
    return register


class Ancestry:
    """Whether the checkout of the-way holds a version: the answer of `git merge-base
    --is-ancestor`, asked of the checkout the entry `repository` under `the-way` names.
    A git that cannot read the checkout makes every answer unknown, with the reason."""

    def __init__(self, git: Git):
        self.git = git
        self.failure: str | None = None
        self.shallow = False
        self.commits: dict[str, tuple[str | None, str | None]] = {}
        self.holdings: dict[tuple[str, str], tuple[bool | None, str | None]] = {}
        try:
            self.shallow = git.run("rev-parse", "--is-shallow-repository").strip() == b"true"
        except GitError as error:
            self.failure = str(error)

    def commit(self, text: str) -> tuple[str | None, str | None]:
        """The full hash of the commit that `text` names in the checkout, or None with the reason:
        the checkout lacks it, a short hash is ambiguous, or it is no commit."""
        if text not in self.commits:
            self.commits[text] = self.resolve(text)
        return self.commits[text]

    def resolve(self, text: str) -> tuple[str | None, str | None]:
        if self.failure is not None:
            return None, f"the checkout of the-way could not be read by git: {self.failure}"
        if SHORT_HASH.fullmatch(text) is None:
            return None, "the commit is no hexadecimal name of a commit"
        shallow = " (the checkout is a shallow clone, which may lack it)" if self.shallow else ""
        try:
            names = self.git.run("rev-parse", f"--disambiguate={text}").decode("ascii").split()
            if not names:
                return None, f"the-way's history lacks commit {text}{shallow}"
            if len(names) > 1:
                return None, f"the short hash {text} is ambiguous in the-way's history"
            if self.git.code("rev-parse", "--verify", "--quiet", f"{names[0]}^{{commit}}") != 0:
                return None, f"{text} is no commit of the-way's history"
        except GitError as error:
            return None, f"git could not read the-way's history: {error}"
        return names[0], None

    def holds(self, pin: str, fix: str) -> tuple[bool | None, str | None]:
        """Whether the version `pin` holds the commit `fix`, or None with the reason."""
        if (pin, fix) not in self.holdings:
            self.holdings[(pin, fix)] = self.compare(pin, fix)
        return self.holdings[(pin, fix)]

    def compare(self, pin: str, fix: str) -> tuple[bool | None, str | None]:
        version, why = self.commit(pin)
        if version is None:
            return None, why
        fixed, why = self.commit(fix)
        if fixed is None:
            return None, why
        try:
            code = self.git.code("merge-base", "--is-ancestor", fixed, version)
        except GitError as error:
            return None, f"git could not compare the version {pin} with the fix: {error}"
        if code == 0:
            return True, None
        if code == 1:
            if self.shallow:
                return None, ("the version lacks the fix in a shallow clone of the-way, which may "
                              "lack its history")
            return False, None
        return None, f"git could not compare the version {pin} with the fix (exit code {code})"

    def stamp(self, version: str) -> tuple[int | None, str | None]:
        """The committer date of a full commit hash of the checkout, as a Unix time, or None with
        the reason; a value that is no number is not read (WAY-339)."""
        try:
            text = self.git.run("log", "-1", "--format=%ct", version, "--").decode("ascii").strip()
        except (GitError, ValueError) as error:
            return None, f"git could not read the date of the commit: {display(error)}"
        try:
            return int(text), None
        except ValueError:
            return None, "the date of the commit is not a number"

    def differs(self, earlier: str, later: str, paths: tuple[str, ...]) -> bool:
        """Whether the files at `paths` differ between two full commit hashes of the-way, by
        `git diff --quiet`: exit 1, or any failure, counts as changed."""
        try:
            return self.git.code("diff", "--quiet", earlier, later, "--", *paths) != 0
        except GitError:
            return True


def counted(count: int, refused: int) -> str:
    """A count as a cell: exact where no refused row belongs to it, `at least n` where some does."""
    return f"at least {count}" if refused else str(count)


@dataclass
class Analysis:
    """The tables the register adds to the result, as rows of text; the values it leaves unknown
    as (repository, record, value, why) (`unknown`), and the values the register holds back, its
    refused rows and problems whose cycle is not read (`held`); both go into the pairs of
    *Unknown values* alike."""
    cycle_rows: list[list[str]]
    fixed_rows: list[list[str]]
    open_rows: list[list[str]]
    dropped_rows: list[list[str]]
    cost_rows: list[list[str]]
    unknown: list[tuple[str, str, str, str]]
    held: list[tuple[str, str, str, str]]


def analyse(reads: list["Read"], register: Register, ancestry: Ancestry,
            today: date) -> Analysis:
    """Count the register's problems against the cycles the reads found: per cycle by class and
    weight, per fixed issue by whether the pin of its cycles holds the fix, and
    per open issue the cycles it came back in and the days it has waited."""
    cycles = [cycle for read in reads for cycle in read.cycles]
    # Each commit that adds a copy of a record, with the cycles whose copy it adds: one commit may
    # add the records of several cycles, and then it names none of them.
    owners: dict[tuple[str, str], list[Cycle]] = {}
    for cycle in cycles:
        for record in dict.fromkeys([cycle.record, *cycle.later]):
            owners.setdefault((cycle.repository, record), []).append(cycle)
    index = {key: found[0] for key, found in owners.items() if len(found) == 1}
    shared = {key: found for key, found in owners.items() if len(found) > 1}
    # The problems of a *Record* that names several cycles count in none of them, so the counts of
    # each of those cycles read `at least n`.
    uncounted: Counter = Counter()
    found = [(problem, index.get((problem.repository, problem.record)))
             for problem in register.problems]
    # The values the register holds back are its refused rows and the problems whose cycle is not
    # read; every unknown value, those included, is grouped by field and reason in `unknown_rows`.
    held = list(register.refused)
    unknown: list[tuple[str, str, str, str]] = []
    counts: dict[tuple[str, str], Counter] = {}
    for problem, cycle in found:
        if cycle is not None:
            tally = counts.setdefault((cycle.repository, cycle.record), Counter())
            tally[(problem.cls, problem.weight)] += 1
            continue
        key = (problem.repository, problem.record)
        if key in shared:
            for owner in shared[key]:
                uncounted[(owner.repository, owner.record)] += 1
            why = ("its Record is a commit that adds the records of more than one cycle, so the "
                   "cycle it belongs to is not known")
        else:
            why = ("no named repository holds the cycle of its record; name its key with "
                   "--repository")
        held.append((problem.repository[:TEXT_CAP], problem.record,
                     f"row {problem.number} of `Problems`", why))
    # A refused row belongs to the cycle its Repository and Record name, and to the issue its Issue
    # names, when each is usable; a row with neither stays in *Unknown values* only. Its count shows
    # as `at least n`, since the row's own figure is not in the count.
    refused_cycle: Counter = Counter()
    refused_issue: Counter = Counter()
    valid_issues = {name for name, _, _ in register.issues}
    for repository, record, issue in register.refused_problems:
        key = (repository, record.lower())
        cycle = index.get(key) if FULL_HASH.fullmatch(record) else None
        if cycle is not None:
            refused_cycle[(cycle.repository, cycle.record)] += 1
        elif FULL_HASH.fullmatch(record) and key in shared:
            for owner in shared[key]:
                uncounted[(owner.repository, owner.record)] += 1
        if issue in valid_issues:
            refused_issue[issue] += 1
    cycle_rows = []
    for cycle in cycles:
        key = (cycle.repository, cycle.record)
        mine = counts.get(key, Counter())
        refused = refused_cycle[key]
        partial = refused + uncounted[key]
        head = [cycle.repository, cycle.record]
        rows_here = []
        for cls in register.classes:
            tally = [mine[(cls, weight)] for weight in LEVELS]
            if any(tally):
                rows_here.append(head + [cls] + [counted(count, partial) for count in tally]
                                 + [str(refused)])
        if not rows_here:
            rows_here.append(head + [NONE] + [counted(0, partial)] * 4 + [str(refused)])
        cycle_rows += rows_here
    # The problems of each issue, gathered once rather than by a scan of every problem per issue.
    by_issue: dict[str, list[tuple[Problem, Cycle | None]]] = {}
    for problem, cycle in found:
        by_issue.setdefault(problem.issue, []).append((problem, cycle))
    fixed_rows, open_rows, dropped_rows, cost_rows = [], [], [], []
    for name, fate, fix in register.issues:
        members = by_issue.get(name, [])
        # The cost of an occurrence stands in the problem's row, so the cycle is not needed: a
        # problem of a cycle that is not read is counted, and a refused row makes the count a lower
        # bound.
        levels = Counter(problem.cost for problem, _ in members)
        cost_rows.append([name, fate] + [counted(levels[level], refused_issue[name])
                                         for level in COST_LEVELS] + [str(refused_issue[name])])
        hit = {(cycle.repository, cycle.record): cycle for _, cycle in members
               if cycle is not None}
        not_read = sum(1 for _, cycle in members if cycle is None)
        refused = refused_issue[name]
        if fate == FIXED:
            fixed, why = ancestry.commit(fix)
            if fixed is None:
                unknown.append((THE_WAY, NONE, f"the fix of issue `{name}`", why))
            holding = lacking = pin_unknown = 0
            for _, cycle in members:
                if cycle is None:
                    continue
                if cycle.pin is None:
                    pin_unknown += 1
                elif fixed is not None:
                    holds, why = ancestry.holds(cycle.pin, fix)
                    if holds is None:
                        pin_unknown += 1
                        unknown.append((cycle.repository, cycle.record, "Process pin", why))
                    elif holds:
                        holding += 1
                    else:
                        lacking += 1
            shown = (["unknown", "unknown"] if fixed is None
                     else [counted(holding, refused), counted(lacking, refused)])
            fixed_rows.append([name, fix] + shown + [counted(pin_unknown, refused),
                                                     counted(not_read, refused), str(refused)])
        elif fate == "open":
            # Each problem waits from the copy its Record names, which after a correction may be
            # a later copy than the cycle's first.
            dates = [cycle.copies.get(problem.record, cycle.committed)
                     for problem, cycle in members if cycle is not None]
            if refused:
                days = UNKNOWN
                unknown.append((THE_WAY, NONE, f"waiting of issue `{name}`",
                                "some of its problem rows are refused, so its waiting is not "
                                "known"))
            elif not members:
                days = "—"
            elif not_read:
                days = UNKNOWN
                unknown.append((THE_WAY, NONE, f"waiting of issue `{name}`",
                                "a problem's cycle is not known, so the day it came back first is "
                                "not known"))
            elif UNKNOWN in dates:
                days = UNKNOWN
                unknown.append((THE_WAY, NONE, f"waiting of issue `{name}`",
                                "the commit date of the copy one of its problems names is unknown"))
            else:
                waited = (today - date.fromisoformat(min(dates))).days
                if waited < 0:
                    days = UNKNOWN
                    unknown.append((THE_WAY, NONE, f"waiting of issue `{name}`",
                                    "its earliest copy is dated after the day of the run"))
                else:
                    days = str(waited)
            # The problem stands in the first cycle it is found in and comes back in each other
            # cycle, so the count is the cycles that hold it less one, whichever of them is first.
            # A refused row or a problem of an unread cycle may belong to a cycle not counted
            # here, so the count is a lower bound then: at least the known cycles less one.
            came_back = max(len(hit) - 1, 0)
            open_rows.append([name, counted(came_back, refused + not_read),
                              counted(len(members), refused), counted(not_read, refused), days,
                              str(refused)])
        else:
            dropped_rows.append([name, counted(len(hit), refused), counted(len(members), refused),
                                 counted(not_read, refused), str(refused)])
    return Analysis(cycle_rows, fixed_rows, open_rows, dropped_rows, cost_rows,
                    list(dict.fromkeys(unknown)), list(dict.fromkeys(held)))


def unknown_field(value: str) -> str:
    """The field of an unknown value: the value with the number of its row, the name of its issue
    and the commit of its version taken out, so that the values of one kind make one pair."""
    value = ROW_NUMBER.sub("row of ", value, count=1)
    value = ISSUE_VALUE.sub(r"\1 of an issue", value, count=1)
    return VERSION_SUFFIX.sub("a version", value, count=1)


def unknown_rows(unknown: list[tuple[str, str, str, str]]) -> list[list[str]]:
    """The unknown values as one row for each pair of a field and a reason, in the order each pair
    first occurs: the count is the values of the pair, and the examples are the first EXAMPLES of
    them, each as repository, record and value."""
    counts: Counter = Counter()
    examples: dict[tuple[str, str], list[str]] = {}
    for repository, record, value, why in unknown:
        key = (unknown_field(value), why)
        counts[key] += 1
        shown = examples.setdefault(key, [])
        if len(shown) < EXAMPLES:
            shown.append(f"{repository} {record}: {value}")
    return [[field_text, str(counts[(field_text, why)]), why,
             "; ".join(examples[(field_text, why)])] for field_text, why in counts]


# The process versions (WAY-339)


@dataclass
class Version:
    """A version of the process: the full commit of the-way that cycles pin, its committer date
    as a Unix time and as a day, the price list its costs are priced by, and its cycles."""
    commit: str
    stamp: int
    day: str
    price: str
    cycles: list[Cycle]


@dataclass
class Series:
    """A run of versions between which no change splits a series: why it begins with its first
    version, its versions, and the rows of its table."""
    begins: str
    versions: list[Version]
    rows: list[list[str]] = field(default_factory=list)


@dataclass
class Versions:
    # The two kinds of series of the process versions (WAY-339): the series of the cost, the
    # median cost and Q3 are compared in; and the series of the count of remarks, Q1 and Q2 are
    # compared in, which ends wherever a series of the cost ends and at more changes.
    cost: list[Series] = field(default_factory=list)
    count: list[Series] = field(default_factory=list)
    no_version: list[Cycle] = field(default_factory=list)
    unknown: list[tuple[str, str, str, str]] = field(default_factory=list)
    # Every version, in the order of their dates: the series of the measures are made of them.
    ordered: list["Version"] = field(default_factory=list)


SERIES_COST = "Cost"
SERIES_COUNT = "Count of remarks"
COST_HEADER = ["Version (commit)", "Committed", "Cycles", "Cycles with a known cost",
               "Median cost (USD)", "Q3: cost falls"]
COUNT_HEADER = ["Version (commit)", "Committed", "Cycles", "Q1: contradiction only after code",
                "Plans read", "Q2: more than a third of slices too large"]


def median_of(costs: list[Decimal]) -> Decimal | None:
    """The median of the costs: the middle one, or the mean of the two middle ones; None where
    there is none."""
    if not costs:
        return None
    ordered = sorted(costs)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


FIRST_VERSION = "the first version of the result"


def changed_paths(ancestry: Ancestry, earlier: str, later: str,
                  paths: tuple[str, ...]) -> list[str]:
    """The paths of `paths` whose files differ between two full commit hashes of the-way, none
    where no file does: `git diff --quiet` of each, a failure counting as changed, so that a series
    is never joined by mistake (WAY-339)."""
    if not ancestry.differs(earlier, later, paths):
        return []
    return [path for path in paths if ancestry.differs(earlier, later, (path,))] or list(paths)


def names_of(paths: list[str]) -> str:
    return " and ".join(f"`{path}`" for path in paths)


def changed_reason(ancestry: Ancestry, earlier: str, later: str,
                   paths: tuple[str, ...]) -> str | None:
    """None where the files at `paths` do not differ between two full commit hashes of the-way,
    else a reason that names the paths that changed (WAY-339)."""
    changed = changed_paths(ancestry, earlier, later, paths)
    return f"{names_of(changed)} changed between the two versions" if changed else None


# A cycle that changed the tool that wrote a file of its copy (WAY-339)


def withdraw_values(cycle: Cycle, file: str, reason: str) -> None:
    """Give the values the tool that wrote `file` measured as unknown, with the reason, in place of
    what the file gave and of the reasons and the missing fields of its reading: the file is not
    read for this cycle. The number of fix rounds stands, since the record gives it, not the
    script."""
    if file == STAGES_FILE:
        cycle.working = cycle.waiting = cycle.cost = cycle.share = None
        names = STAGES_VALUES
        cycle.missing = []
    elif file == MEASURES_FILE:
        cycle.measures = {}
        names = ("Mechanism measures",)
        cycle.unknown = [pair for pair in cycle.unknown if pair[0] not in MEASURE_LABELS]
        cycle.missing_in = [pair for pair in cycle.missing_in if pair[0] != MEASURES_FILE]
    else:
        cycle.gate_runs, cycle.gate_timed = [], []
        names = ("Gate runs",)
        cycle.unknown = [pair for pair in cycle.unknown if not pair[0].startswith("Gate runs")]
        cycle.missing_in = [pair for pair in cycle.missing_in if pair[0] != GATE_FILE]
    cycle.unknown = [pair for pair in cycle.unknown if pair[0] not in names]
    cycle.unknown += [(name, reason) for name in names]


def note_changed_tools(reads: list["Read"], ancestry: Ancestry) -> None:
    """For each cycle of the-way, give as unknown the values of each file of its copy whose tool
    the cycle's own change changed (WAY-339): the files of the tool differ between the version the
    cycle ran on and the commit of the last copy of its record in the-way's own history, by `git
    diff --quiet`, a failure counting as changed. Only a cycle of the-way is read so: the change of
    a cycle of another repository lies in that repository, which holds none of these tools, and its
    copy is not a commit of the-way's history. A cycle whose version does not resolve, and a copy
    that holds no such file, which is of an earlier form, are left as they are."""
    for read in reads:
        if read.key != THE_WAY:
            continue
        for cycle in read.cycles:
            version = ancestry.commit(cycle.pin)[0] if cycle.pin is not None else None
            if version is None:
                continue
            last = cycle.later[-1] if cycle.later else cycle.record
            for file, paths in TOOL_GROUPS:
                changed = (changed_paths(ancestry, version, last, paths)
                           if file in cycle.held else [])
                if changed:
                    withdraw_values(cycle, file, f"the cycle changed the tool that wrote them: "
                                                 f"{names_of(changed)} changed between the "
                                                 f"version it ran on and the last copy of its "
                                                 f"record")


def cost_boundary(earlier: Version, later: Version, ancestry: Ancestry) -> str | None:
    """Why a new series of the cost begins at `later`, or None where both versions share one: a
    new price list, or a change of the script that measures the cost, and nothing else."""
    if earlier.price != later.price:
        return "the price list changed"
    return changed_reason(ancestry, earlier.commit, later.commit, COST_SCRIPTS)


def count_boundary(earlier: Version, later: Version, register: Register,
                   ancestry: Ancestry) -> str | None:
    """Why a new series of the count of remarks begins at `later`, or None where both versions
    share one: wherever a series of the cost begins, and at a date of the register's list of
    classes or a change of the files that give the form of a stage report or the reviewer's
    instructions."""
    why = cost_boundary(earlier, later, ancestry)
    if why is not None:
        return why
    if register.class_dates_unknown:
        return "the register's list of classes is not given in full, so it may have changed"
    # A date on the day of either version counts: the test errs toward more series.
    at = bisect.bisect_left(register.class_dates, earlier.day)
    if at < len(register.class_dates) and register.class_dates[at] <= later.day:
        return "the register's list of classes changed between the two versions"
    return changed_reason(ancestry, earlier.commit, later.commit, COUNT_PATHS)


def split_series(versions: list[Version], boundary) -> list[Series]:
    """Split the versions, in the order of their dates, into runs: a new one begins at a version
    for which `boundary(previous version, version)` gives a reason, which the series keeps."""
    blocks: list[Series] = []
    for number, version in enumerate(versions):
        why = boundary(versions[number - 1], version) if number else None
        if why is None and blocks:
            blocks[-1].versions.append(version)
        else:
            blocks.append(Series(why or FIRST_VERSION, [version]))
    return blocks


def instrument_series(versions: list[Version], ancestry: Ancestry,
                      scripts: tuple[str, ...]) -> list[Series]:
    """Split the versions, in the order of their dates, into series by the change of the scripts
    alone: a series begins at a version whose files at `scripts` differ from the previous
    version's (WAY-339), and its reason names the scripts that changed. Nothing else splits it:
    not the price list, the register's list of classes or the files of the count of remarks."""
    return split_series(versions, lambda earlier, later: changed_reason(
        ancestry, earlier.commit, later.commit, scripts))


@dataclass
class MeasureVersions:
    """The series of the mechanism measures and of the gate times, each with its rows, and the
    answers of *Falls* that are unknown as (repository, record, value, why)."""
    mechanism: list[Series] = field(default_factory=list)
    gate: list[Series] = field(default_factory=list)
    unknown: list[tuple[str, str, str, str]] = field(default_factory=list)


NO_MEASURE = "—"  # the measure cell of the one row of a version that gives no value
MECHANISM_HEADER = ["Version (commit)", "Measure", "Cycles with a value", "Median", "Falls"]
GATE_HEADER = ["Version (commit)", "Measure", "Runs compared", "Median (seconds)", "Falls",
               "Runs not compared", "Median of those (seconds)"]


def median_text(median: Decimal | None, suffix: str = "") -> str:
    """A median as the exact value of its Decimal, a half with its decimal, never in exponent
    form."""
    return UNKNOWN if median is None else format(median, "f") + suffix


def falls_answer(version: Version, first: bool, median: Decimal | None,
                 previous: Decimal | None, subject: str, rest: str, what: str,
                 unknown: list[tuple[str, str, str, str]], name: str) -> str:
    """`yes` where the median is lower than the previous version's of the same measure in the same
    series, `no` where it is not, and `unknown`, with its reason kept in `unknown`, where the
    version is the first of its series or either median is not known."""
    if first:
        why = "no previous version in the series"
    elif median is None:
        why = f"no {subject} of the version{rest} gives {what}, so its median is not known"
    elif previous is None:
        why = f"no {subject} of the previous version{rest} gives {what}"
    else:
        return "yes" if median < previous else "no"
    unknown.append((THE_WAY, NONE, f"{name}, version {version.commit}", why))
    return UNKNOWN


def measure_number(label: str, text: str) -> Decimal:
    """The value of a cycle-level line that `read_measures` kept: a whole number, or for the share
    a number of percent with one decimal."""
    return Decimal(text[:-1] if label == SHARE_LABEL else text)


def mechanism_rows(block: Series, unknown: list[tuple[str, str, str, str]]) -> None:
    """The rows of a series of the mechanism measures: for each version and each cycle-level
    measure, the median of the cycles that give a value and whether it falls."""
    previous: dict[str, Decimal | None] = {}
    for index, version in enumerate(block.versions):
        medians: dict[str, Decimal | None] = {}
        if not any(label in cycle.measures for cycle in version.cycles for label in MEASURE_LABELS):
            # A version no cycle of which gives a value has one row and one line of reason.
            block.rows.append([version.commit, NO_MEASURE, "0", UNKNOWN, UNKNOWN])
            unknown.append((THE_WAY, NONE, f"Mechanism measures of version {version.commit}",
                            "no cycle of this version gives a value: its copies hold no "
                            f"`{MEASURES_FILE}` (an earlier cycle, or a script that failed; the "
                            "record's *Verification* says which) or give none"))
            previous = {}
            continue
        for label in MEASURE_LABELS:
            values = [measure_number(label, cycle.measures[label])
                      for cycle in version.cycles if label in cycle.measures]
            median = median_of(values)
            medians[label] = median
            falls = falls_answer(version, index == 0, median, previous.get(label), "cycle", "",
                                 "a value", unknown, f"Measure falls: {label}")
            block.rows.append([version.commit, label, str(len(values)),
                               median_text(median, "%" if label == SHARE_LABEL else ""), falls])
        previous = medians


def gate_values(version: Version) -> dict[str, tuple[list[Decimal], list[Decimal]]]:
    """The times of the runs of a version, over all its cycles, by measure: the total first and
    then each directory that any run has, by name. Each measure holds the values of the runs that
    passed with no other gate and apart those of the runs not compared: with another gate, with an
    unknown count, that failed or whose exit code is unknown; a run that does not give the time
    adds to neither (WAY-350)."""
    found: dict[str, tuple[list[Decimal], list[Decimal]]] = {TOTAL_MEASURE: ([], [])}
    for cycle in version.cycles:
        for run in cycle.gate_timed:
            side = 0 if run.others == 0 and run.code == 0 else 1
            if run.total is not None:
                found[TOTAL_MEASURE][side].append(run.total)
            for name, seconds in run.directories:
                lists = found.setdefault(DIRECTORY_MEASURE + name, ([], []))
                if seconds is not None:
                    lists[side].append(seconds)
    return {name: found[name] for name in [TOTAL_MEASURE, *sorted(found.keys() - {TOTAL_MEASURE})]}


def gate_rows(block: Series, unknown: list[tuple[str, str, str, str]]) -> None:
    """The rows of a series of the gate times: for each version and each measure, the median of the
    runs that passed with no other gate and whether it falls, and the runs not compared apart,
    never compared (WAY-350). A version no run of which gives a time has one row and one line of
    reason."""
    previous: dict[str, Decimal | None] = {}
    for index, version in enumerate(block.versions):
        medians: dict[str, Decimal | None] = {}
        values = gate_values(version)
        if all(not alone and not apart for alone, apart in values.values()):
            block.rows.append([version.commit, NO_MEASURE, "0", UNKNOWN, UNKNOWN, "0", UNKNOWN])
            unknown.append((THE_WAY, NONE, f"Gate times of version {version.commit}",
                            "no run of this version gives a time: its copies hold no "
                            f"`{GATE_FILE}` ({ABSENCE_CAUSES[GATE_FILE]}; the "
                            "record's *Verification* says which) or give none"))
            previous = {}
            continue
        for name, (alone, apart) in values.items():
            median = median_of(alone)
            medians[name] = median
            falls = falls_answer(version, index == 0, median, previous.get(name), "run",
                                 " that passed with no other gate", "this time", unknown,
                                 f"Gate time falls: {name}")
            block.rows.append([version.commit, name, str(len(alone)), median_text(median), falls,
                               str(len(apart)), median_text(median_of(apart))])
        previous = medians


def measure_versions(versions: Versions, ancestry: Ancestry) -> MeasureVersions:
    """Group the versions into the series of each instrument and give the medians and the
    comparison of each version within its own series (WAY-339, WAY-350)."""
    result = MeasureVersions()
    result.mechanism = instrument_series(versions.ordered, ancestry, (MEASURES_SCRIPT,))
    result.gate = instrument_series(versions.ordered, ancestry, GATE_SCRIPTS)
    for block in result.mechanism:
        mechanism_rows(block, result.unknown)
    for block in result.gate:
        gate_rows(block, result.unknown)
    return result


def contradiction_of(version: Version) -> tuple[str, str | None]:
    """Q1 for a version: yes where a cycle answers yes, no where every cycle answers no."""
    answers = [cycle.contradiction for cycle in version.cycles]
    if "yes" in answers:
        return "yes", None
    if answers and all(answer == "no" for answer in answers):
        return "no", None
    return "unknown", "a cycle's answer is unknown, so the question is not settled for the version"


def too_large_of(version: Version) -> tuple[str, str, str | None]:
    """Q2 for a version, with the cell *Plans read*: the sums of the slices of the version's plans,
    too-large over planned, above one third is yes. Where a plan is not read, its slices could
    turn either answer, so the answer is unknown."""
    planned_cycles = [cycle for cycle in version.cycles if not cycle.plan_left_out]
    read = [cycle for cycle in planned_cycles
            if cycle.planned is not None and cycle.too_large is not None]
    plans_read = f"{len(read)} of {len(planned_cycles)}"
    if not read:
        return plans_read, "unknown", "no cycle's plan can be read"
    if len(read) < len(planned_cycles):
        return plans_read, "unknown", (f"the plans of {len(planned_cycles) - len(read)} cycle(s) "
                                       "are not read, so the share of the version's slices is "
                                       "not known")
    planned = sum(cycle.planned for cycle in read if cycle.planned is not None)
    large = sum(cycle.too_large for cycle in read if cycle.too_large is not None)
    if planned == 0:
        return plans_read, "unknown", "the plans that are read hold no slice"
    return plans_read, ("yes" if 3 * large > planned else "no"), None


def process_versions(reads: list[Read], register: Register, ancestry: Ancestry,
                     prices: Prices) -> Versions:
    """Group the cycles by their version, split the versions into series, and answer the three
    questions of each version within its own series (WAY-339)."""
    result = Versions()
    groups: dict[str, list[Cycle]] = {}
    for read in reads:
        for cycle in read.cycles:
            if cycle.pin is None:
                result.no_version.append(cycle)
                continue
            commit, why = ancestry.commit(cycle.pin)
            if commit is None:
                result.no_version.append(cycle)
                result.unknown.append((cycle.repository, cycle.record, "Process pin", why or ""))
                continue
            groups.setdefault(commit, []).append(cycle)
    versions: list[Version] = []
    for commit, members in groups.items():
        stamp, why = ancestry.stamp(commit)
        day = committed_date(str(stamp)) if stamp is not None else None
        if day is None:
            why = why or "the commit's date lies outside the years the command can read"
            result.no_version += members
            result.unknown.append((THE_WAY, NONE, f"version {commit}", why))
            result.unknown += [(cycle.repository, cycle.record, "Process pin",
                                "its version has no readable date") for cycle in members]
            continue
        versions.append(Version(commit, stamp or 0, day, prices.date, members))
    versions.sort(key=lambda version: (version.stamp, version.commit))
    result.ordered = versions
    result.count = split_series(
        versions, lambda earlier, later: count_boundary(earlier, later, register, ancestry))
    result.cost = split_series(
        versions, lambda earlier, later: cost_boundary(earlier, later, ancestry))
    for block in result.count:
        count_rows(block, result.unknown)
    for block in result.cost:
        cost_rows(block, result.unknown)
    return result


def count_rows(block: Series, unknown: list[tuple[str, str, str, str]]) -> None:
    """The rows of a series of the count of remarks: for each version its answers Q1 and Q2, each
    with its reason in `unknown` where it is not known. No number of the cost stands in them."""
    for version in block.versions:
        answer1, why1 = contradiction_of(version)
        plans, answer2, why2 = too_large_of(version)
        for label, why in (("contradiction only after code", why1), ("slices too large", why2)):
            if why:
                unknown.append((THE_WAY, NONE, f"{label}, version {version.commit}", why))
        block.rows.append([version.commit, version.day, str(len(version.cycles)), answer1, plans,
                           answer2])


def cost_rows(block: Series, unknown: list[tuple[str, str, str, str]]) -> None:
    """The rows of a series of the cost: for each version the median cost of its cycles with a
    known cost, and Q3, whether it is lower than the previous version's of the same series."""
    previous: Version | None = None
    previous_median: Decimal | None = None
    for version in block.versions:
        costs = [cycle.cost for cycle in version.cycles if cycle.cost is not None]
        median = median_of(costs)
        if previous is None:
            answer3, why3 = "unknown", "no previous version in the series"
        elif median is None or previous_median is None:
            answer3, why3 = "unknown", "a median cost is not known"
        else:
            answer3 = "yes" if median < previous_median else "no"
            why3 = None
        if why3:
            unknown.append((THE_WAY, NONE, f"cost falls, version {version.commit}", why3))
        block.rows.append([version.commit, version.day, str(len(version.cycles)), str(len(costs)),
                           money(median), answer3])
        previous, previous_median = version, median


def versions_lines(versions: Versions) -> list[str]:
    """The section *Process versions*: a table per series of the cost and per series of the
    count of remarks, each with the reason it begins where it does, and a note of the cycles in no
    version."""
    lines = [
        "## Process versions",
        "",
        "A version of the process is the commit of the-way that its cycles' *Process pin* "
        "resolves to, ordered by the commit's date. The versions are cut into series of two kinds "
        "(WAY-339), and a measure is compared only inside a series of its own kind: no cell sets "
        "a number of one kind of series beside a number of the other.",
        "",
        "A series of the cost holds the median cost and the answer Q3. It begins at a new price "
        f"list or at a change of `{COST_SCRIPT}`, the script that measures the cost, and at no "
        "other change: not at a change of the instructions of the reviewer.",
        "",
        "A series of the count of remarks holds the answers Q1 and Q2. It begins wherever a "
        "series of the cost begins, and also at a date of *Added* or *Withdrawn* of the "
        "register's list of classes, and at any change of the files that give the form of a "
        "stage report or the instructions of the reviewer: those under `task-cycle/change`, "
        "`task-cycle/plan`, `task-cycle/review` and `task-cycle/spec`, and "
        "`task-cycle/agent-types/the-way-stage.md`, whose text the reviewer receives as its "
        "instruction. The test is `git diff --quiet` (exit 1, or any other failure, counts as "
        "changed), and any change of those files begins a series, whether or not it alters that "
        "form or those instructions. The price of keeping the series of the cost whole across "
        "such a change: a rise of the cost after a change of the reviewer's instructions may be "
        "the reviewer finding more or the process getting dearer, and the count of remarks, "
        "whose meaning changes with the reviewer, is the series that ends there.",
        "",
        "Q1, Q2 and Q3 are `yes`, `no` or `unknown`; *Unknown values* says why an answer is "
        "unknown. The reason each series begins where it does stands under its heading.",
        "",
    ]
    for title, blocks, header in ((SERIES_COST, versions.cost, COST_HEADER),
                                  (SERIES_COUNT, versions.count, COUNT_HEADER)):
        for number, block in enumerate(blocks, 1):
            lines += [f"### {title}, series {number}", "",
                      f"Begins at this version: {block.begins}.", ""]
            lines += table(header, block.rows)
            lines.append("")
    if versions.no_version:
        lines += [
            "### No version",
            "",
            f"{len(versions.no_version)} cycle(s) stand in no version and in no series: their "
            "*Process pin* is unknown, does not resolve in the-way's history, or names a commit "
            "with no readable date. Each reason is in *Unknown values*.",
            "",
        ]
    if lines[-1] == "":
        lines.pop()
    return lines


def measure_versions_lines(measured: MeasureVersions) -> list[str]:
    """The section *Measure versions*: a table per series of each instrument, the median of each
    measure of each version and whether it falls against the previous version of its series."""
    lines = [
        "## Measure versions",
        "",
        "The versions are those of *Process versions*, but the series are not: the measures of how "
        "a cycle's agents use context and the prompt cache and the times of the gate are the "
        "numbers by which a change to the instructions of the cycle is judged, so only a change of "
        "the instrument that measures them splits them (WAY-339). A series of the mechanism "
        f"measures begins at a version whose `{MEASURES_SCRIPT}` differs from the previous "
        f"version's, and a series of the gate times at one whose `{GATE_SCRIPT}` or "
        f"`{GATE_TEST_RUNNER}` differs, by "
        "`git diff --quiet` (exit 1, or any other failure, counts as changed). A new price list, a "
        "date of the register's list of classes and a change under `task-cycle/change`, "
        "`task-cycle/plan`, `task-cycle/review`, `task-cycle/spec` or of "
        "`task-cycle/cycle_stages.py` split neither, though a new price list and a change of "
        "`task-cycle/cycle_stages.py` split the series of the cost, and the others the series "
        "of the count of remarks. "
        "Each series is its own subsection, a number of one series is never set beside a number of "
        "another, and the cycles in no version stand in no series. *Falls* is `yes` where the "
        "median is lower than the previous version's median of the same measure in the same "
        "series, `no` where it is not, and `unknown` where the version is the first of its series "
        "or either median is not known; *Unknown values* says why. A median is written as the "
        "exact value, a half with its decimal.",
        "",
        "*Mechanism measures*: the median is of the values of the version's cycles that give one, "
        "and *Cycles with a value* counts them.",
        "",
        "*Gate times*: the runs are taken together over all the cycles of the version. The median "
        "and *Falls* take only the runs that passed (exit code 0) during which no other gate run by "
        "the script was going (*Runs compared*, WAY-350). The runs not compared are those with "
        "another gate, with the count `unknown`, that failed (a failed run's time says how soon "
        "it failed, not how long the gate takes) or whose exit code is unknown: they are counted "
        "and their median shown apart in the last two columns and are never compared, so a "
        "version in which no run passed alone has no comparison. Each count is of the runs that "
        "give the time of its row, and a directory's median takes the runs that give its time. A "
        "version in which no cycle gives a value, or no run a time, has one row, with `—` for the "
        "measure, and a value in *Unknown values*.",
        "",
    ]
    for title, blocks, header in (("Mechanism measures", measured.mechanism, MECHANISM_HEADER),
                                  ("Gate times", measured.gate, GATE_HEADER)):
        for number, block in enumerate(blocks, 1):
            lines += [f"### {title}, series {number}", "",
                      f"Begins at this version: {block.begins}.", ""]
            lines += table(header, block.rows)
            lines.append("")
    if lines[-1] == "":
        lines.pop()
    return lines


# The result


def cell(text: str) -> str:
    """Text on one line that cannot end or split a cell of a table: a bar is written `\\x7c`, as
    `display` writes a control character, so that no cell holds a bar at all. An escaped bar
    `\\|` would not do: Markdown readers differ on whether a backslash before it escapes the bar
    or is itself escaped, and a reader of the second kind ends the cell there."""
    return display(" ".join(str(text).split())).replace("|", "\\x7c")


def duration(seconds: int | None) -> str:
    if seconds is None:
        return UNKNOWN
    hours, rest = divmod(seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    return f"{hours}:{minutes:02}:{seconds:02}"


def money(value: Decimal | None) -> str:
    return UNKNOWN if value is None else format(value.quantize(MONEY), "f")


def share_text(value: Decimal | None) -> str:
    return UNKNOWN if value is None else f"{value.quantize(SHARE)}%"


def table(header: list[str], rows: list[list[str]]) -> list[str]:
    """A Markdown table of the header and the rows, every cell written through `cell`."""
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(cell(text) for text in row) + " |" for row in rows]
    return lines


def measures_lines(cycles: list[Cycle]) -> list[str]:
    """The section *Mechanism measures*: one row per cycle, each label of the file a column."""
    lines = [
        "## Mechanism measures",
        "",
        "Written by `task-cycle/cycle_measures.py` into each cycle's record as "
        "`mechanism_measures.md`; `unknown` is never zero, and *Unknown values* says why. The "
        "table of agents stays in that file.",
        "",
    ]
    rows = [[cycle.repository, cycle.record,
             *[cycle.measures.get(label, UNKNOWN) for label in MEASURE_LABELS]]
            for cycle in cycles]
    return lines + table(["Repository", "Record", *MEASURE_LABELS], rows)


def gate_lines(cycles: list[Cycle]) -> list[str]:
    """The section *Gate runs*: one row per run, a cycle with no run having none."""
    lines = [
        "## Gate runs",
        "",
        "Written by `task-cycle/gate_times.py` into each cycle's record as `gate_times.md`, one row "
        "per run of the gate; times are seconds, and `unknown` is never zero. *Directories* lists "
        "each directory the gate printed with its seconds, and `—` where it printed none.",
        "",
    ]
    rows = [[cycle.repository, cycle.record, *run] for cycle in cycles for run in cycle.gate_runs]
    return lines + table(["Repository", "Record", "Started (UTC)", "Exit code", "Total seconds",
                          "Other gate runs at the same time", "Directories"], rows)


def render(reads: list[Read], prices: Prices, analysis: Analysis, versions: Versions,
           measured: MeasureVersions) -> str:
    cycles = [cycle for read in reads for cycle in read.cycles]
    lines = [
        "# Count of the audit of the process",
        "",
        "Written by `process-audit/audit_count.py`. A cycle is named by its repository and *Record*, "
        "the commit that adds the first copy of its record; *Later copies* are the commits that "
        "add it again after a correction, and the values are read from the last copy. *Process "
        "pin* is the version of the-way the cycle ran on, *Remarks* the number of its process "
        "remarks, and the times are h:mm:ss from the copy's `stages.md`. `unknown` is a value the "
        "copy does not give, never zero; *Unknown values* says why. A cycle of the-way whose own "
        "change changed the tool that wrote a file of its copy has the values of that file "
        "`unknown` for that reason (WAY-339), and stands in the version it ran on.",
        "",
        "## Repositories",
        "",
        "| Repository | Cycles | Read |",
        "|---|---|---|",
    ]
    for read in reads:
        if read.error:
            state = "no: " + read.error
        else:
            state = "yes, a shallow clone whose history may lack cycles" if read.shallow else "yes"
        lines.append(f"| {cell(read.key)} | {len(read.cycles)} | {cell(state)} |")
    lines += [
        "",
        "## Cycles",
        "",
        "| Repository | Record | Committed | Folder | Later copies | Process pin | Remarks "
        "| Working time without waiting for tools | Waiting for tools |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for cycle in cycles:
        lines.append(
            f"| {cell(cycle.repository)} | {cycle.record} | {cycle.committed} | {cell(cycle.folder)} "
            f"| {' · '.join(cycle.later) or 'none'} | {cycle.pin or UNKNOWN} "
            f"| {UNKNOWN if cycle.remarks is None else cycle.remarks} | {duration(cycle.working)} "
            f"| {duration(cycle.waiting)} |")
    lines += [
        "",
        "## Cost",
        "",
        f"Prices of the list dated {prices.date}: a cost belongs to that series only, and a new "
        "list or a change of `task-cycle/cycle_stages.py` starts a new one (WAY-339). A stretch of "
        "the orchestrator with no token usage costs nothing. A stage report whose section of "
        "stages has the columns *Cache write (5 minutes)* and *Cache write (1 hour)* is priced "
        "with each of them at its own price; an earlier form "
        "has its cache writes inside its input and prices them as input, an approximation. "
        "A cycle whose stage report has no section of stages is priced from its table of "
        "tokens by model at the same prices, and its share of the cost in fix rounds is unknown. "
        "*Fix rounds* is the number of findings files the record's *Review rounds* "
        "names; *Share of the cost in fix rounds* is the cost of the subagent turns given one of "
        "those findings files — each fix and the review of that fix — over the cycle's cost. "
        "`unknown` has its reason in *Unknown values*.",
        "",
        "| Repository | Record | Price list | Cost (USD) | Fix rounds "
        "| Share of the cost in fix rounds |",
        "|---|---|---|---|---|---|",
    ]
    for cycle in cycles:
        lines.append(
            f"| {cell(cycle.repository)} | {cycle.record} | {cell(prices.date)} "
            f"| {money(cycle.cost)} | {UNKNOWN if cycle.rounds is None else cycle.rounds} "
            f"| {share_text(cycle.share)} |")
    lines += ["", *measures_lines(cycles), "", *gate_lines(cycles), "", *versions_lines(versions),
              "", *measure_versions_lines(measured), ""]
    lines += [
        "## Problems by cycle",
        "",
        "The problems of the register by class and weight, each problem once; a cycle "
        "with no problem has one row, `none`. *Refused rows* are rows of *Problems* that name this "
        "cycle and were refused for a class, weight, cost of an occurrence or issue the register "
        "lacks; a count with one reads `at least n`, as the refused row is not in it. A count "
        "reads `at least n` also where a problem names as its *Record* a commit that adds the "
        "records of more than one cycle: it counts in none of them. Problems whose cycle no named repository holds, or "
        "whose *Record* names more than one cycle, are in *Unknown values*.",
        "",
    ]
    lines += table(["Repository", "Record", "Class", "No problem", "Minor", "Important",
                    "Critical", "Refused rows"], analysis.cycle_rows)
    lines += [
        "",
        "## Fixed issues",
        "",
        "A fixed issue's problems count apart by whether the *Process pin* of their cycle holds "
        "the fix, by the commit and never by date. `unknown` where the fix is not in the "
        "checkout of the-way, and the reasons are in *Unknown values*. *Refused rows* are refused "
        "rows of *Problems* that name this issue; a count with one reads `at least n`.",
        "",
    ]
    lines += table(["Issue", "Fix", "Problems in cycles whose pin holds the fix",
                    "Problems in cycles whose pin lacks it", "Problems with an unknown pin",
                    "Problems whose cycle is not read", "Refused rows"], analysis.fixed_rows)
    lines += [
        "",
        "## Open issues",
        "",
        "*Cycles its problems came back in* counts the cycles in which a problem of the issue "
        "stands, except the first of them, where it stood and did not come back: `0` where it "
        "stands in one cycle only. It reads `at least n` where refused rows of the issue or "
        "problems of a cycle that is not read may belong to cycles not counted. *Days waiting* "
        "counts from the earliest commit date of the copies its problems' *Record* names to the "
        "day of the run; `—` where the issue has no problem yet. A count of problems with refused "
        "rows of the issue reads `at least n`. The issues are in the order of the register, never "
        "ranked by their counts, and the weighing is the human's.",
        "",
    ]
    lines += table(["Issue", "Cycles its problems came back in", "Problems",
                    "Problems whose cycle is not read", "Days waiting", "Refused rows"],
                   analysis.open_rows)
    lines += [
        "",
        "## Dropped issues",
        "",
        "A dropped issue's problems are counted apart; it has no waiting. A count with refused "
        "rows of the issue reads `at least n`.",
        "",
    ]
    lines += table(["Issue", "Cycles", "Problems", "Problems whose cycle is not read",
                    "Refused rows"], analysis.dropped_rows)
    lines += [
        "",
        "## Cost of an occurrence by issue",
        "",
        "For each issue, whatever its fate, how many of its problems stand on each level of the cost "
        "of an occurrence: the highest level that the actual cost of one occurrence reached, the "
        "levels running from the cheapest to the dearest as the columns do; the meaning of each is "
        "in the register's table *Costs of an occurrence*. This is no cost of a cycle, which the "
        "section *Cost* gives in money. A problem counts by its row, whether or not its cycle is "
        "read. *Refused rows* are refused rows of *Problems* that name this issue; a count with one "
        "reads `at least n`. The issues are in the order of the register, never ranked by their "
        "costs, and the weighing is the human's.",
        "",
    ]
    lines += table(["Issue", "Fate", *COST_LEVELS, "Refused rows"], analysis.cost_rows)
    lines += [
        "",
        "## Unknown values",
        "",
        "The values the count did not establish, one row for each field and reason, with how many "
        "values the pair has and its first three examples, each as repository, record and value. "
        "The result keeps the number and three examples of each pair, and no option of the count "
        "lists the rest. The full list of a pair's values stands where they are read: the "
        "register's own values (its refused rows and the problems of a cycle it names) in the "
        "register; the cycles' values in the copies of the cycles' records in the history of git. "
        "The values about an issue or a version are made by the count from the register and from "
        "those copies, and have no list of their own.",
        "",
    ]
    entries = [(cycle.repository, cycle.record, value, why)
               for cycle in cycles for value, why in cycle.unknown]
    entries += dict.fromkeys(analysis.unknown + versions.unknown + measured.unknown)
    entries += analysis.held
    lines += table(UNKNOWN_HEADER, unknown_rows(entries))
    return "\n".join(lines) + "\n"


def write(folder: Path, name: str, text: str) -> None:
    target = folder / name
    temporary = folder / f".{name}.tmp"
    try:
        with open(temporary, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        os.replace(temporary, target)
    except OSError as error:
        raise AuditCountError(f"cannot write {name} in the directory of the entry "
                              f"`{RESULTS_ENTRY}` under `{THE_WAY}`: "
                              f"{display(error.strerror or error)}") from None


def day_of(text: str) -> date:
    """A day written YYYY-MM-DD, for `--today`."""
    if DATE_TEXT.fullmatch(text) is None:
        raise argparse.ArgumentTypeError("the day is not written YYYY-MM-DD")
    try:
        return date.fromisoformat(text)
    except ValueError:
        raise argparse.ArgumentTypeError("the day is no date") from None


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = Parser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--locations", default=DEFAULT_LOCATIONS, metavar="FILE")
    parser.add_argument("--repository", action="append", default=[], metavar="KEY")
    parser.add_argument("--prices", default=str(PRICES), metavar="FILE")
    parser.add_argument("--today", type=day_of, default=None, metavar="YYYY-MM-DD")
    try:
        args = parser.parse_args(argv)
        today = args.today if args.today is not None else datetime.now(timezone.utc).date()
        locations = read_locations(args.locations)
        register_path = entry_path(locations, THE_WAY, REGISTER_ENTRY, "file")
        results = entry_path(locations, THE_WAY, RESULTS_ENTRY, "directory")
        named = repositories(locations, args.repository)
        the_way = the_way_checkout(locations)
        # No repository holds the results, the-way's included, whether this run reads it or not.
        for key, path in [*named.items(), (THE_WAY, the_way)]:
            if inside(results, path):
                raise AuditCountError(f"the directory of the entry `{RESULTS_ENTRY}` under "
                                      f"`{THE_WAY}` lies inside the repository "
                                      f"`{display(key)}`; the result is never written into a "
                                      f"repository")
        prices = read_prices(args.prices)
        register = read_register(register_path)
        ancestry = Ancestry(Git(the_way))
        reads = [read_repository(key, path, prices) for key, path in named.items()]
        note_changed_tools(reads, ancestry)
        analysis = analyse(reads, register, ancestry, today)
        versions = process_versions(reads, register, ancestry, prices)
        measured = measure_versions(versions, ancestry)
        text = render(reads, prices, analysis, versions, measured)
        dated = f"count-{today.isoformat()}.md"
        write(results, dated, text)
        write(results, LATEST, text)
    except AuditCountError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    failed = [read for read in reads if read.error]
    for read in failed:
        print(f"Error: repository `{display(read.key)}`: {read.error}", file=sys.stderr)
    for why in register.errors:
        print(f"Error: the register of problems: {display(why)}", file=sys.stderr)
    # A field a copy's `stages.md` lacks is no reason to withhold the result (WAY-344): each is
    # named here after the result is written. The folder is text of the history, so it is cut.
    lacking = [(read, cycle, missing_reason(name)) for read in reads for cycle in read.cycles
               for name in cycle.missing]
    # The fields of mechanism_measures.md and gate_times.md are named the same way.
    lacking += [(read, cycle, missing_reason(name, file)) for read in reads
                for cycle in read.cycles for file, name in cycle.missing_in]
    for read, cycle, reason in lacking:
        print(f"Error: repository `{display(read.key[:TEXT_CAP])}`: cycle "
              f"`{display(cycle.folder[:TEXT_CAP])}`: {reason}", file=sys.stderr)
    count = sum(len(read.cycles) for read in reads)
    print(f"Wrote {dated} and {LATEST}: {count} cycles in {len(reads) - len(failed)} of "
          f"{len(reads)} repositories.")
    return 1 if failed or register.errors or lacking else 0


if __name__ == "__main__":
    sys.exit(main())
