def is_pangram(sentence):
    abc = "abcdefghijklmnopqrstuvwxyz"

    for pangram in abc:
        if not(pangram in sentence.lower()):
            return False


    return True
