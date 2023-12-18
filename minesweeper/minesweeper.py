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

    mines = 0

    iterate = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    del iterate[4]

    for i, lines in enumerate(minefield):
        for c, col in enumerate(lines):
            if minefield[i][c] == " ":
                for y, x in iterate:
                    if ((len(minefield) - 1) >= (i + y) >= 0) and ((len(lines) - 1) >= (c + x) >= 0) and minefield[i + y][c + x] == "*":

                        mines += 1

            if mines > 0:
                minefield[i] = f"{minefield[i][:c]}{mines}{minefield[i][c + 1:]}"
            mines = 0

    return minefield
