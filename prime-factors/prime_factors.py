import math


def factors(n):
    factors = []
    quot, rem = divmod(n, 2)
    while rem == 0 and n > 1:
        factors.append(2)
        n = quot
        quot, rem = divmod(n, 2)

    candidate = 3
    while n > 1:
        quot, rem = divmod(n, candidate)
        while rem == 0:
            factors.append(candidate)
            n = quot
            quot, rem = divmod(n, candidate)

        candidate += 2

    return factors
