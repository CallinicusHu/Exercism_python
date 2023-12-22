import itertools


def annotate(minefield):
    check = []
    for line in minefield:
        for char in line:
            if " " != char != "*":
                raise ValueError("The board is invalid with current input.")
        check.append(len(line))
    if check and sum(check) != check[0] * len(check):
        raise ValueError("The board is invalid with current input.")

    iterate = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    del iterate[4]
    are_valid_indexes = lambda a, i, y, b, c, x: (a > (i + y) >= 0) and (b > (c + x) >= 0)
    mines = 0

    for i, line in enumerate(minefield):
        for c, entry in enumerate(line):
            if entry == " ":
                for y, x in iterate:
                    if are_valid_indexes(len(minefield), i, y, len(line), c, x) and minefield[i + y][c + x] == "*":
                        mines += 1

            if mines > 0:
                minefield[i] = f"{minefield[i][:c]}{mines}{minefield[i][c + 1:]}"
                mines = 0

    return minefield
