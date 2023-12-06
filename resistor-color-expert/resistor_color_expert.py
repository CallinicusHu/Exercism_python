code = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
tolerance = {"grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%",
             "green": "±0.5%", "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±5%"}
suffix = {0: " ohms", 1: " kiloohms", 2: " megaohms", 3: " gigaohms"}
print()


def resistor_label(colors):
    if len(colors) == 1:
        return str(code.index(colors[0])) + " ohms"
    if len(colors) == 4:
        return label4(colors)
    if len(colors) == 5:
        return label5(colors)


def label4(colors):
    ohms_str = str(((10 * code.index(colors[0])) + (code.index(colors[1]))) * pow(10, code.index(colors[2])))

    if ohms_str == "0":
        return "0 ohms"

    suffix_code = suffixcode(ohms_str)
    zeros = zerocount(ohms_str)
    ohms_str = removezeros(ohms_str)

    if len(ohms_str) + zeros == 4:
        return f"{ohms_str[:len(ohms_str) - 1]}.{ohms_str[len(ohms_str) - 1:]}{suffix.get(suffix_code + 1)} {tolerance.get(colors[3])}"
    else:
        return f"{ohms_str}{'0' * zeros}{suffix.get(suffix_code)} {tolerance.get(colors[3])}"


def label5(colors):
    ohms_str = str(
        (((100 * code.index(colors[0]))) + (10 * (code.index(colors[1]))) + (code.index(colors[2]))) *
        pow(10, code.index(colors[3])))

    if ohms_str == "0":
        return "0 ohms"

    print(ohms_str)

    suffix_code = suffixcode(ohms_str)
    zeros = zerocount(ohms_str)
    ohms_str = removezeros(ohms_str)

    print(ohms_str)

    if len(ohms_str) + zeros > 3:
        return f"{ohms_str[:len(ohms_str) - 2]}.{ohms_str[len(ohms_str) - 2:]}{suffix.get(suffix_code + 1)} {tolerance.get(colors[4])}"
    else:
        return f"{ohms_str}{'0' * zeros}{suffix.get(suffix_code)} {tolerance.get(colors[4])}"


def suffixcode(ohms_str):
    return ohms_str.count("0") // 3


def zerocount(ohms_str):
    return ohms_str.count("0") % 3


def removezeros(ohms_str):
    return ohms_str.replace("0", "")
