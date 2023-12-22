def append(list1, list2):
    return list1 + list2


def concat(lists): #how can I write this in one line?
    concated = []
    for item in lists:
        concated += item
    return concated


def filter(function, list): #how can I write this in one line?
    filtered = []
    for item in list:
        if function(item):
            filtered += [item]
    return filtered

def length(list): #how can I write this in one line?
    leng = 0
    for item in list:
        leng += 1
    return leng


def map(function, list): #how can I write this in one line?
    new_list = []
    for item in list:
        new_list += [function(item)]
    return new_list


def foldl(function, list, initial): #I don't yet understand the original function
    folded = []
    return folded


def foldr(function, list, initial): #I yet to understand the original function
    folded = []
    return folded


def reverse(list):
    leng = length(list)-1 #this is not cheating I wrote it
    reversed = []
    for item in list:
        reversed = append(reversed, [list[leng]])
        leng -= 1
    return reversed
    #return list[::-1] #this works of course but it feels like cheeting
