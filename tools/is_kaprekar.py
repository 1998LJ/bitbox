# tool: is_kaprekar
# description: Checks whether an integer is a Kaprekar number.
# author: @1998LJ
# example: is_kaprekar "9" -> "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    value = str(args[0]).strip()
    if not value:
        return "Error: Argument cannot be empty."

    try:
        n = int(value)
    except ValueError:
        return "Error: Argument must be an integer."

    if n < 0:
        return "False"

    digits = len(str(n))
    square = str(n * n).zfill(digits + 1)
    left = int(square[:-digits] or "0")
    right = int(square[-digits:])
    return str(left + right == n)
