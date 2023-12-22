scoring = {**(dict.fromkeys(("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"), 1)),
           **(dict.fromkeys(("B", "C", "M", "P"), 3)),
           **(dict.fromkeys(("F", "H", "V", "W", "Y"), 4)),
           **{"K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10, "D": 2, "G": 2}}

def score(word):
    return sum([scoring.get(letter.upper()) for letter in word])