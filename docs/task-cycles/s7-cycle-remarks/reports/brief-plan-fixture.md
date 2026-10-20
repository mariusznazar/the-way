# Plan — illustrative documentation correction

- Task: illustrative frozen task
- Spec: none
- Base: illustrative base

## Foundation entries

none

## Slices

### Slice 1 — Clarify the accepted answer

- **Goal:** An accepted answer is carried without another question.
- **Change:** `instructions.md`
- **Read:** `decision.md`
- **Checks:** Compare both authorized and unapproved-answer scenarios.
- **Depends on:** none

### Slice 2 — Present an unanswered proposal

- **Goal:** A proposal awaits the human's answer.
- **Change:** `questions.md`
- **Read:** `instructions.md`
- **Checks:** Compare accepted and rejected proposal scenarios.
- **Depends on:** Slice 1

## Independence and execution

Sequential: the question uses the acceptance instruction.

## Coverage

| Requirement | Slice |
|---|---|
| Accepted answer | 1 |
| Unanswered proposal | 2 |

## Choices

none
