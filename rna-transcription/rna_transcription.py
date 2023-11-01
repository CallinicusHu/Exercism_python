def to_rna(dna_strand):
    dna = ["G", "C", "T", "A"]
    rna = ["C", "G", "A", "U"]
    dna_strand = list(dna_strand)

    find = 0

    for index, find in enumerate(dna_strand):
        for got, this in enumerate(dna):
            if find == this:
                dna_strand[index] = rna[got]

    dna_strand = "".join(ch for ch in dna_strand)

    #káromkodás-káromkodás, egyszerűen nem látom mikor melyik típusra milyen műveletek működnek, itt a str, list, list of strings, amin a hajamat tépem, melyikben hogy és mikor és mire működik az indexelés

    #fail4
    """
    if dna_strand[0] == dna[0]:
        dna_strand.replace(dna[0], rna[0])

    if dna_strand[1] == dna[1]:
        dna_strand.replace(dna[1], rna[1])

    if dna_strand[2] == dna[2]:
        dna_strand.replace(dna[2], rna[2])

    if dna_strand[3] == dna[3]:
        dna_strand.replace(dna[3], rna[3])
    """
    #fail3
    """
    print(dna_strand)
    place = 0
    for got, find in enumerate(dna_strand):
        print(got, find)
        place = dna.index(find)
        dna_strand[got] = rna[place]
        print(dna_strand)

    """
    #fail2
    """
    for index, find in enumerate(dna_strand):
        print(index, find)
        place = dna.index(find)
        print(place)
        dna_strand.replace(dna_strand[index], rna[place])

    """
    #fail1
    """
    for index, find in enumerate(dna_strand):
        place = dna.index(find)
        dna_strand = dna_strand.replace(dna_strand[index], rna[place])
        print(dna_strand)
        
    """
    #fail0
    """
    for count, char in enumerate(dna_strand):
        print(count, char)
        for index, find in enumerate(dna):
            print(index, find)
            if dna[index] == find:
                dna_strand = dna_strand.replace(dna[index], rna[index])
                print(dna[index], dna_strand[count], rna[index], dna_strand)
    """

    return dna_strand
