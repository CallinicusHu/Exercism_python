def slices(series, length):

    if series == "":
        raise ValueError("series cannot be empty")

    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    slices = []
    start = 0
    end = length
    for _ in range(start, len(series), 1):
        if len(series[start:end:]) < length:
            break
        slices.append(series[start:end:])
        start += 1
        end += 1

    return slices


