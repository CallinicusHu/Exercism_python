num_up_to_9 = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
tenfolds = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
teens = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
prefixes = {3: "thousand", 6: "million", 9: "billion"}

def say(number):
    if number < 0:
        raise ValueError("input out of range")

    if number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    return any_big(number)


def up_till_99(number):

    if number < 10:
        return num_up_to_9[number]

    if number == 10:
        return "ten"

    if number < 20:
        return teens[number]

    dash = "-"
    if number % 10 == 0:
        dash = ""

    return f"{tenfolds[number // 10]}{dash}{num_up_to_9[number % 10]}"

def up_till_999(number):

    if number < 100:
        return up_till_99(number)

    mendokusai = " hundred "
    if number % 100 == 0:
        mendokusai = " hundred"

    return f"{num_up_to_9[number // 100]}{mendokusai}{up_till_99(number % 100)}"

def any_big(number):

    if number < 1_000:
        return up_till_999(number)

    lennie = len(str(number))

    if lennie < 6:
        power = 3
    elif lennie < 9:
        power = 6
    #elif lennie < 12:
    #    power = 9
    #else:
    #    power = 12
    else:
        power = 9

    # power = ??? #in one line / formula

    mendokusai = f" {prefixes[min(power, 9)]} "
    if number % (10 ** power) == 0:
        mendokusai = f" {prefixes[min(power, 9)]}"

    return f"{any_big(number // (10 ** power))}{mendokusai}{any_big(number % (10 ** power))}"
    # ???
    """
    >>> 987_654_321_123 % 10 ** 9 
    654321123
    >>> 987_654_321_123 // 10 ** 9
    987

    """


