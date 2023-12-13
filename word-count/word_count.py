def count_words(sentence):
    for char in sentence:
        if not char.isalnum():
            sentence = sentence.replace(char, " ")

    sentence = sentence.lower().replace(" t ", "'t ").replace(" re ", "'re ").replace(" s ", "'s ").split()

    counted = {}
    for word in sentence:
        counted[word] = counted.get(word, 0) + 1

    return counted
