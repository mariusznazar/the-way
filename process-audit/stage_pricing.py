"""The price of the stage rows of a cycle's `stages.md`, moved out of `audit_count.py`.

The price list as numbers (`ModelPrice`, `Prices`), a row of the section of tokens by model
(`StageTokens`) and the cost in dollars of such rows at a list's prices (`priced`, `priced_older`,
`cost_at`), as `process-audit/audit_count.py` counts the cost of a cycle (WAY-337). It is imported,
never run, and runs nothing when imported. Standard library only.
"""

from dataclasses import dataclass
from decimal import Decimal

UNKNOWN = "unknown"
NO_MODEL = "—"
ORCHESTRATOR = "orchestrator"
MILLION = Decimal(1_000_000)
# A text copied from a file into a reason is cut to this many characters.
TEXT_CAP = 200


@dataclass(frozen=True)
class ModelPrice:
    """The prices of one model per million tokens. A write price is None where the list has `—`
    for that lifetime: the model has no price for such a write, while the other prices stand."""

    input: Decimal
    cached: Decimal
    output: Decimal
    write_5m: Decimal | None
    write_1h: Decimal | None


@dataclass
class Prices:
    """The price list: its date, and per model its prices, or None where no page gives the price
    of its input, its cached input or its output: a model with no price at all."""

    date: str
    table: dict[str, ModelPrice | None]


@dataclass
class StageTokens:
    """One row of the section of `stages.md` that gives each stage's tokens by model. `files` is
    what its cell *Files named* gives: the files of `reports/` the turn was given, None where the
    cell reads `unknown` or the form has no such column; `files_read` is False where the cell is
    not a list of such files. `write_5m` and `write_1h` are the cache writes of each lifetime, parts
    of `input`: zero for the forms that have no such columns and for the older table."""

    number: str
    name: str
    model: str
    input: int
    cached: int
    output: int
    files: frozenset[str] | None = None
    files_read: bool = True
    write_5m: int = 0
    write_1h: int = 0


def is_orchestrator_row(name: str) -> bool:
    """The orchestrator's own rows, as `cycle_stages.py` names them: its stretches and the rows of
    its work while subagents run in parallel. Their work is the orchestrator's, so they serve no
    fix round by the files they name; the orchestrator's tokens while a fix runs stand in the
    fix's own row."""
    return name == ORCHESTRATOR or name.startswith("orchestrator while in parallel: ")


def priced(rows: list[StageTokens], prices: Prices) -> tuple[list[Decimal] | None, str | None]:
    """The cost in dollars of each row at the list's prices, or None with the reason: a model with
    no price, a cached input above its input, a subagent stage with no token usage, a stage whose
    model is unknown, or a section with no stage that has any, make the cost unknown. A row of the
    orchestrator with no token usage — a stretch, or its work while subagents run in parallel —
    costs nothing."""
    costs: list[Decimal] = []
    if all(row.model == NO_MODEL for row in rows):
        return None, "every stage of `stages.md` has no token usage, so the cost is not known"
    for row in rows:
        # A name from `stages.md` is cut before it reaches a reason: the reason is written twice
        # per cycle, and a crafted name would otherwise make the result as large as the file.
        name = row.name[:TEXT_CAP]
        if row.model == UNKNOWN:
            # `cycle_stages.py` writes this for a stage whose transcript holds no token usage at
            # all, and for tokens of a response that names no model.
            return None, (
                f"stage `{name}` gives its model as unknown: its token usage was not "
                "read, or names no model"
            )
        if row.model == NO_MODEL:
            if is_orchestrator_row(row.name):
                # A row of the orchestrator's own work with no response of a model in it:
                # `cycle_stages.py` reads every response of the orchestrator's transcript.
                costs.append(Decimal(0))
                continue
            # `cycle_stages.py` writes this mark for a stage it found no token usage for: its
            # tokens are not known, so its cost is not zero.
            return None, (
                f"stage `{name}` has no token usage in its transcript, so its cost is not known"
            )
        if row.cached > row.input:
            return None, f"the cached input of stage `{name}` is above its input"
        if row.cached + row.write_5m + row.write_1h > row.input:
            return None, (
                f"the cached input and the cache writes of stage `{name}` are above its input"
            )
        price = prices.table.get(row.model)
        if price is None:
            return None, f"the price list gives no price for model `{row.model[:TEXT_CAP]}`"
        cost, reason = cost_at(price, row)
        if cost is None:
            return None, reason
        costs.append(cost)
    return costs, None


def cost_at(price: ModelPrice, row: StageTokens) -> tuple[Decimal | None, str | None]:
    """The cost in dollars of a row at a price, or None with the reason where the row holds writes
    of a lifetime the price list gives no price for. The input that is neither read from a cache nor
    written to one is priced at the *Input* price, the cached input at the *Cached input* price,
    the writes of each lifetime at their own price and the output at the *Output* price; a row with
    no writes is priced by the first, the second and the last alone. The caller has checked that the
    cached input and the writes together are not above the input."""
    plain = row.input - row.cached - row.write_5m - row.write_1h
    total = (
        Decimal(plain) * price.input
        + Decimal(row.cached) * price.cached
        + Decimal(row.output) * price.output
    )
    for count, write_price, lifetime in (
        (row.write_5m, price.write_5m, "5 minutes"),
        (row.write_1h, price.write_1h, "1 hour"),
    ):
        if count == 0:
            continue
        if write_price is None:
            return None, (
                f"the price list gives no price of a cache write of {lifetime} for "
                f"model `{row.model[:TEXT_CAP]}`"
            )
        total += Decimal(count) * write_price
    return total / MILLION, None


def priced_older(
    rows: list[StageTokens], prices: Prices
) -> tuple[list[Decimal] | None, str | None]:
    """The cost in dollars of each row of the table of tokens by model at the list's prices, as
    `priced` gives it for the rows of the section, or None with the reason: a model `unknown`, a
    cached input above its input, or a model with no price make the cost unknown."""
    costs: list[Decimal] = []
    for row in rows:
        name = row.model[:TEXT_CAP]
        if row.model == UNKNOWN:
            return None, (
                "the table of tokens by model names the model `unknown`: its token usage "
                "was not read, or names no model"
            )
        if row.cached > row.input:
            return None, f"the cached input of model `{name}` is above its input"
        price = prices.table.get(row.model)
        if price is None:
            return None, f"the price list gives no price for model `{name}`"
        cost, reason = cost_at(price, row)
        if cost is None:
            return None, reason
        costs.append(cost)
    return costs, None
