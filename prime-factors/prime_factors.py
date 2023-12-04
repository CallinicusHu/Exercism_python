import math


def factors(value):

    primes = find_primes(value) # prime candidates, numbers where which has the lcm equal to the value
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

    prime_candidates = []

    for numbers in range(2, find_lcm_part(value)):
        if math.lcm(numbers, value) == value:
            prime_candidates.append(numbers)

    return prime_candidates

def find_lcm_part(value):
    return 10 ** (len(str(value)) - len(str(value))//2) #now it should work with any number
