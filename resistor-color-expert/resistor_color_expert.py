code = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
tolerance = {"grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%",
             "green": "±0.5%", "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±5%"}
suffix = {0: "ohms", 1: "kiloohms", 2: "megaohms", 3: "gigaohms"}

def resistor_label(colors):
    if len(colors) == 1:
        return f"{str(code.index(colors[0]))} {suffix[0]}"
    elif len(colors) == 4:
        ohms_str = label4(colors)
    else:
        ohms_str = label5(colors)

    if ohms_str == "0":
        return f"{ohms_str} {suffix[0]}" #aka "0 ohms"

    return f"{ohms_begins(ohms_str)}{ohms_cont(ohms_str)} {suffix[suffixcode(ohms_str)]} {tolerance.get(colors[-1])}"

def label4(colors):
    return str(
        ((10 * code.index(colors[0])) + (code.index(colors[1]))) * pow(10, code.index(colors[2])))

def label5(colors):
    return str(
        (((100 * code.index(colors[0]))) + (10 * (code.index(colors[1]))) + (code.index(colors[2]))) *
        pow(10, code.index(colors[3])))


def suffixcode(ohms_str):
    return (len(ohms_str) - 1) // 3

def ohms_begins(ohms_str):
    if len(ohms_str) % 3 == 0:
        return ohms_str[:3]
    elif len(ohms_str) % 3 != 0:
        return f"{ohms_str[:len(ohms_str) % 3]}"

def ohms_cont(ohms_str):
    if ohms_str.count('0') % 3 == 0 or len(ohms_str) < 4:
        return ""
    else:
        return f".{ohms_str[len(ohms_str) % 3:len(ohms_str) - ohms_str.count('0')]}"
