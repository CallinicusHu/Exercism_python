
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

    for i, line in enumerate(minefield):
        for c, pos in enumerate(line):
            if pos == " ":

                if i > 0 and c > 0 and minefield[i - 1][c - 1] == "*":
                    mines += 1
                if i > 0 and minefield[i - 1][c] == "*":
                    mines += 1
                if i > 0 and c < len(line) - 1 and minefield[i - 1][c + 1] == "*":
                    mines += 1

                if c > 0 and minefield[i][c - 1] == "*":
                    mines += 1
                if c < len(line) - 1 and minefield[i][c + 1] == "*":
                    mines += 1

                if i < len(minefield) - 1 and c > 0 and minefield[i + 1][c - 1] == "*":
                    mines += 1
                if i < len(minefield) - 1 and minefield[i + 1][c] == "*":
                    mines += 1
                if i < len(minefield) - 1 and c < len(line) - 1 and minefield[i + 1][c + 1] == "*":
                    mines += 1

                if mines > 0:

                    minefield[i] = f"{minefield[i][:c]}{mines}{minefield[i][c+1:]}"

                mines = 0

    return minefield
