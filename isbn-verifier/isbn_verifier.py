def is_valid(isbn):

    #Fail
    """
    if len(isbn) < 10:
        return False
    print(isbn)
    isbn = [value for value in isbn if value != "-"]
    print(isbn)
    isbn = [eval(value) for value in isbn]
    print(isbn)


    last = isbn.pop(-1)
    if not(last.isnumeric or last == "X"):
        return False
    print(last)


    calc = 0

    for index, num in enumerate(isbn):
        calc = calc + index * num
    print(calc)

    print((calc + last) % 11)
    if calc + last % 11 == 0:
        return True
    """
    #Fail

    isbn = list(isbn)
    if eval(isbn[-1]).isnumeric() or isbn[-1] == "X":
        return False

    return


#is_valid("3-598-21508-8")