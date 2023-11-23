code = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")


def label(colors):

    ohms_str = str(((10 * code.index(colors[0])) + (code.index(colors[1]))) * pow(10, code.index(colors[2])))

    if ohms_str == "0":
        return "0 ohms"

    if ohms_str.count("0") == 9:
        return ohms_str.replace("0", "") + " gigaohms"
    if ohms_str.count("0") == 8:
        return ohms_str.replace("0", "") + "00 megaohms"
    if ohms_str.count("0") == 7:
        return ohms_str.replace("0", "") + "0 megaohms"
    if ohms_str.count("0") == 6:
        return ohms_str.replace("0", "") + " megaohms"
    if ohms_str.count("0") == 5:
        return ohms_str.replace("0", "") + "00 kilohms"
    if ohms_str.count("0") == 4:
        return ohms_str.replace("0", "") + "0 kiloohms"
    if ohms_str.count("0") == 3:
        return ohms_str.replace("0", "") + " kiloohms"
    if ohms_str.count("0") == 2:
        return ohms_str.replace("0", "") + "00 ohms"
    if ohms_str.count("0") == 1:
        return ohms_str.replace("0", "") + "0 ohms"
    if ohms_str.count("0") == 0:
        return ohms_str.replace("0", "") + " ohms"
