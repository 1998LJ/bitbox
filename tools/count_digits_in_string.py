# tool: count_digits_in_string
# description: Counts digit characters in a string.
# author: @1998LJ
# example: count_digits_in_string "abc123" -> "3"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    return str(sum(character.isdigit() for character in str(args[0])))
