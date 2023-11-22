code = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
def label(colors): #["red", "black", "red"] still fails


    ohms = ((10 * code.index(colors[0])) + (code.index(colors[1]))) * pow(10, code.index(colors[2]))
    ohms_str = str(ohms)

    if ohms == 0:
        return "0 ohms"

    if ohms % 1_000_000_000 == 0: #"white":
        return str(ohms_str[:2]) + " gigaohms"
    if ohms % 100_000_000 == 0: #"grey":
        return str(ohms_str[:2]) + "00 megaohms"
    if ohms % 10_000_000 == 0: #"violet":
        return str(ohms_str[:2]) + "0 megaohms"
    if ohms % 1_000_000 == 0: #"blue":
        return str(ohms_str[:2]) + " megaohms"
    if ohms % 100_000 == 0: #"green":
        return str(ohms_str[:2]) + "00 kilohms"
    if ohms % 10_000 == 0: #"yellow":
        return str(ohms_str[:2]) + "0 kiloohms"
    if ohms % 1000 == 0: #"orange":
        return str(ohms_str[:2]) + " kiloohms"
    if ohms % 100 == 0: #"red":
        return str(ohms_str[:2]) + "00 ohms"
    if ohms % 10 == 0: #"brown":
        return str(ohms_str[:2]) + "0 ohms"
    if ohms % 1 == 0: #"black":
        return str(ohms_str[:2]) + " ohms"
    
