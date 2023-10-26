"""Functions to help edit essay homework using string manipulation."""

"""
Vagy én felejtettem el hogy kell hibát olvasni, tesztelni pycharmban ami könnyen lehet, vagy az excercismen máshogy jelenik meg az eredmény mint pycharmban. :-(
"""
def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    return title.title()
# megtaláltam ezt a .title()t de arra nem jöttem rá hogy lehet-e upperrel specifikus karaktert nagyra cserélni vagy hogy azonosítom be az új szó elejét amit cserélni kell


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    sentence = list(sentence)
    if sentence[-1] == ".":
        return True
    else:
        return False


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    sentence = sentence.lstrip().rstrip()
    #ez is működik de megint az hiányzik nekem hogy nem tudom megállapítani hogy van-e az elején/végén szóköz és hány

    return sentence


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    return sentence.replace(old_word, new_word)
