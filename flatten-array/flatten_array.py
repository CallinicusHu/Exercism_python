def flatten(iterable):
    cheat_str = str(iterable)
    final = []
    add_to_int = ""

    for numbers in range(len(cheat_str)):
        if cheat_str[numbers].isdigit() or cheat_str[numbers] == "-":
            add_to_int = add_to_int + cheat_str[numbers]
        else:
            add_to_int = add_to_int + " "

    for hole in add_to_int.split():
        final.append(eval(hole))

    return final
