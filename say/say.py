import math

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

    power = (math.ceil(len(str(number)) / 3)) * 3 - 3

    mendokusai = f" {prefixes[power]} "
    if number % (10 ** power) == 0:
        mendokusai = f" {prefixes[power]}"

    return f"{any_big(number // (10 ** power))}{mendokusai}{any_big(number % (10 ** power))}"


