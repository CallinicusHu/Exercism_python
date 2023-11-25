def translate(text):

    if isvowel(text[0]) or text.startswith("xr") or text.startswith("yt"):
        return text + "ay"

def isvowel(letter):
    return letter == "a" or "e" or "i" or "o" or "u"
