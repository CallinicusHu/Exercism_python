from math import sqrt

def score(x, y):

    #x = abs(x)

    #y = abs(y)

    z = sqrt(x * x + y * y)

    if z <= 1:
        return 10

    if z <= 5:
        return 5

    if z <= 10:
        return 1
 
    else:
        return 0
