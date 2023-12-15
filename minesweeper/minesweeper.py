def annotate(minefield):
    check = []
    for line in minefield:
        for char in line:
            if " " != char != "*":
                raise ValueError("The board is invalid with current input.")
        check.append(len(line))
    if check and sum(check) != check[0] * len(check):
        raise ValueError("The board is invalid with current input.")

    iterate = [[-1, -1], [-1, +0], [-1, +1],
               [+0, -1], [+0, +1],
               [+1, -1], [+1, +0], [+1, +1]]

    for i, line in enumerate(minefield):
        for c, pos in enumerate(line):

            if pos == " ":
                mines = 0
                for lin, col in iterate:
                    try:
                        if minefield[i + lin][c + col] == "*":
                            mines += 1

                    except:
                        continue

                if mines > 0:
                    minefield[i] = f"{minefield[i][:c]}{mines}{minefield[i][c + 1:]}"

    return minefield
