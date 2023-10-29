def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
        #if i > (number / 2):
        #    break

    if sum(factors, -factors[-1]) > number:
        return "abundant"
    if sum(factors, -factors[-1]) < number:
        return "deficient"

    return "perfect"
