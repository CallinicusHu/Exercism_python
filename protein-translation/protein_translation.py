def proteins(strand):
    print("\n")
    codons = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    } #is there a simppler way than defining this dictionary?

    proteins = []
    strand_list = []
    print(proteins)
    for thirds in range(0, len(strand), 3):
        strand_list.append(strand[thirds:thirds+3])

    print(strand_list)
    print(proteins)
    for part in strand_list:
        if codons[part] == "STOP":
            return proteins
        if part in codons:
            proteins.append(codons[part])

    print(proteins)

    return proteins
