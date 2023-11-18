def transform(legacy_data):
    values = str(list(legacy_data.values()))
    lower_values = values.lower()

    for anything in lower_values:
        if not (anything.isalpha()):
            lower_values = lower_values.replace(anything, "")

    for anything in values:
        if not (anything.isalpha()):
            values = values.replace(anything, "")

    data = {}

    for letters in range(len(lower_values)):
        for score, letter in legacy_data.items():
            if values[letters] in letter:
                fill = lower_values[letters]
                filli = score

                data.update({fill: filli})

    return data
