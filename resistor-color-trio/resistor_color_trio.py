code = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")


def label(colors):

    ohms_str = str(((10 * code.index(colors[0])) + (code.index(colors[1]))) * pow(10, code.index(colors[2])))

    if ohms_str == "0":
        return "0 ohms"

    suffix_code = ohms_str.count("0") // 3
    zeros = ohms_str.count("0") % 3
    suffix = {0: " ohms", 1: " kiloohms", 2: " megaohms", 3: " gigaohms"}
    ohms_str = ohms_str.replace("0", "")

    return f"{ohms_str}{'0' * zeros}{suffix.get(suffix_code)}"

