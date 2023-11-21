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

    check = True

    for items in list_one:
        if items not in list_two:
            check = False
    if check:
        return SUBLIST

    check = True

    for items in list_two:
        if items not in list_one:
            check = False
    if check:
        return SUPERLIST

    return UNEQUAL


