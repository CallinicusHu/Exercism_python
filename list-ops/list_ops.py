def append(lst1, lst2):
    return lst1 + lst2


def concat(lsts): #one line
    return [x for lst in lsts for x in lst]


def filter(function, lst): #one line
    return [item for item in lst if function(item)]


def length(lst): #can this be done in one line without calling a builtin function?
    return sum(1 for item in lst) #this works but I am not sure if I want to call functions in this task


def map(function, lst): #one line
    return [function(item) for item in lst]


def foldl(function, lst, initial): #can this be done in one line?
    for item in lst:
        initial = function(initial, item)
    return initial


def foldr(function, lst, initial): #can this be done in one line?
    for item in reverse(lst):
        initial = function(initial, item)
    return initial


def reverse(lst): #can this be done in one line?
    leng = length(lst)-1 #this is not cheating I wrote it
    reversed = []
    for item in lst: #I do not use the item in this for anything, am I making a mistake here?
        reversed = append(reversed, [lst[leng]]) #this too
        leng -= 1

    return reversed

    #return lst[::-1] #this works of course but again it feels like cheeting

