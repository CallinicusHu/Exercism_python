"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    word = "un" + word

    return word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    number_of_words = len(vocab_words)

    for a in range(1, number_of_words):
        vocab_words[a] = vocab_words[0] + vocab_words[a]

    vocab_words = " :: ".join(vocab_words)

    #print(vocab_words)

    return vocab_words

#make_word_groups(['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture'])

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    x = len(word)-4
    word = word[0: x]

    if word[-1] == "i":
        x = len(word) - 1
        word = word[0: x] + "y"

    #print(word)

    return word

#remove_suffix_ness("heaviness")

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    sentence = list(sentence.split(" "))
    #print(sentence)
    #print(sentence[index])
    nemtudommimicsoda = sentence[index]
    if nemtudommimicsoda[-1] == ("." or "," or "?" or "!"):
        x = len(nemtudommimicsoda) - 1
        nemtudommimicsoda = nemtudommimicsoda[0: x]

    nemtudommimicsoda = nemtudommimicsoda + "en"

    return nemtudommimicsoda

#adjective_to_verb("fekete macska farka barna", 1)