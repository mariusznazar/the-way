# Decision log

The decisions of the game.

## Saving

How a game is saved and what a save holds.

### GAME-01 — How is a game saved?

A game is saved to one file.

- **Scope:** core, persistence
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision:
  - complies: a save writes `game.sav`;
  - violates: a save writes two files.
- **Origin:** none

*Rationale:* one file is easy to copy.
*Rejected:* a folder of files.

## Withdrawn identifiers

| Identifier | Why |
|---|---|
| GAME-00 | merged into GAME-01 |
