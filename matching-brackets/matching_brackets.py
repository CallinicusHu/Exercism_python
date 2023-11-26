import string

brackets = list("[](){}")

def is_paired(input_string):


    cntr = []

    for items in range(len(brackets)):
        cntr.append(input_string.count(brackets[items]))

    if not((cntr[0] == cntr[1]) and (cntr[2] == cntr[3]) and (cntr[4] == cntr[5])):
        print("right amounts")
        return False

    #check, fail, works but useless
    check = []

    for bracket in range(0, len(brackets), 2):
        if brackets[bracket] in input_string:
            for char in input_string:
                if char == brackets[bracket] or char == brackets[bracket + 1]:
                    check.append(char)


    print(check)

    only_brackets = input_string

    for char in input_string:
        if char not in brackets:
            only_brackets = only_brackets.replace(char, "")

    print(only_brackets)

    """ fail
    for bracket in range(0, len(brackets), 2):
        if brackets[bracket] in only_brackets:
            where = only_brackets.find(brackets[bracket]) + 1
            if not (only_brackets[-where] == brackets[bracket + 1]):
                return False
    """

    """ so fail
    first_half = only_brackets[:(len(only_brackets) // 2)]
    print(first_half)
    first = "[({"
    second = "])}"
    trans = {"[": "]", "(": ")", "{": "}", "]": "[", ")": "(", "}": "{"}
    what = first_half.maketrans(trans)
    second_half = first_half.translate(what)
    print(second_half)

    print(only_brackets)
    print(first_half+second_half)

    if only_brackets == (first_half+second_half):
        return False
    """

    return True

