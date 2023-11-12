def flatten(iterable):
    iterable = str(iterable)
    final = []

    for numbers in range(len(iterable)):
        if not (iterable[numbers].isdigit() or iterable[numbers] == "-"):
            iterable = iterable.replace(iterable[numbers], " ")

    for hole in iterable.split():
        final.append(int(hole))

    return final
