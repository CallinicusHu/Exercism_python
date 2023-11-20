def transform(legacy_data):
    data = {}

    for score, letters in legacy_data.items():
        for letter in letters:
            data.update({letter.lower(): score})

    return data
