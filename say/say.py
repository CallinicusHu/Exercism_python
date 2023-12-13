numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
           10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred",
           11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
fixes = {3: "thousand", 6: "million", 9: "billion"}

def say(number):
    if number < 0:
        raise ValueError("input out of range")

    if number > 999_999_999_999:
        raise ValueError("input out of range")

    if number < 21:
        return numbers[number]

    num_str = str(number).rjust(12, "0")

    magnitudes = [num_str[0:3], num_str[3:6], num_str[6:9], num_str[9:12]]

    print(magnitudes)

    for digits in range(2, -1, -1): #wrong but in progress
        if magnitudes[-1][digits] == "0":
            continue
        else: print(numbers[int(magnitudes[-1][digits])])