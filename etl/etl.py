def transform(legacy_data):

    print("\n")


    values = str(list(legacy_data.values()))
    lower_values = values.lower()
    print(lower_values)
    print("\n")

    for anything in lower_values:
        if not(anything.isalpha()):
            lower_values = lower_values.replace(anything, "")

    for anything in values:
        if not (anything.isalpha()):
            values = values.replace(anything, "")

    keys = list(legacy_data.keys())

    data = {}

    for letters in range(len(lower_values)):
        print(letters)
        for score, letter in legacy_data.items():
            print(score, letter)
            if values[letters] in letter:
                fill = lower_values[letters]
                filli = score
                print("what", fill, filli)
                data.update({fill: filli})

    print("\n")
    print(keys)
    print(values)
    print(type(values))
    print(lower_values)
    print("\n")
    print(data)

    return data
    #for keys in range(len(legacy_data)):
    #    key = legacy_data.setdefault(keys)


