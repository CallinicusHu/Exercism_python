DICT = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 0: "no"}

def lines(start):
    line_1_2 = f"{DICT[start]} green {"bottle" if start == 1 else "bottles"} hanging on the wall,"
    line_3 = "And if one green bottle should accidentally fall,"
    line_4 = f"There'll be {(DICT[start - 1]).lower()} green {"bottle" if start == 2 else "bottles"} hanging on the wall."
    return line_1_2, line_1_2, line_3, line_4

def recite(start, take=1):

    song = []

    for verse in range(take):
        song += lines(start)
        start -= 1
        if verse < take - 1:
            song += ['']

    return song