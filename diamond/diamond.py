def rows(letter):
    abc = "abcdefghijklmnopqrstuvwxyz".upper()
    where = abc.index(letter)  # the index position of the given letter in alphabet, B = 1
    size = max(where * 2 + 1, 1)  # this is how many columns and lines the diamond should have

    diamond = f"{' ' * where}A{' ' * where}\n" # first A line with spaces

    for build in range(size - 2):
        diamond += f"{' ' * size}\n" # body of the diamond with spaces

    if where > 0:
        diamond += f"{' ' * where}A{' ' * where}\n" # last A line with spaces

    size += 1 #lines got 1 index longer because of \n

    for count, build in enumerate(range(size, size * (where + 1), size)):
        position = build + where - count - 1
        diamond = f"{diamond[:position]}{abc[count + 1]}{diamond[position + 1:]}"
        position = build + where + count + 1
        diamond = f"{diamond[:position]}{abc[count + 1]}{diamond[position + 1:]}"

    for count, build in enumerate(range((size * (size - 2)), (size * (round(size / 2)) + 1), -size)):
        position = build - where + count - 1
        diamond = f"{diamond[:position]}{abc[count + 1]}{diamond[position + 1:]}"
        position = build - where - count - 3 # I have no idea why is this -3 but it is
        diamond = f"{diamond[:position]}{abc[count + 1]}{diamond[position + 1:]}"

    print(f"\n{diamond}\n") # At this point we print out the diamond shape I think the exercise described.

    diamond = diamond.replace("\n", "") # actual task does not require linebreaks
    size -= 1

    diamond_list = []

    for rebuild in range(0, len(diamond), size):
        diamond_list.append(diamond[rebuild:rebuild+size])

    print(diamond_list) # At this point we print out the diamond shape I think the exercise expects.

    return diamond_list

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
