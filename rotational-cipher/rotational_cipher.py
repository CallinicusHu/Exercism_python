def rotate(text, key):

    alphabet = tuple("abcdefghijklmnopqrstuvwxyz")
    bigabet = tuple(("abcdefghijklmnopqrstuvwxyz").upper())
    text = list(text)

    cipher = []

    for char in text:
        if char.isupper():
            cipher.append(bigabet[i_dont_like_this(bigabet.index(char), key)])
        elif char.islower():
            cipher.append(alphabet[i_dont_like_this(alphabet.index(char), key)])
        else:
            cipher.append(char)
        #print(cipher)

    cipher = "".join(char for char in cipher)
    #print(cipher)

    return cipher

def i_dont_like_this(indec, key):
    "calculate rotated index"

    #print("index", indec)
    #print("key", key)

    true_index = indec + key

    while true_index >= 26:
        true_index -= 26

    return true_index

#y = rotate("!Corgi!", 3)
#print(y)