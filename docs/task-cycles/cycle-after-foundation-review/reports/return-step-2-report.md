# Return step report (after correction 1)

**Status:** done. The return step commits nothing; the head stays `f92d9dd` and the worktree is clean.

## Return step (as the record's item gives it)

- **Foundation compared with code:** nothing no longer matched. What I compared:
  - WAY-316 (new third paragraph, `narrows WAY-373`, the added sentence of *Rationale*) with WAY-373 and
    WAY-25: WAY-316 names WAY-373 in *Relations* and states the area in its binding sentences, as WAY-25
    asks; WAY-373 narrows nothing and nothing else narrows either (`git grep "narrows WAY-316\|narrows
    WAY-373"` finds only WAY-316's line), so no two decisions narrow each other.
  - The first paragraph of "Working copies" in `task-cycle/skill/SKILL.md` (the exception for a screenshot
    shown to the human), `task-cycle/change/ui_check.md` (lines 12-21), `task-cycle/review/SKILL.md`
    (lines 91-96) and `task-cycle/skill/request_template.md` (lines 181-186, kind 13, *Checks*): each says
    a shown screenshot lies in the place the product's foundation settles, outside the repository, and
    that where none is settled none is kept or shown; none says a shown screenshot goes to the agent's
    directory. They agree with the new paragraph.
  - The invariants `record-copy-image-check` and `record-copy-image-files` and their tests
    (`task-cycle/test_image_files_check.py`): the rule is about image files in the record's copy and is
    not touched by the precedence.
  - The entries the first return step compared (WAY-13, WAY-375, WAY-376, WAY-261, WAY-289): the
    correction touched none of them.
  - The part map entries `task-cycle` and `decisions`: no file moved between parts, no dependency added;
    no change.
- **Decisions written or changed:** none in this return step. (The correction changed WAY-316.)
- **Invariants written or changed:** none.
- **Environment facts:** none.
- **Glossary terms:** none; no term used against its entry.
- **Part-map changes:** none.
- **Projected entries written:** none.
- **Rows of *Settlements to record* written:** none in this return step (rows 1-7 were written by the
  foundation step; the correction carries remark 1, which is no row).
- **The correction review's Minor finding** (WAY-316's *Verification* has no complies/violates line for
  the new precedence) is a review finding and no foundation entry; as the handoff says, I did not write
  it, deferred nothing and list it for no later work.

## Checks (command, exit code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (full, no `--skip-test-citations`) | 0 (`0 errors`) |

No test directory was run: this step changed no file, and the directory runs of the correction itself
(`elements/common`, `task-cycle`, `agent-instructions`, all exit 0) stand on the same tree. The whole
gate was not run, as instructed.

## Reaches beyond the handoff

- `task-cycle/review/SKILL.md`, lines 88-99 (read): it says where a screenshot the reviewer takes lies,
  so I compared it.

## Unread material

none. (The handoff, `foundation_step.md` and `return_step.md` were read whole, the latter two earlier in
this session and not read again; the files compared were read in the passages named above.)

## Searches not found or unclear

none

## Working copies

None made.
