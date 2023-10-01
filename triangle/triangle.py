def triangle(sides):

    real = False
    
    if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
        real = True

    if sides[0] == sides[1] == sides[2] == 0:
        real = False

    return real


def equilateral(sides):
    
    #if sides[0] == sides[1] == sides[2] == 0:
    #    return False

    if triangle(sides) == False:
         return False
    
    if sides[0] == sides[1] == sides[2]:
        return True
        
    return False


def isosceles(sides):

    if triangle(sides) == False:
         return False
    
    if equilateral(sides) == True:
        return True
    
    if (sides[0] == sides[1] != sides[2]) or (sides[0] != sides[1] == sides[2]) or (sides[0] != sides[1] == sides[2]) or (sides[0] == sides[2] != sides[1]):
        return True
    
    return False


def scalene(sides):

    if triangle(sides) == False:
         return False    
    
    if sides[0] != sides[1] != sides[2] != sides[0]:
        return True
    
    return False
