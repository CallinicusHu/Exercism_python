def is_valid(isbn):
    # fail
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
    # Fail

    # vacak = isbn

    """
    for rosz in vacak:
        print(rosz)
        #print(rosz, isbn)
        if not(rosz.isnumeric()):
            print("\t", rosz, isbn)
            isbn.remove(rosz)
            print("\t", rosz, isbn)
    """

    print(isbn)
    isbn = list(isbn)
    if len(isbn) < 10:
        return False
    last = isbn.pop(-1)
    #print("1", isbn, type(isbn))
    #print("2", last, type(isbn))
    if last == "X":
        last = "10"

    #print("3", last, type(last))

    if not (last.isnumeric()):
        return False

    last = int(last)

    #print("fail", isbn)

    I_HATE_ISBN = isbn

    if 9 != len(I_HATE_ISBN):
        if "-" not in I_HATE_ISBN:
            return False

    isbn = [s for s in isbn if s.isdigit()]

    #print("actual:", isbn)
    #print(len(isbn))

    if not (len(isbn) == 9):
        return False

    isbn.append(last)
    #print(isbn)

    I_HATE_ISBN = isbn

    isbn = [int(s) for s in isbn]
    print("numeric", isbn)

    total = 0

    for index, add in enumerate(range(9, -1, -1)):
        #print(isbn, ":", (index + 1), isbn[add], (index + 1) * isbn[add], total)
        total = total + ((index + 1) * isbn[add])
        #print(total)

    #print("total", total)

    if total % 11 == 0:
        return True

    return False

a = is_valid("3-598-21508-8adg")
print(a)
print("\n")

b = is_valid("359821508262456g")
print(b)
print("\n")

c = is_valid("3-5ttert98-21508-8adg")
print(c)
print("\n")

d = is_valid("3-598-21508-8")
print(d)
print("\n")

e = is_valid("a3-598-21a508-8")
print(e)
print("\n")

