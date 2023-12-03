import math


def factors(value):

    primes = find_primes(value)
    prime_factors = []
    temporary = value
    count = 0

    while temporary > 1:
        if temporary % primes[count] == 0:
            temporary //= primes[count]
            prime_factors.append(primes[count])

        else:
            count += 1

    return prime_factors


def find_primes(value):
    primes = []

    for numbers in range(2, math.isqrt(value) + 10):  # +10 because low numbers sometimes fail
        if math.lcm(numbers, value) == value:
            primes.append(numbers)

    print(primes)

    return primes
