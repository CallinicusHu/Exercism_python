import string

abc = string.ascii_lowercase
zyx = abc[::-1]

def encode(plain_text):
    plain_text = "".join(ch for ch in plain_text if ch.isalnum()).lower()
    encoded = str.maketrans(abc, zyx)
    plain_text = plain_text.translate(encoded)

    if len(plain_text) < 6:
        return plain_text

    new_text = []
    for fifths in range(0, len(plain_text), 5):
        new_text.append(plain_text[fifths:fifths+5])

    return " ".join(new_text).rstrip()

def decode(ciphered_text):
    decoded = str.maketrans(zyx, abc, " ")

    return ciphered_text.translate(decoded)
