# tool: pairwise_sum
# description: Sums corresponding elements of two comma-separated number lists.
# author: @1998LJ
# example: pairwise_sum "1,2,3" "4,5,6" -> "5,7,9"

from decimal import Decimal, InvalidOperation


def _parse_numbers(value: object) -> list[Decimal] | None:
    parts = [part.strip() for part in str(value).split(",")]
    if not parts or any(not part for part in parts):
        return None
    try:
        return [Decimal(part) for part in parts]
    except InvalidOperation:
        return None


def _format_number(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide exactly two comma-separated lists."

    first = _parse_numbers(args[0])
    second = _parse_numbers(args[1])
    if first is None or second is None:
        return "Error: Lists must contain valid numbers."
    if len(first) != len(second):
        return "Error: Lists must have the same length."

    return ",".join(
        _format_number(left + right)
        for left, right in zip(first, second)
    )
