# tool: character_appearances
# description: Counts occurrences of each character in a string.
# author: @1998LJ
# example: character_appearances "banana" -> "a:3,b:1,n:2"

from collections import Counter


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    text = str(args[0])
    counts = Counter(text)
    return ",".join(
        f"{character}:{counts[character]}"
        for character in sorted(counts)
    )
