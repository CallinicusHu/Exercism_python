"""code = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }"""

code = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

#works both with the dict and the list, list only as long the order is not changed (tuple would be safer?)

def color_code(color):
    #return code.get(color)
    return code.index(color)

def colors():
    #return list(code.keys())
    return code
