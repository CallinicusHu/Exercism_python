def find_anagrams(word, candidates):

    print("\n")
    print(word)
    print(candidates)

    anagrams = []

    for this, first in enumerate(candidates):
        if first.lower() == word.lower():
            candidates.pop(this)

    word_a = word.lower()
    candidates_a = [char.lower() for char in candidates]

    print(candidates)

    word_a = list(word_a)
    candidates_a = [list(item) for item in candidates_a]

    word_a.sort()

    for count in range(len(candidates_a)):
        candidates_a[count].sort()
        #print(candidates_a[count], "and", word_a)

        if candidates_a[count] == word_a:
            anagrams.append(candidates[count])


    #print(word_a)
    #print(candidates_a)
    #print(anagrams)

    return anagrams

