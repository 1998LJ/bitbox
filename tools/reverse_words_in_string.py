# tool: reverse_words_in_string
# description: Reverses the order of words in a string.
# author: @1998LJ
# example: reverse_words_in_string "hello world" -> "world hello"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    return " ".join(reversed(str(args[0]).split()))
