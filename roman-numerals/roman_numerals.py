DICT = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
        20: "XX", 30: "XXX", 40: "XL", 50: "L",
        60: "LX", 70: "LXX", 80: "LXXX", 90: "XC", 100: "C",
        200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
        1000: "M", 2000: "MM", 3000: "MMM"}

def roman(number):

    spqr = ""
    strnumber = str(number)


    if number >= 1000:
        spqr += DICT[int(f"{strnumber[-4:-3:]}000")]

    if number >= 100:
        if strnumber[-3::] != "000":
            spqr += DICT[int(f"{strnumber[-3:-2:]}00")]

    if number >= 10:
        if strnumber[-2::] != "00":
            spqr += DICT[int(f"{strnumber[-2:-1:]}0")]

    if strnumber[-1::] != "0":
        spqr += DICT[int(strnumber[-1::])]

    return spqr


