def factors(value):
    #print("\n", value, "\n")
    primes = find_primes(value)
    primes.append(value)
    prime_factors = []
    temporary = value
    count = 0

    while temporary > 1:
        if temporary % primes[count] == 0:
            temporary //= primes[count]
            prime_factors.append(primes[count])
            #print(temporary)
        else:
            count += 1

    #print("prime factors", prime_factors, "\n---")
    return prime_factors


def find_primes(value):
    primes = []
    for numbers in range(2, (value // 2) + 1):
        #print(numbers)
        prime = True
        for number in range(2, numbers):
            if numbers % number == 0:
                prime = False
        if prime:
            primes.append(numbers)

    #print("primes", primes)
    return primes