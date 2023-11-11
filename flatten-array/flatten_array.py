def flatten(iterable):

    final = []

    for leng in range(len(iterable)):
        if iterable[leng] or iterable[leng] == 0:
            final.append(iterable[leng])

    print(f"\n{final}")

    return final