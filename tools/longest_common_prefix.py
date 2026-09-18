# tool: longest_common_prefix
# description: Finds the longest common prefix of a comma-separated list of strings.
# author: @1998LJ
# longest_common_prefix("flower,flow,flight") → "fl"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    raw = str(args[0])
    parts = raw.split(",")
    if len(parts) < 2:
        return "Error: Please provide a comma-separated list of at least two strings (e.g. 'flower,flow,flight')."

    # Find longest common prefix across all items in parts
    prefix = parts[0]
    for s in parts[1:]:
        new_prefix = []
        for c1, c2 in zip(prefix, s):
            if c1 == c2:
                new_prefix.append(c1)
            else:
                break
        prefix = "".join(new_prefix)
        if not prefix:
            break

    return prefix
