def flatten(iterable):

    final = []

    while iterable: # amíg van tartlama az iterablenek
        for length in range(len(iterable)): #menjen végig az iterable hosszán
            if iterable[length] or iterable[length] == 0: #ha az iterable aktuális eleme létezik vagy 0
                final.append(iterable[length].pop) # adja hozzá a finalhöz az iterable aktuális elemét amit ezzel töröl is az iterableből
    #végtelen ciklus indexerror typeerror minden baja van

    print(f"\n{final}")

    return final

flatty = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
#flatten(flatty)