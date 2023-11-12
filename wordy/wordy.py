def answer(question):
    question = question.split()
    question.pop(0)
    question.pop(0)
    question[-1] = question[-1].rstrip("?")
    print("\n")

    for index, numbers in enumerate(question):
        if numbers == "plus":
            question[index] = "+"

        if numbers == "minus":
            question[index] = "-"

        if numbers == "multiplied":
            question[index] = "*"
            question[index + 1] = ""

        if numbers == "divided":
            question[index] = "/"
            question[index + 1] = ""

    print(question)

    question = "".join(str(char) for char in question)
    print(question)

    return eval(question)


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
