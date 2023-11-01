def is_valid(isbn):

    #fail
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
    if len(isbn) < 11:
        return False
    last = isbn.pop(-1)
    print("1", isbn, type(isbn))
    print("2", last, type(isbn))
    if last == "X":
        last = "10"

    print("3", last, type(last))

    if not(last.isnumeric()):
        return False

    last = int(last)

    #vacak = isbn

    """
    for rosz in vacak:
        print(rosz)
        #print(rosz, isbn)
        if not(rosz.isnumeric()):
            print("\t", rosz, isbn)
            isbn.remove(rosz)
            print("\t", rosz, isbn)
    """

    print("fail", isbn)

    if not(len(isbn) == 12) or not[s for s in isbn if s.isdigit()]: #ezen mennyire meglepődtem hogy működik O_O
        return False

    isbn = [s for s in isbn if s.isdigit()]

    print("actual:", isbn)
    print(len(isbn))

    if not(len(isbn) == 9):
        return False



    return True


#is_valid("3-598-21ihacnhnori508-X") # itt nem fut le annyiszor mint kéne?
#is_valid("3-598-21508-X") #ezzel még működik
#is_valid("e-598-21S08-X") #