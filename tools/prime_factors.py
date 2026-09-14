# tool: prime_factors
# description: Return the prime factors of n
# author: @1998LJ
# example: prime_factors "12" -> "2,2,3"


def run(*args) -> str:
    if not args or not str(args[0]).strip():
        return ""
    try:
        n = int(str(args[0]).strip())
    except ValueError:
        return ""
    if n <= 1:
        return ""

    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(str(d))
            n //= d
        d += 1
    if n > 1:
        factors.append(str(n))

    return ",".join(factors)
