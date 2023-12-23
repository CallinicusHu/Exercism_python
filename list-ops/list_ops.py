def append(list1, list2):
    return list1 + list2


def concat(lists): #how can I write this in one line?

    #works without function but multiple lines
    concated = []
    for item in lists:
        concated += item
    return concated

    #print([item for item in lists]) #I don't understand
    #return [item for item in lists] #not works I don't understand how to compress that for



def filter(function, list):
    return [item for item in list if function(item)]


def length(list): #how can I write this in one line?

    #works without function but multiple lines
    #leng = 0
    #for item in list:
    #    leng += 1
    #return leng

    return sum(1 for item in list) #this works but I am not sure if I want to call functions in this task





def map(function, list): #how can I write this in one line?
    new_list = []
    for item in list:
        new_list += [function(item)]
    return new_list


def foldl(function, list, initial): #I don't yet understand what to do here
    folded = []
    return folded


def foldr(function, list, initial): #I yet to understand what to do here
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
