import string

#brackets = ["[", "]", "(", ")", "{", "}"]  # list("[](){}")

opener_br = ["[", "(", "{"]  # list("[({")
closer_br = ["]", ")", "}"]  # list("])}")


def is_paired(input_string):
    check = []
    for char in input_string:
        if char in opener_br:
            check.append(char)
        elif char in closer_br:
            if not check:
                return False
            if closer_br.index(char) == opener_br.index(check[-1]):
                check.pop()
            else:
                return False

    return not check
    """
    cntr = []

    for items in range(len(brackets)):
        cntr.append(input_string.count(brackets[items]))

    if not ((cntr[0] == cntr[1]) and (cntr[2] == cntr[3]) and (cntr[4] == cntr[5])):
        return False #checked if the number of brackets are correct

    only_brackets = input_string

    for char in input_string:
        if char not in brackets:
            only_brackets = only_brackets.replace(char, "")

    if only_brackets == "": return True  # no brackets, empty string

    if only_brackets[0] not in opener_br:
        return False #starts with correct bracket

    if only_brackets[-1] not in closer_br:
        return False #ends with correct bracket

    bracket_list = list(only_brackets)

    def find_brsub(br):
        for b in br:
            if b in closer_br:
                first = br.index(b)
                break

        return br[:first + 1]

    while len(bracket_list) > 0:
        brsub = find_brsub(bracket_list)
        if closer_br.index(brsub[-1]) != opener_br.index(brsub[-2]):
            return False #incorrect opener closer pair
        bracket_list.pop(len(brsub) - 1)
        bracket_list.pop(len(brsub) - 2)

    return True #rest must be correct
    """
