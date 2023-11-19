def square_root(number):
    root = 1
    while not((root ** 2) == number):
        root += 1
    return root
