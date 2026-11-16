---
name: audit-process
description: Use when the weekly audit of the process has to be led with the human — the weekly task of the backlog starts it, or the human asks for it — reading the latest result of the counting command, putting before the human what came back after a fix, what still waits and what each version of the process shows, and writing the audit's result into the user's place outside every repository.
---

# Audit the process

Leads the weekly audit of the process with a human, in one session of its own, apart from any
weekly review. A session of its own keeps the audit from sharing the time and the subject of the
weekly review, and a count made on the night before leaves its result ready when the session begins.
It reads the latest result of the counting command, `audit_count.py` beside this file, puts before
the human the matters to weigh, and writes down what the human decided to weigh, what the human
decided to change and what the human set aside. It changes nothing in any repository; in the
register of problems it changes nothing but the list of classes, which it widens on the human's yes
(step 3). A matter the human takes into work becomes a task through the human's own backlog, not
through this session.

This skill lives in `process-audit/` of the-way. In the-way itself, the-way is the checkout or
worktree the session works in, the directory `git rev-parse --show-toplevel` prints in the session's
working directory; in a product, it is the product's pinned `.the-way`. Every path below that starts
with `process-audit/` starts at that root, and the command runs from there.

## What the audit rests on

- **The register of problems.** The user's own tool fills it, from the template
  `process-audit/problem_register.md`, which the user copies to a place of their own and adapts to
  their needs. The audit gives no problem a class, a weight or a cost of an occurrence itself and
  reads the register that an entry of the locations file names (WAY-330).
- **The counting.** `python -B process-audit/audit_count.py` asks nothing and reads nothing from
  stdin, so a system scheduler can start it with no one present. It runs on the night from Friday to
  Saturday, and the session finds its result ready.
- **The weekly task.** A task the human keeps in the backlog, once a week, starts the session.
- Setting up the scheduler and adding the weekly task are human actions (WAY-140). Where either is
  missing, say so to the human and do neither.

## Rules of working

These hold at every step.

- **How often an issue comes back is material, never a priority**. An issue is the one
  matter that like problems of several cycles make. Give no issue a priority, an order of urgency or
  a recommended rank from how often it returned or how long it has waited, and list issues in the
  order the count gives, which is the register's. The human weighs what a return costs and what its
  fix costs.
- **The cost of an occurrence is material, never a priority**. It is the level,
  on the five of the register's table *Costs of an occurrence*, that one occurrence of a problem
  cost: `nothing`, `steps`, `stage`, `round` or `human`, each dearer than the one before. It is no
  cost of a cycle, which *Cost* gives in money, and no weight, which says how far a problem
  endangered the change. Show it beside an issue and leave it to the human to set it against what
  the issue's returns number and what its fix costs. Give no issue a priority, an order or a rank
  from it, and add the levels into no score.
- **Measures are compared inside a series only** (WAY-339). The versions of the process are cut into
  two kinds of series. A series of the cost, which holds the median cost and the answer Q3, begins
  at a new price list or at a change of `task-cycle/cycle_stages.py`, the script that measures the
  cost, and at no other change. A series of the count of remarks, which holds the answers Q1 and Q2,
  begins wherever a series of the cost begins, and also at a date of *Added* or *Withdrawn* in the
  register's list of classes, and at any change of the files of the-way under `task-cycle/change`,
  `task-cycle/plan`, `task-cycle/review` and `task-cycle/spec`, and of
  `task-cycle/agent-types/the-way-stage.md`, whose text the reviewer receives as its instruction,
  whatever the change, so that it compares less and never across a change WAY-339 names. The
  mechanism measures (the numbers of how each cycle's agents use context and the prompt cache, from
  the cycle's `mechanism_measures.md`) and the gate times (the time of each run of the product's
  gate, from `gate_times.md`) have series of their own (WAY-350): a new series of the mechanism
  measures begins only at a change of `task-cycle/cycle_measures.py`, and a new series of the gate
  times only at a change of `task-cycle/gate_times.py` or of `gate/run_tests.py`, the test runner
  whose output gives the time of each directory (WAY-339). The reason of a new series names the
  file or files that changed. A change of the instructions of the cycle, of the reviewer or of the
  author starts none of the mechanism measures or the gate times, and neither does a new price list.
  Set no number of one series beside a number of another, no number of the cost beside a number of
  the count of remarks, no number of the measures or the gate times beside a number of the cost, and
  no week's count beside the week before; a version of the process is judged by the cycles that ran
  on it.
- **No frozen earlier tasks are replayed on an old and a new version**. Where the human asks for
  such a comparison, say that the audit holds no such set and judges a version by its own cycles.
  Cycles run on every version in any case and each record names its version, so the audit has
  material about every version without a cycle made only to measure, and a replay would cost a
  cycle for each task and each version.
- **Whether a fix works is read from the version, never from the date**: the count sets the
  problems of the cycles whose version of the-way holds the fix apart from those of the cycles whose
  version lacks it. Do not set problems before a fix's date against problems after it. A cycle's
  record names the version of the-way the cycle ran on, so a cycle made after the date of a fix can
  still run on a version without it.
- **`unknown` stays `unknown`, and `at least n` stays `at least n`.** Do not read either as zero or
  as `n`, and do not fill a value from another source. A `—` in *Days waiting* means the issue has no
  problem yet.
- **The results lie outside every repository**. Write the audit's result nowhere else, and
  write no path an entry of the locations file holds, nor its content, into a file of a repository
  or a report: name the entry (WAY-320). The repository of the-way is public, and the results carry
  the names of products and the content of remarks from their cycles, which the history of a
  repository keeps after a later change removes them.

## 1. Find the places

Read `project-level/backlog_place.md`, the section "Resolve an entry of the locations file", and
resolve in `~/.the-way/locations.json` the entries the counting needs:

- under `the-way`: `problem_register`, the file of the register, and `audit_results`, the directory
  where the results lie;
- under the key of each product whose cycles the audit reads: `repository`, the path of that
  product's checkout. Under `the-way` the entry `repository` is the checkout of the-way, which holds
  the-way's own cycles and the history the process versions are read from.

Where the file, a key, an entry or the path an entry holds is missing, ask the human where the place
is, in one question of decision, as "How a skill asks" gives it (WAY-113). The ways are usually to
name the place, to create it, or, for the register, to copy the template to a place the human names.
Offer to add the entry to the file, create the file or the key where they are missing, and write
only on the human's yes.

## 2. Get the latest count

List the `audit_results` directory. It holds `count-<YYYY-MM-DD>.md`, one for each run, the day being
the day of the run in UTC; `count-latest.md`, a copy of the newest; and the notes
`audit-<YYYY-MM-DD>.md` of earlier sessions.

A newest count dated before the Friday of the last night from Friday to Saturday means no scheduler
started the counting (a run of that night is dated that Friday or the Saturday, as the clock of the
scheduler and UTC fall). Tell the human, and offer to run it now. The command writes the two count files into the
`audit_results` directory, replacing those of the same day, so run it on the human's yes:

```
python -B process-audit/audit_count.py [--locations FILE] [--repository KEY ...] [--prices FILE] [--today YYYY-MM-DD]
```

Without options it reads `~/.the-way/locations.json` and every key that holds an entry
`repository`; `--repository KEY`, repeated, names the repositories to read; `--prices` names another
price list than `process-audit/price_list.md`; `--today` is the day of the run, which the days of
waiting count to. Its exit code says:

- `0`: the result is written;
- `1`: the result is written, but a repository could not be read, a table of the register is
  refused as a whole, or a cycle's copy lacks a field its files need. The `Error:` lines on stderr
  and the result's sections *Repositories* and *Unknown values* name which. A copy's missing field
  gives one `Error:` line that names the repository, the cycle's folder, the file of the copy
  (`stages.md`, `mechanism_measures.md` or `gate_times.md`) and the field it lacks; *Unknown values*
  names the same file and field beside the values it leaves unknown. Put it before the human at
  step 3 as the first matter;
- `2`: an `Error:` line on stderr and nothing written; the line names the file, key, entry or
  argument that is missing or wrong, never a path. A register that lacks a heading, a table or a
  column the count needs, such as a register kept in an earlier form of the template, ends here with
  the line naming each field missing: it is for the user's own tool to bring the register to the
  template's form, and the session changes nothing in it but a class on the human's yes. Ask the
  human as in step 1, or what to correct, and run again once it is.

Then read `count-latest.md` whole.

## 3. Put the matters before the human

The count has the sections *Repositories*, *Cycles*, *Cost*, *Mechanism measures*, *Gate runs*,
*Process versions*, *Measure versions*, *Problems by cycle*, *Fixed issues*, *Open issues*, *Dropped
issues*, *Cost of an occurrence by issue* and *Unknown values*. *Mechanism measures* gives each
cycle's values of how its agents use context and the prompt cache, and *Gate runs* each run of the
product's gate with its times; both are read from the cycles' records. *Measure versions* gives
their medians per version of the process and whether each falls against the version before, series
by series. Read the newest
earlier note `audit-<YYYY-MM-DD>.md`, if there is one, only to see which matters the human weighed,
decided on a step or set aside; say so beside a matter that comes again.

Take the matters one at a time, in this order, and wait for the human's word on each before the
next. Show each as the rows of the count quoted word for word with the header row of their table,
then what follows from them and what does not, then the question that the rows shown answer. Before
the question, name from the rows what they show as broken or out of date and a step can change — a
repository on an old version of the process, a count that did not succeed, an issue with no task —
and put each such thing as a question of decision, as "How a skill asks" gives it (WAY-113). The
recommendation rests on what the rows show as broken, never on how often the issue came back, how
long it has waited or the level of the cost of an occurrence; the rules of working on those two
stand as they are. Where the rows show nothing to change, say so in one sentence; the question that
the rows answer is then a question of assessment, open and with no recommendation. A matter ends in
one of three outcomes: the human weighs it further, decides on a step, or sets it aside.

1. **What the count could not read.** The *Repositories* table: any repository read `no`, a shallow
   clone whose history may lack cycles, a repository the human expected that is missing. Then the
   kinds of `unknown` in *Unknown values* and how many cycles each touches, and any *Refused rows*.
   *Unknown values* gives every value the count did not establish as one line for each field and
   reason, with how many values the pair has and its first three examples, and no option of the
   count lists the rest. The full list of a pair's values stands where they are read: the register's
   own values (its refused rows and the problems of a cycle it names) in the register, the cycles'
   values in the copies of their records in git history. The values about an issue or a version
   are made by the count from the register and from those copies, and have no list of their own.
   A row refused for its class is one such line, with the reason `the class is not in the list of
   classes` and its row of *Problems* among the first examples: it is the matter of a class the list
   lacks, below. The user's own tool corrects any other refused row in the register. An archive of
   earlier cycles gives `unknown` often: a record with no item *Process remarks on the-way* gives no
   remarks, and a record that lacks another line or item the count reads of it (the line `Process pin`
   or `Target branch and base`, the item *Discarded attempt*, *Review rounds*, *Plan* or *Slices
   returned too large*) gives `unknown` for the values that need it, with a reason that names it and
   no `Error:` line (WAY-344); a `stages.md` with neither of its two time lines gives no times, and no error, as an
   earlier form does; a `stages.md` with neither the section of tokens by model nor the earlier
   form's table of tokens by model gives no cost, and an earlier form with that table gives the cost
   from it. The forms of `stages.md` the count reads, each with what it lacks (WAY-344):
   (a) the older table of tokens by model, with no detailed section: its cost is given, its cache
   writes priced as input (an approximation), and the share of the cost in fix rounds `unknown`,
   since that table gives no turns;
   (b) the detailed section without the two time lines: the times `unknown`, no error;
   (c) the detailed section without the column *Files named*: the share of the cost in fix rounds
   `unknown`, no error;
   (d) the detailed section without the two columns of the cache writes: its cost is given, the
   writes priced as input (an approximation), and no value `unknown` for that reason;
   (e) the newer form, with all of them.
   A file with one of the two time lines and not the other, or with one of the two columns of the
   cache writes and not the other, is not a form but a missing field: the run ends with exit 1 and
   an `Error:` line that names the field. The share of the cost in fix rounds is `unknown` where the
   record's *Review rounds* is not in the form `task-cycle/record_template.md` gives, and in forms
   (a) and (c), which have no column *Files named*. A copy with no `mechanism_measures.md` or
   `gate_times.md` is an earlier cycle or one whose measuring script failed, and a copy with no
   `gate_times.md` is also a cycle whose final gate ran in CI, which no script of the cycle timed;
   the record's *Verification* says which. That is the state of those records, and no defect of the
   count. The gate times compare only the runs on the cycle's own system, which a cycle with its
   final gate in CI has fewer of or none.
2. **What came back after a fix.** Each issue of *Fixed issues*: its problems in the cycles whose
   *Process pin* holds the fix, apart from those in the cycles whose pin lacks it, and the columns for
   a pin that is unknown or a cycle that is not read. Beside each, quote its row of *Cost of an
   occurrence by issue* with the header row of that table: how many of its problems stand on each
   level of the cost of an occurrence.
3. **What still waits, and for how long.** Each issue of *Open issues*: the cycles its problems came
   back in (the first cycle where a problem stood does not count, so `0` is a problem seen once),
   its problems and its *Days waiting*. Add the issues of *Dropped issues* once,
   as the count gives them, with no waiting. Beside each issue, open or dropped, quote its row of
   *Cost of an occurrence by issue* with the header row of that table.
4. **What each version of the process shows.** For each series of *Process versions*, one at a time,
   with the line that says why it begins where it does. A series of the cost shows the median cost
   at constant prices of each version and its answer Q3; a series of the count of remarks shows its
   answers Q1 and Q2. Each answer is `yes`, `no` or `unknown` inside its series, and a number of one
   kind of series is never set beside a number of the other. Q1 asks whether a contradiction with the
   settlements came out only after the code was written, and the count reads it from two marks of the
   cycle's record, never from the text of a reviewer's remarks: `yes` where an entry of *Review
   rounds* says `contradiction yes` or *Discarded attempt*, held once by the record, gives the
   reason `open design choice` (in any of its entries, where it holds one for each discarded
   attempt); a `yes` stands over the `unknown` of any other part of the record, save that the reason
   does not stand over a doubled *Discarded attempt*, which only the mark of an entry does;
   `no` where every entry of *Review rounds* says `contradiction no` or is a review that passed with
   no fix, and *Discarded attempt* reads `none` or gives only the reasons `reserved choice` and
   `size`; `unknown` otherwise: where an entry of a round carries no mark, where *Review rounds* is
   missing, doubled or in neither form, or where *Discarded attempt* is missing, doubled or gives no
   reason (a text or an entry with no reason at its start, or a text of one attempt that holds a
   second `reason: ` followed by a backtick), which a record written before those marks stood in the
   template does wherever it holds such an entry or such a text. Quote
   the cycles of a version from *Cost*, with their share of the cost in fix rounds, where the human
   wants them. Name together, in one matter, the series whose rows give nothing but `unknown`, and
   the cycles in *No version*, with the reasons *Unknown values* gives.
   The series of *Measure versions* follow in the same matter, the mechanism measures and the gate
   times each apart, one series at a time, each with the line that says why it begins where it
   does. For each series, quote the rows of its table with the table's header row; then what follows
   from them and what does not; then one open question for the human that the rows answer, with a
   recommendation only where the rows show something broken that a step can change, as above. The
   gate times of runs not compared (those with another gate beside them or an
   unknown count, those that failed and those whose exit code is unknown) are shown apart as the
   count shows them, and are never compared (WAY-350). A version in which no cycle gives a value or
   no run a time has one row with `—` for the measure; name such versions together, with the reason
   *Unknown values* gives, and quote no row of them one by one. A measure is material and never a
   priority, as the rules of working say of the other numbers.

**A class the list lacks.** Where a row refused for its class, or the human's own reading of a
problem, shows a problem that no class of the register's *Classes* fits, the list widens; the
problem is never given the nearest class instead. Read that row of the register, and put
before the human a new class: its name, lower-case letters, digits and hyphens, the refused row's
class where it is one; what it means; and the day of the session as the date it is added. On the
human's yes, add the row `| <name> | <meaning> | <YYYY-MM-DD> | none |` to *Classes* in the register
that the entry `problem_register` names, which lies in the user's place and never in a repository,
and change nothing else of it. Adding a class gives no problem a class (WAY-330): a problem's class
in *Problems* stays the user's tool's to write. The date starts a new series of the count of remarks,
and of neither the cost nor any mechanism measure or gate time (WAY-339), and the next count reads
the class; offer to run the count
again as step 2 gives. Where the human says no, or names a class the list already holds, the
problem's row is a correction for the user's tool.

Where the register itself seems wrong to the human otherwise, such as a problem under another class
or an issue whose fate has changed, the correction is the user's own tool's to make: note it in the
result.

## 4. Write the result

Write the result as `audit-<YYYY-MM-DD>.md`, the day of the session, in the `audit_results`
directory beside the counts. Where a note of that day exists, read it and go on from the matters it
holds. Show the human its text first, and write it on the human's yes. It holds:

- the count it rests on, by its file name, and the repositories it read;
- *Weighed*: each matter the human weighs further — the issue's name, or the series and the version's
  commit — with the rows quoted as they were shown and the human's words about it;
- *Decided*: each matter at which the human decided on a step — the question of decision as it was
  put, the way the human chose and the human's words about it; the step is the human's to take,
  through the backlog, as a matter taken into work is;
- *Set aside*: each matter the human set aside, with the human's reason as said;
- *Not reached*: the matters not yet put before the human, where the session ended early;
- *Classes added*: each class the session added to the register, with its name, meaning and date;
- the corrections of the register the human named.

Where the human ends the session early, write the note with what was decided and the rest under
*Not reached*.
