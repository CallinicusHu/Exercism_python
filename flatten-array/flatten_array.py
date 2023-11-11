def flatten(iterable):

    """
    final = []

    while iterable: # amíg van tartlama az iterablenek
        for length in range(len(iterable)): #menjen végig az iterable hosszán
            if iterable[length] or iterable[length] == 0: #ha az iterable aktuális eleme létezik vagy 0
                final.append(iterable.pop(length)) # adja hozzá a finalhöz az iterable aktuális elemét amit ezzel töröl is az iterableből
    #végtelen ciklus indexerror typeerror minden baja van

    print(f"\n{final}")
    """


    final = []
    tempor = iterable.copy()
    print(iterable)
    #print(tempor)

    for next_in_iterable in range(len(iterable)):
        if type(iterable[next_in_iterable]) != list:
            if iterable[next_in_iterable] or iterable[next_in_iterable] == 0:
                final.append(iterable[next_in_iterable])
        else:
            final.append(deep(iterable[next_in_iterable]))

    print(final)

    return final

def deep(zoom):

    for next in range(len(zoom)):
        if type(zoom[next]) != list:
            if zoom[next] or zoom[next] == 0:
                return zoom[next] # ha a next nem lista tegye a final végére a 26on
        else:
            deep(next) # ha next lista menjen újra amíg nem az

    print("zoom", zoom)
    return

flatty = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
flatten(flatty)