def rows(letter):

    abc = "abcdefghijklmnopqrstuvwxyz".upper()
    where = abc.index(letter) # the index position of the given letter in alphabet, B = 1
    size = max(where * 2 + 1, 1) #this is how many columns and lines the diamond should have
    print("\n")
    print(where)
    print(size)

    diamond = f"{"-" * where}A{"-" * where}\n"

    for build in range(size - 2):
        diamond += f"{"-" * size}\n"

    if where > 0:
        diamond += f"{"-" * where}A{"-" * where}"

    print("\n")
    print(diamond)
    print("\n")

    print("size * size: ", size * size, "\n", len(diamond))
    print("\n")

    for build in range((size+1), (size+1)*size, size+1):
        diamond = diamond.replace(diamond[build], abc[1])
        print(build)

    print(diamond)

"""
What the exercise describes:
    A    
   B B   
  C   C  
 D     D 
E       E
 D     D 
  C   C  
   B B   
    A    
    
What the exercise actually expects:
["  A  ", " B B ", "C   C", " B B ", "  A  "]
"""