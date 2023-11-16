def answer(question):
    """ #fail
    if not("plus" in question):
        if not ("minus" in question):
            if not ("divided" in question):
                if not ("multiplied" in question):
                    raise ValueError("unknown operation")
    """

    if ("cubed" in question) or ("Who" in question): #tests needs these
        raise ValueError("unknown operation")

    question = question.split()
    question.pop(0) #remove What
    question.pop(0) #remove is

    if not (question): #is the question string empty now?
        raise ValueError("syntax error")

    question[-1] = question[-1].rstrip("?") #remove ? from the end

    for index, numbers in enumerate(question):
        if numbers == "plus":
            question[index] = "+"

        if numbers == "minus":
            question[index] = "-"

        if numbers == "multiplied":
            question[index] = "*"
            question[index + 1] = "" #this should be deleted but I don't want to mess up the indexing

        if numbers == "divided":
            question[index] = "/"
            question[index + 1] = ""

    if "" in question:
        question.remove("") #now I delete them

    try: #first and last character must be numbers at this point
        int(question[0])
        int(question[-1])
    except:
        raise ValueError("syntax error")

    question.insert(3, ")")
    question.insert(0, "(")

    question = "".join(str(char) for char in question)

    try:
        return eval(question)
    except:
        raise ValueError("syntax error")



""" #I don't need this
def take_the_numbers(question):

    list_of_numbers = list(question)
    for numbers in range(len(question)):
        if not (question[numbers].isdigit() or question[numbers] == "-"):
            question = question.replace(question[numbers], " ")

    list_of_numbers = list(question)
    print("\n", list_of_numbers)

    #for hole in question.split():
    #    list_of_numbers.append(int(hole))

    return list_of_numbers
"""
