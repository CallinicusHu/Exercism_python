def flatten(iterable):
    iterable = str(iterable)
    final = []
    add_to_int = ""

    for numbers in iterable: #numbers is used to find the numbers in cheat_str
        if numbers.isdigit() or numbers == "-":
            add_to_int += numbers
        else:
            add_to_int += " "

    for hole in add_to_int.split():
        final.append(int(hole))

    return final
