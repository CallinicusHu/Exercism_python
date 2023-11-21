"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):

    if list_one == list_two:
        return EQUAL

    #list_one.sort()
    #list_two.sort()

    compare = []

    for items in range(len(list_one)):
        if list_one[items] in list_two:
            compare.append(list_one[items])
            print(compare)

    if compare == list_one:
        return SUBLIST

    compare.clear()

    for items in range(len(list_two)):
        if list_two[items] in list_one:
            compare.append(list_two[items])
            print(compare)

    if compare == list_two:
        return SUPERLIST



    return UNEQUAL


