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

The places it needs are keys of the user's locations file (WAY-320), read as
`project-level/backlog_place.md` reads a key; FILE defaults to `~/.the-way/locations.json`:

- under the key `the-way`, the key `problem_register`, the file of the register of problems
  (`process-audit/problem_register.md` is its template), and the key `audit_results`, the
  directory where the result is written;
- under the key of each repository whose cycles it reads — the name of a product, as the
  register's *Repository* column gives it — the key `repository`, the path of that product's
  checkout. Each `--repository KEY` names a repository to read; without one, it reads every
  repository key that holds a key `repository`. The-way's own checkout is the key `repository` under
  `the-way`, and where that key is missing, the checkout this script lies in.
  The command finds every place it needs by itself, since it runs with no human present, and the
  session that reads its result finds the same places by the same names.

A path is absolute or starts with `~`. Where the file, a key or the path a key holds
is missing, or a key's value is not a path, the command writes nothing and names it in an
`Error:` line on stderr, so that the skill of the audit asks the human; it never asks itself.

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
- *Remarks*: the number of sub-items under the record's item `Process remarks on the-way`, `0`
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
  The cache writes are inside *Input* (`task-cycle/stage_transcripts.py`, which
  `task-cycle/cycle_stages.py` imports, folds them in). In the form
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
  round by that path: one sub-item for each round under the item, opening with the word `findings`
  and the path between backticks (`task-cycle/record_template.md`). A
  sub-item of a review that passed
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
- `task-cycle/cycle_stages.py` and the module `task-cycle/stage_transcripts.py` that it imports,
  the two files of the script that measures the cost, and no other script
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
words of a reviewer's remarks or from the text of an item (WAY-404, WAY-405). It is yes where a
sub-item of *Review rounds* opens with the path of its findings file and
`, contradiction yes`, or the
item *Discarded attempt* opens with `reason: ` and the marker `open design choice` in backticks, or
any of its sub-items does, where a cycle that discarded more than one attempt writes one sub-item for each
(the markers are `open design choice`, `reserved choice` and `size`, and only the start of the item,
or of the first line of each sub-item, is read; the sub-items are read only
as a list: nothing stands
beside the colon, the first line under the item is a sub-item at the indent
of the others and no plain
line stands at that indent or less; any other lines under the item are the details of one attempt,
read for a second `reason: ` followed by a backtick alone, whatever word stands there; a line at
the left margin ends the item). It is no where
every sub-item of *Review rounds* gives its mark, `contradiction no` or the form
of a review that passed with no fix, and *Discarded attempt* reads `none` or opens with the marker
`reserved choice` or `size` (each of its sub-items does, where it holds
several). Each yes stands over
the unknown that the other item gives, but the mark of a sub-item is read only where *Review rounds*
is held once and in its form (no sub-item in neither form, no findings file named twice, nothing
beside its colon), and the marker only where *Discarded attempt* is held once. It is unknown,
with the one reason `the sub-item of a round does not say whether there was a contradiction` for a
round of any record, older or newer, where a fix round's sub-item carries no mark; with its own reason where *Discarded attempt* opens with no marker and does
not read `none`, where its lines are no sub-items at one indent alone or text stands beside its
colon and the whole text, which does not read `none`, holds a second `reason: ` followed by a
backtick or opens with no marker, where it is missing or doubled, or where *Review rounds* is
missing, doubled or in neither form. Q2, more than one third of the slices of the plans came
back too large: from the item
*Plan* (`none` on the one-author route leaves the cycle out; otherwise the figure written just
before the word `slices`, as in `8 slices`, and where there is none or more than one, unknown)
and the sub-items of *Slices returned too large* (`none` is 0); the answer is yes where three times
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
`task-cycle/spec`, nor one of `task-cycle/agent-types/the-way-stage.md`,
`task-cycle/cycle_stages.py` or `task-cycle/stage_transcripts.py`, and neither script splits a
series of the cost. The section
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
start the series of what they measure: `task-cycle/cycle_stages.py` and the module
`task-cycle/stage_transcripts.py` that it imports for the times, the cost and the
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
checkout of the-way (the key `repository` under `the-way`, or this checkout), a pin written as a
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
when an argument is wrong, the locations file, the price list, the register or a key it needs is
missing or wrong, the register lacks a heading, a table or a column it needs, the register is
larger than 4 MiB or not UTF-8, the result directory lies inside a repository to read or the
checkout of the-way, or the result cannot be written.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path

sys.dont_write_bytecode = True
from stage_pricing import (  # noqa: E402  the price of a stage's rows, in the directory of this file
    NO_MODEL,
    TEXT_CAP,
    UNKNOWN,
    ModelPrice,
    Prices,
)
from record_reading import (  # noqa: E402  the reading of a cycle's record, in the directory of this file
    GATE_FILE,
    MAX_BYTES,
    MEASURES_FILE,
    RECORDS,
    THE_WAY,
    WRITE_1H_COLUMN,
    WRITE_5M_COLUMN,
    AuditCountError,
    Cycle,
    Git,
    GitError,
    Read,
    add_cost,
    guarded_optional,
    has_line,
    header_fields,
    is_separator,
    missing_line,
    missing_reason,
    process_pin,
    process_questions,
    read_file,
    read_gate,
    read_measures,
    remarks_count,
    stages_time,
    table_cells,
    tree_entries,
)
from problem_register import (  # noqa: E402  the register of problems, in the directory of this file
    DATE_TEXT,
    read_register,
)
from version_analysis import (  # noqa: E402  the analysis of the versions, in the directory of this file
    STAGES_FILE,
    STAGES_VALUES,
    WAITING_NAME,
    WORKING_NAME,
    Ancestry,
    analyse,
    committed_date,
    measure_versions,
    note_changed_tools,
    process_versions,
)
from audit_report import (  # noqa: E402  the writing of the result, in the directory of this file
    RESULTS_ENTRY,
    render,
    write,
)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-cycle"))
import remarks_check  # noqa: E402  the cutting of a record's lines, shared with its check

display = remarks_check.display

DEFAULT_LOCATIONS = "~/.the-way/locations.json"
REGISTER_ENTRY = "problem_register"
REPOSITORY_ENTRY = "repository"
# The checkout of the-way this script lies in, used where `the-way` has no key `repository`.
OWN_CHECKOUT = Path(__file__).resolve().parent.parent
# The price list of this part, read as a file of the-way (`--prices` names another one).
PRICES = Path(__file__).resolve().parent / "price_list.md"

RECORD_PATHSPEC = ":(glob)docs/task-cycles/*/cycle.md"
LATEST = "count-latest.md"
WORKING_LINE = "- Working time without waiting for tools:"
WAITING_LINE = "- Waiting for tools:"
PRICE_HEADING = "List date"
PRICE_MODEL = "Model id in stages.md"
PRICE_COLUMNS = ("Input", "Cached input", "Output", WRITE_5M_COLUMN, WRITE_1H_COLUMN)
PRICE = re.compile(r"[0-9]{1,6}(?:\.[0-9]{1,6})?")
TURN_SUFFIX = re.compile(r" — turn [0-9]{1,6}$")
# The locations file and the price list are named by their options in an error, never by their
# path, which is the user's (WAY-320).
LOCATIONS_LABEL = "the locations file (`--locations`)"
PRICES_LABEL = "the price list (`--prices`)"


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # type: ignore[override]
        raise AuditCountError(message)


# The locations file


def read_locations(name: str) -> dict:
    """The locations file as a JSON object; a key written twice is an error, since
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
                raise AuditCountError(
                    f"{label} holds the key `{display(key[:TEXT_CAP])}` twice in one object"
                )
            seen[key] = value
        return seen

    try:
        data = json.loads(text, object_pairs_hook=unique)
    except json.JSONDecodeError as error:
        raise AuditCountError(
            f"{label} is not JSON: line {error.lineno}, column {error.colno}"
        ) from None
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
        raise AuditCountError(
            f"the key `{display(key)}` of the locations file is not a JSON object"
        )
    return value


def entry_path(locations: dict, key: str, entry: str, kind: str) -> Path:
    """The path the key `entry` under `key` holds, which must exist as a `kind`: "file" or
    "directory". The path itself is never printed: an error names the key (WAY-320)."""
    where = f"the key `{display(entry)}` under `{display(key)}`"
    entries = key_object(locations, key)
    if entry not in entries:
        raise AuditCountError(
            f"the locations file holds no key `{display(entry)}` under `{display(key)}`"
        )
    value = entries[entry]
    if not isinstance(value, str) or not value.strip():
        raise AuditCountError(f"{where} of the locations file is not a path written as a string")
    try:
        path = Path(value).expanduser()
        if not path.is_absolute():
            raise AuditCountError(
                f"{where} of the locations file is not an absolute path or a path from `~`"
            )
        exists = path.is_dir() if kind == "directory" else path.is_file()
    except OSError, ValueError, RuntimeError:
        exists = False
    if not exists:
        raise AuditCountError(f"the path of {where} of the locations file is no existing {kind}")
    return path


def the_way_checkout(locations: dict) -> Path:
    """The checkout of the-way: the key `repository` under `the-way`, or this script's own."""
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
        raise AuditCountError(
            "no repository named in the locations file holds a key "
            "`repository`; add one or name a repository with --repository"
        )
    return dict(sorted(found.items()))


def inside(path: Path, folder: Path) -> bool:
    child = os.path.normcase(os.path.abspath(os.path.realpath(path)))
    parent = os.path.normcase(os.path.abspath(os.path.realpath(folder)))
    return child == parent or child.startswith(parent.rstrip(os.sep) + os.sep)


# The price list


def read_prices(name: str) -> Prices:
    """The price list, read as a file of the-way: a missing or wrong list stops the run with
    nothing written, as a wrong key of the locations file does."""
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
        raise AuditCountError(
            f"{label} "
            + (
                "holds the line `List date` more than once"
                if dates
                else "holds no line `List date`"
            )
        )
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
                    raise AuditCountError(
                        f"a table of {label} lacks the column {', '.join(lacking)}"
                    )
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
                raise AuditCountError(
                    f"a price of model `{display(model[:TEXT_CAP])}` in {label} "
                    "is neither a number nor `—`"
                )
        # A `—` in *Input*, *Cached input* or *Output* is a model with no price at all; one in a
        # write column leaves only that lifetime with no price.
        table[model] = (
            None
            if any(number is None for number in numbers[:3])
            else ModelPrice(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])
        )
    if not table:
        raise AuditCountError(f"{label} names no model")
    return Prices(dates[0], table)


# Reading a cycle


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
        measures, gate = (
            guarded_optional(git, entries, prefix, name) for name in (MEASURES_FILE, GATE_FILE)
        )
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
    cycle.held = {
        name
        for name, text in (
            (STAGES_FILE, stages),
            (MEASURES_FILE, measures[0]),
            (GATE_FILE, gate[0]),
        )
        if text is not None
    }
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
    cycle.working, reason = stages_time(
        lines, fenced, WORKING_LINE, "working time without waiting for tools"
    )
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


def read_repository(key: str, path: Path, prices: Prices) -> Read:
    """The cycles whose records the history of one repository holds."""
    result = Read(key)
    git = Git(path)
    try:
        git.run("rev-parse", "--git-dir")
        result.shallow = git.run("rev-parse", "--is-shallow-repository").strip() == b"true"
        listed = git.run(
            "log",
            "--full-history",
            "--branches",
            "--remotes",
            "--diff-filter=A",
            "--no-renames",
            "--topo-order",
            "--reverse",
            "--format=%H %ct",
            "--",
            RECORD_PATHSPEC,
        ).decode("ascii")
        copies: dict[bytes, list[tuple[str, str]]] = {}
        for line in listed.splitlines():
            commit, _, stamp = line.partition(" ")
            added = git.run(
                "diff-tree",
                "--root",
                "--no-commit-id",
                "-r",
                "-z",
                "--no-renames",
                "--diff-filter=A",
                "--name-only",
                commit,
                "--",
                RECORD_PATHSPEC,
            )
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
        cycle = Cycle(
            key,
            display(folder.decode("utf-8", errors="replace")),
            first,
            committed or UNKNOWN,
            [commit for commit, _ in commits[1:]],
            {commit: committed_date(when) or UNKNOWN for commit, when in commits},
        )
        if committed is None:
            cycle.unknown.append(
                ("Committed", "the commit's date lies outside the years the command can read")
            )
        fill(cycle, git, commits[-1][0], folder, key == THE_WAY, prices)
        result.cycles.append(cycle)
    result.cycles.sort(key=lambda cycle: (cycle.committed, cycle.folder, cycle.record))
    return result


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
                raise AuditCountError(
                    f"the directory of the key `{RESULTS_ENTRY}` under "
                    f"`{THE_WAY}` lies inside the repository "
                    f"`{display(key)}`; the result is never written into a "
                    f"repository"
                )
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
    lacking = [
        (read, cycle, missing_reason(name))
        for read in reads
        for cycle in read.cycles
        for name in cycle.missing
    ]
    # The fields of mechanism_measures.md and gate_times.md are named the same way.
    lacking += [
        (read, cycle, missing_reason(name, file))
        for read in reads
        for cycle in read.cycles
        for file, name in cycle.missing_in
    ]
    for read, cycle, reason in lacking:
        print(
            f"Error: repository `{display(read.key[:TEXT_CAP])}`: cycle "
            f"`{display(cycle.folder[:TEXT_CAP])}`: {reason}",
            file=sys.stderr,
        )
    count = sum(len(read.cycles) for read in reads)
    print(
        f"Wrote {dated} and {LATEST}: {count} cycles in {len(reads) - len(failed)} of "
        f"{len(reads)} repositories."
    )
    return 1 if failed or register.errors or lacking else 0


if __name__ == "__main__":
    sys.exit(main())
