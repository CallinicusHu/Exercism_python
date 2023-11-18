def encode(plain_text):

    plain_text = plain_text.lower()
    new_text = ""
    final_text = ""

    for counter, text in enumerate(plain_text):
        if text.isalpha():
            new_text += encode_single(text)
            print(new_text)
        if text.isdigit():
            new_text += text
            print(new_text)

    for spaces in range(0, len(new_text)):
        if (spaces > 0) and ((spaces + 1) % 5 == 0):
            final_text += new_text[spaces] + " "
        else:
            final_text += new_text[spaces]
        print(final_text)

    final_text = final_text.strip()

    print(final_text)

    return final_text

def decode(ciphered_text):
    final_text = ""

    for text in ciphered_text:
        if text.isalpha():
            final_text += decode_single(text)
        if text.isnumeric():
            final_text += text

    return final_text

def encode_single(letter):

    abc = "abcdefghijklmnopqrstuvwxyz"
    zyx = "zyxwvutsrqponmlkjihgfedcba"

    letter = zyx[abc.index(letter)]

    return letter

def decode_single(letter):

    abc = "abcdefghijklmnopqrstuvwxyz"
    zyx = "zyxwvutsrqponmlkjihgfedcba"

    letter = abc[zyx.index(letter)]

    return letter