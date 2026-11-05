# Report of the return step — task stage-remarks-check

**Status:** done

**Commits:** none. Head stays `5e90498`; the worktree is clean (`git status --short` prints nothing).
Nothing needed correcting, so the own-work check, which the handoff asks for where text or code is
committed, does not apply.

## Return step (fields of `task-cycle/record_template.md`)

- **Foundation compared with code:**
  - WAY-294 (written), against `task-cycle/remarks_check.py`, `task-cycle/skill/SKILL.md` ("The
    process remarks check", step 12, step 9.4 stop), `correction.md`, `blocked_finding.md` and
    `reserved_return.md`: the commits it names (copy for a request, its repetition in a correction,
    copy of a blocked request) are exactly the sites that call the check; the script lists items other
    than `none`, only lists, and lists an item again until the remarks hold it as many times as the
    reports give it (`check()` counts with `seen` against `held`); the orchestrator's append with stage
    name and full report path stands in SKILL.md and the record template. It matches.
  - WAY-295 (written), against SKILL.md "A listing you hold wrong", `request_template.md` item 10, the
    *Checks* line and the variant row: script unchanged in the cycle, archive written, case entered in
    the remarks as an entry of the orchestrator and not as an item of its stage, case in *For you to
    decide*; "the repeated run does not hold the archive back" is in SKILL.md ("the archive is not held
    back"). It matches. The request's state stays as it is for its other causes in both the text and
    the entry, which says nothing of a draft.
  - WAY-296 (written), against `record_template.md` (the list item `Process remarks on the-way` with
    entries under it, last item of the record) and `TemplateTest`: it matches.
  - WAY-260 (named by the task): its text, "into the cycle record's *Process remarks on the-way*",
    names the item the template now fixes, and its *Verification* (omit, edit or combine an item is a
    violation) is what the script checks. It matches; no edit.
  - WAY-148 (named): the check adds no stage message or handoff duty, and the stage reports it reads
    stay files in the cycle's `reports/`. It matches.
  - WAY-38 and WAY-89 (named): `grep` of `task-cycle/remarks_check.py` shows only `argparse`, `re`,
    `sys`, `collections`, `dataclasses`, `pathlib` and `__future__`, and no `subprocess` or `os.system`;
    the script runs on the Python 3.14 the repository declares. It matches.
  - WAY-290 and WAY-291 (named): the pattern is followed (script not fixed in the cycle, case in the
    request's decisions and *Checks*, case copied into the remarks); WAY-291's draft state is not
    copied, which WAY-295 does not claim. It matches.
  - The entries the search of the foundation found (`foundations/` for "process remark", "remarks",
    "Searches not found", "word for word", "request_check", "form check"; made at the foundation step):
    WAY-286 only gives the form of the description; no collision.
  - Part map: `task-cycle` (`task-cycle/**` covers the new script and test; its responsibility, "the
    steps a task runs through and the review its change gets along them", still holds with a check
    inside a step) and `decisions` (`elements/decisions/**`, `foundations/decisions.md`; three entries
    added in its form). No entry needs a change.
  - Exclusion: the task's *Out of scope* excludes changes to `cycle_remarks_digest.py` and
    `/ai-review-cycles`; no entry is written for them. The script keeps a port of the digest's cut and
    the template names the digest; neither changes the digest.
  - The review's Minor findings M1 (substring match), M2 (request state unchanged for a held-wrong
    listing) and M3 (`display()` escapes) are not fixed here, as the handoff says. None of the entries
    contradicts the code because of them: WAY-294's "hold word for word" is the containment reading M1
    describes.
- **Decisions written or changed:** none in this step (WAY-294, WAY-295 and WAY-296 were written at the
  foundation step and stand unchanged).
- **Invariants written or changed:** none. The task, the decisions and the human set no rule that
  needs one.
- **Environment facts:** none. The change rests on no source outside the product (the digest and the
  `loop2` archives are inputs of the acceptance run, not facts a decision rests on).
- **Glossary terms:** none. No word is used in another meaning than its usual one; "process remarks"
  and "report" are plain words and are not in the glossary.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none; the task is independent and projects none.
- **Rows of *Settlements to record* written:** row 1 as WAY-294, row 2 as WAY-295, row 3 as WAY-296
  (written at the foundation step; found made true by the code and the process text).

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle`: exit 0.
- Not run: the product's gate `python -B gate/run_tests.py`, which is the orchestrator's.
  The two runs above were made although nothing was committed, to confirm the state is unchanged.

## Reaches beyond the handoff

- `foundations/part_map.md`, the `decisions` and `task-cycle` entries (the handoff names them).
- `foundations/decisions.md`, WAY-294 to WAY-296 read again as written, and `task-cycle/skill/*.md`
  and `task-cycle/record_template.md` re-read for the comparison. All inside the handoff's list; no
  reach outside it.

## Searches not found or unclear

- Whether `task-cycle/record_template.md` should name `cycle_remarks_digest.py`, a script of the
  author's private notes outside the repository: I wrote that name at the first stage, to say why
  the block has the form it has. Unclear whether a file of the-way may name it. The comparison finds
  no foundation entry against it, so I left it.
