
onepoint = dict.fromkeys(("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"), 1)
twopoint = dict.fromkeys(("D", "G"), 2)
threepoint = dict.fromkeys(("B", "C", "M", "P"), 3)
fourpoints = dict.fromkeys(("F", "H", "V", "W", "Y"), 4)
morepoints = {"K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}

scoring = {**onepoint, **twopoint, **threepoint, **fourpoints, **morepoints}

def score(word):
    return sum([scoring.get(letter.upper()) for letter in word])
