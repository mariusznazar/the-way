---
name: audit-process
description: Use when the weekly audit of the process has to be led with the human — the weekly task of the backlog starts it, or the human asks for it — reading the latest result of the counting command, putting before the human what came back after a fix, what still waits and what each version of the process shows, and writing the audit's result into the user's place outside every repository.
---

# Audit the process

Leads the weekly audit of the process with a human, in one session of its own, apart from any
weekly review (WAY-340). It reads the latest result of the counting command, `audit_count.py` beside
this file, puts before the human the matters to weigh, and writes down what the human decided to
weigh and what the human set aside. It changes nothing in any repository and nothing in the register
of problems; a matter the human takes into work becomes a task through the human's own backlog, not
through this session.

This skill lives in `process-audit/` of the-way. In the-way itself, the-way is the checkout or
worktree the session works in, the directory `git rev-parse --show-toplevel` prints in the session's
working directory; in a product, it is the product's pinned `.the-way`. Every path below that starts
with `process-audit/` starts at that root, and the command runs from there.

## What the audit rests on

- **The register of problems.** The user's own tool fills it, from the template
  `process-audit/problem_register.md`, which the user copies to a place of their own and adapts to
  their needs. The audit gives no problem a class or a weight itself and reads the register that an
  entry of the locations file names (WAY-329).
- **The counting.** `python -B process-audit/audit_count.py` asks nothing and reads nothing from
  stdin, so a system scheduler can start it with no one present. It runs on the night from Friday to
  Saturday, and the session finds its result ready (WAY-340).
- **The weekly task.** A task the human keeps in the backlog, once a week, starts the session
  (WAY-340).
- Setting up the scheduler and adding the weekly task are human actions (WAY-140). Where either is
  missing, say so to the human and do neither.

## Rules of working

These hold at every step.

- **How often an issue comes back is material, never a priority** (WAY-335). An issue is the one
  matter that like problems of several cycles make. Give no issue a priority, an order of urgency or
  a recommended rank from how often it returned or how long it has waited, and list issues in the
  order the count gives, which is the register's. The human weighs what a return costs and what its
  fix costs.
- **Measures are compared inside a series only** (WAY-338). A series is a run of versions of the
  process between which the price list, the register's list of classes and the reviewed files of
  the-way did not change. Set no number of one series beside a number of another, and no week's count
  beside the week before; a version of the process is judged by the cycles that ran on it.
- **No frozen earlier tasks are replayed on an old and a new version** (WAY-339). Where the human
  asks for such a comparison, say that the audit holds no such set and judges a version by its own
  cycles.
- **Whether a fix works is read from the version, never from the date** (WAY-334): the count sets the
  problems of the cycles whose version of the-way holds the fix apart from those of the cycles whose
  version lacks it. Do not set problems before a fix's date against problems after it.
- **`unknown` stays `unknown`, and `at least n` stays `at least n`.** Do not read either as zero or
  as `n`, and do not fill a value from another source. A `—` in *Days waiting* means the issue has no
  problem yet.
- **The results lie outside every repository** (WAY-331). Write the audit's result nowhere else, and
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

A newest count older than the last night from Friday to Saturday means no scheduler started the
counting. Tell the human, and offer to run it now. The command writes the two count files into the
`audit_results` directory, replacing those of the same day, so run it on the human's yes:

```
python -B process-audit/audit_count.py [--locations FILE] [--repository KEY ...] [--prices FILE] [--today YYYY-MM-DD]
```

Without options it reads `~/.the-way/locations.json` and every key that holds an entry
`repository`; `--repository KEY`, repeated, names the repositories to read; `--prices` names another
price list than `process-audit/price_list.md`; `--today` is the day of the run, which the days of
waiting count to. Its exit code says:

- `0`: the result is written;
- `1`: the result is written, but a repository could not be read or a table of the register is
  missing; the `Error:` lines on stderr and the result's sections *Repositories* and *Unknown values*
  name which. Put it before the human at step 3 as the first matter;
- `2`: an `Error:` line on stderr and nothing written; the line names the file, key, entry or
  argument that is missing or wrong, never a path. Ask the human as in step 1, or what to correct,
  and run again once it is.

Then read `count-latest.md` whole.

## 3. Put the matters before the human

The count has the sections *Repositories*, *Cycles*, *Cost*, *Process versions*, *Problems by
cycle*, *Fixed issues*, *Open issues*, *Dropped issues* and *Unknown values*. Read the newest
earlier note `audit-<YYYY-MM-DD>.md`, if there is one, only to see which matters the human weighed or
set aside; say so beside a matter that comes again.

Take the matters one at a time, in this order, and wait for the human's word on each before the
next. Show each as the rows of the count quoted word for word with the header row of their table,
then what follows from them and what does not, then one question that the rows shown answer. These
are questions of assessment, so they stay open and carry no recommendation. A matter ends in one of
two outcomes: the human weighs it further, or sets it aside.

1. **What the count could not read.** The *Repositories* table: any repository read `no`, a shallow
   clone whose history may lack cycles, a repository the human expected that is missing. Then the
   kinds of `unknown` in *Unknown values* and how many cycles each touches, and any *Refused rows*,
   which the user's own tool corrects in the register. An archive of earlier cycles gives
   `unknown` often: a record with no item *Process remarks on the-way* gives no remarks; a
   `stages.md` without the working-time lines or the section of tokens by model gives no times and no
   cost; the share of the cost in fix rounds is `unknown` where the record's *Review rounds* is not
   in the form `task-cycle/record_template.md` gives, or `stages.md` has no column *Files named*.
   That is the state of those records, and no defect of the count.
2. **What came back after a fix.** Each issue of *Fixed issues*: its problems in the cycles whose
   *Process pin* holds the fix, apart from those in the cycles whose pin lacks it, and the columns for
   a pin that is unknown or a cycle that is not read.
3. **What still waits, and for how long.** Each issue of *Open issues*: the cycles in which its
   problem came back, its problems and its *Days waiting*. Add the issues of *Dropped issues* once,
   as the count gives them, with no waiting.
4. **What each version of the process shows.** For each series of *Process versions*, one at a time,
   with the line that says why it begins where it does: the median cost at constant prices of each
   version and its answers Q1, Q2 and Q3, which `yes`, `no` or `unknown` give inside that series. Quote
   the cycles of a version from *Cost*, with their share of the cost in fix rounds, where the human
   wants them. Name together, in one matter, the series whose rows give nothing but `unknown`, and
   the cycles in *No version*, with the reasons *Unknown values* gives.

Where the register itself seems wrong to the human, such as a problem under another class or an
issue whose fate has changed, the correction is the user's own tool's to make: note it in the result.

## 4. Write the result

Write the result as `audit-<YYYY-MM-DD>.md`, the day of the session, in the `audit_results`
directory beside the counts. Where a note of that day exists, read it and go on from the matters it
holds. Show the human its text first, and write it on the human's yes. It holds:

- the count it rests on, by its file name, and the repositories it read;
- *Weighed*: each matter the human weighs further — the issue's name, or the series and the version's
  commit — with the rows quoted as they were shown and the human's words about it;
- *Set aside*: each matter the human set aside, with the human's reason as said;
- *Not reached*: the matters not yet put before the human, where the session ended early;
- the corrections of the register the human named.

Where the human ends the session early, write the note with what was decided and the rest under
*Not reached*.
