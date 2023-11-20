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
    for spaces in range(0, len(plain_text)):
        if (spaces > 0) and ((spaces + 1) % 5 == 0):
            new_text.append(plain_text[spaces] + " ")
        else:
            new_text.append(plain_text[spaces])

    plain_text = "".join(new_text).rstrip()

    return plain_text

def decode(ciphered_text):
    decoded = str.maketrans(zyx, abc, " ")
    ciphered_text = ciphered_text.translate(decoded)
    return ciphered_text
