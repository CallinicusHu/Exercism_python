def flatten(iterable):
    iterable = str(iterable)
    final = []

    """ #works fine tried something else
    add_to_int = ""

    
    for numbers in iterable: #numbers is used to find the numbers in cheat_str
        if numbers.isdigit() or numbers == "-":
            add_to_int += numbers
        else:
            add_to_int += " "
            
    """

    for numbers in range(len(iterable)):
        if not(iterable[numbers].isdigit() or iterable[numbers] == "-"):
            iterable = iterable.replace(iterable[numbers], " ") #this only works with index

    for hole in iterable.split():
        final.append(int(hole))

    """ #I do think the line 26 or 27 should both work instead of lines 21-22 but they produce strange errors I don't understand.
    print(final)
    final = final.append(int(hole) for hole in iterable.split())
    final.append(int(hole) for hole in iterable.split())
    print(final)
    """

    return final
