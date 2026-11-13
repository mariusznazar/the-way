---
name: audit-process
description: Use when the weekly audit of the process has to be led with the human — the weekly task of the backlog starts it, or the human asks for it — reading the latest result of the counting command, putting before the human what came back after a fix, what still waits and what each version of the process shows, and writing the audit's result into the user's place outside every repository.
---

# Audit the process

Leads the weekly audit of the process with a human, in one session of its own, apart from any
weekly review (WAY-341). It reads the latest result of the counting command, `audit_count.py` beside
this file, puts before the human the matters to weigh, and writes down what the human decided to
weigh and what the human set aside. It changes nothing in any repository; in the register of problems
it changes nothing but the list of classes, which it widens on the human's yes (step 3). A matter the
human takes into work becomes a task through the human's own backlog, not through this session.

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
  Saturday, and the session finds its result ready (WAY-341).
- **The weekly task.** A task the human keeps in the backlog, once a week, starts the session
  (WAY-341).
- Setting up the scheduler and adding the weekly task are human actions (WAY-140). Where either is
  missing, say so to the human and do neither.

## Rules of working

These hold at every step.

- **How often an issue comes back is material, never a priority** (WAY-336). An issue is the one
  matter that like problems of several cycles make. Give no issue a priority, an order of urgency or
  a recommended rank from how often it returned or how long it has waited, and list issues in the
  order the count gives, which is the register's. The human weighs what a return costs and what its
  fix costs.
- **The cost of an occurrence is material, never a priority** (WAY-346, WAY-336). It is the level,
  on the five of the register's table *Costs of an occurrence*, that one occurrence of a problem
  cost: `nothing`, `steps`, `stage`, `round` or `human`, each dearer than the one before. It is no
  cost of a cycle, which *Cost* gives in money, and no weight, which says how far a problem
  endangered the change. Show it beside an issue and leave it to the human to set it against what
  the issue's returns number and what its fix costs. Give no issue a priority, an order or a rank
  from it, and add the levels into no score.
- **Measures are compared inside a series only** (WAY-339). A new series of the cost begins at a new
  price list, or at a change of the form of a stage report, of the list of classes or of the
  instructions of the reviewer. The count splits more often than that: at a new price list, at a
  date of the register's list of classes, and at any change of the files of the-way under
  `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` and `task-cycle/spec` or of
  `task-cycle/cycle_stages.py`, whatever the change, so that it compares less and never across a
  change WAY-339 names. The mechanism measures (the numbers of how each cycle's agents use context
  and the prompt cache, from the cycle's `mechanism_measures.md`) and the gate times (the time of
  each run of the product's gate, from `gate_times.md`) have series of their own (WAY-348, WAY-350):
  a new series of them begins only at a change of the script that measures them,
  `task-cycle/cycle_measures.py` or `task-cycle/gate_times.py`. A change of the instructions of the
  cycle, of the reviewer or of the author starts none of them, and neither does a new price list.
  Set no number of one series beside a number of another, no number of the measures or the gate
  times beside a number of the cost, and no week's count beside the week before; a version of the
  process is judged by the cycles that ran on it.
- **No frozen earlier tasks are replayed on an old and a new version** (WAY-340). Where the human
  asks for such a comparison, say that the audit holds no such set and judges a version by its own
  cycles.
- **Whether a fix works is read from the version, never from the date** (WAY-335): the count sets the
  problems of the cycles whose version of the-way holds the fix apart from those of the cycles whose
  version lacks it. Do not set problems before a fix's date against problems after it.
- **`unknown` stays `unknown`, and `at least n` stays `at least n`.** Do not read either as zero or
  as `n`, and do not fill a value from another source. A `—` in *Days waiting* means the issue has no
  problem yet.
- **The results lie outside every repository** (WAY-332). Write the audit's result nowhere else, and
  write no path an entry of the locations file holds, nor its content, into a file of a repository
  or a report: name the entry (WAY-320).

## 1. Find the places

Read `project-level/backlog_place.md`, the section "Resolve an entry of the locations file", and
resolve in `~/.the-way/locations.json` the entries the counting needs:

- under `the-way`: `problem_register`, the file of the register, and `audit_results`, the directory
  where the results lie;
- under the key of each product whose cycles the audit reads: `repository`, the path of that
  product's checkout. Under `the-way` the entry `repository` is the checkout of the-way, which holds
  the-way's own cycles and the history the process versions are read from.

Where the file, a key, an entry or the path an entry holds is missing, ask the human where the place
is, in one question: the ways open, what each costs, and a recommendation (WAY-113). The ways are
usually to name the place, to create it, or, for the register, to copy the template to a place the
human names. Offer to add the entry to the file, create the file or the key where they are missing,
and write only on the human's yes.

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
earlier note `audit-<YYYY-MM-DD>.md`, if there is one, only to see which matters the human weighed or
set aside; say so beside a matter that comes again.

Take the matters one at a time, in this order, and wait for the human's word on each before the
next. Show each as the rows of the count quoted word for word with the header row of their table,
then what follows from them and what does not, then one question that the rows shown answer. These
are questions of assessment, so they stay open and carry no recommendation. A matter ends in one of
two outcomes: the human weighs it further, or sets it aside.

1. **What the count could not read.** The *Repositories* table: any repository read `no`, a shallow
   clone whose history may lack cycles, a repository the human expected that is missing. Then the
   kinds of `unknown` in *Unknown values* and how many cycles each touches, and any *Refused rows*.
   A row refused for its class — its row in *Unknown values* names row `<n>` of *Problems* and gives
   the reason `the class is not in the list of classes` — is the matter of a class the list lacks,
   below; the user's own tool corrects any other refused row in the register. An archive of earlier
   cycles gives
   `unknown` often: a record with no item *Process remarks on the-way* gives no remarks; a
   `stages.md` without the working-time lines gives no times, as an earlier form does; a `stages.md`
   with neither the section of tokens by model nor the earlier form's table of tokens by model gives
   no cost, and an earlier form with that table gives the cost from it. The share of the cost in fix
   rounds is `unknown` where the record's *Review rounds* is not in the form
   `task-cycle/record_template.md` gives, or `stages.md` has no column *Files named*, which the
   earlier form lacks.
   That is the state of those records, and no defect of the count.
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
   with the line that says why it begins where it does: the median cost at constant prices of each
   version and its answers Q1, Q2 and Q3, which `yes`, `no` or `unknown` give inside that series. Quote
   the cycles of a version from *Cost*, with their share of the cost in fix rounds, where the human
   wants them. Name together, in one matter, the series whose rows give nothing but `unknown`, and
   the cycles in *No version*, with the reasons *Unknown values* gives.
   The series of *Measure versions* follow in the same matter, the mechanism measures and the gate
   times each apart, one series at a time, each with the line that says why it begins where it
   does. For each series, quote the rows of its table with the table's header row; then what follows
   from them and what does not; then one open question for the human that the rows answer, with no
   recommendation. The gate times of runs with another gate beside them are shown apart as the count
   shows them, and are never compared. A measure is material and never a priority, as the rules of
   working say of the other numbers.

**A class the list lacks.** Where a row refused for its class, or the human's own reading of a
problem, shows a problem that no class of the register's *Classes* fits, the list widens; the
problem is never given the nearest class instead (WAY-333). Read that row of the register, and put
before the human a new class: its name, lower-case letters, digits and hyphens, the refused row's
class where it is one; what it means; and the day of the session as the date it is added. On the
human's yes, add the row `| <name> | <meaning> | <YYYY-MM-DD> | none |` to *Classes* in the register
that the entry `problem_register` names, which lies in the user's place and never in a repository,
and change nothing else of it. Adding a class gives no problem a class (WAY-330): a problem's class
in *Problems* stays the user's tool's to write. The date starts a new series of the cost and of no
mechanism measure or gate time (WAY-339), and the next count reads the class; offer to run the count
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
- *Set aside*: each matter the human set aside, with the human's reason as said;
- *Not reached*: the matters not yet put before the human, where the session ended early;
- *Classes added*: each class the session added to the register, with its name, meaning and date;
- the corrections of the register the human named.

Where the human ends the session early, write the note with what was decided and the rest under
*Not reached*.
