vowels = ["a", "e", "i", "o", "u"]


def translate(text):
    text_list = text.split(" ")
    for num, word in enumerate(text_list):
        if isvowel(word[0]) or word.startswith("xr") or word.startswith("yt"):
            text_list[num] = word + "ay"

        elif (len(word) == 2) and (word[1] == "y"):
            text_list[num] = word[::-1] + "ay"

        elif (not isvowel(word[0])) and (not isvowel(word[1])) and (word[2] == "y"):
            text_list[num] = word[2:] + word[:2] + "ay"

        elif not (isvowel(word[0])) and ((word[0] == "q") and (word[1] == "u")):
            text_list[num] = word[2:] + "quay"

        elif not (isvowel(word[0])) and (word[1] == "q") and (word[2] == "u"):
            text_list[num] = word[3:] + word[0] + "quay"

        elif not (isvowel(word[0])):
            count = 1
            vowel = False
            while not vowel:
                if count == len(word):
                    break
                if not (isvowel(word[count])):
                    count += 1
                else:
                    vowel = True
            text_list[num] = word[count:] + word[:count] + "ay"

    return " ".join(text_list)


def isvowel(letter):
    return letter in vowels
