def abbreviate(words):
    for char in words:
        if char == "'":
            words = words.replace(char, "")
        elif not char.isalnum():
            words = words.replace(char, " ")

    words = words.split()

    return "".join([word[0].upper() for word in words])
