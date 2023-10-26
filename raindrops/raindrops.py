def convert(number):

    ppp = ""
    a = True
    b = True
    c = True

    if number % 3 == 0:
        ppp = ppp + "Pling"
        a = False
    if number % 5 == 0:
        ppp = ppp + "Plang"
        b = False
    if number % 7 == 0:
        ppp = ppp + "Plong"
        c = False
    if a and b and c:
        ppp = str(number)

    return ppp
