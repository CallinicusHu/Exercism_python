import string

def rows(letter):

    abc = string.ascii_uppercase
    position = abc.index(letter)
    size = position * 2 + 1
    diamond = [abc[0].center(size)]

    if position > 0:
        for line in range(position):
            diamond.append(f"{abc[line + 1]}{' ' * ((line * 2) + 1)}{abc[line + 1]}".center(size))
        for line in range(position, 0, -1):
            diamond.append(diamond[line - 1][::-1])

    return diamond

    """
    print("\n")
    abc = string.ascii_uppercase
    where = abc.index(letter)  # the index position of the given letter in alphabet, B = 1

    diamond = f"{' ' * where}A{' ' * where}\n" # first A line with spaces

    for build in range(0, where):
        letter = abc[build + 1]
        position = (where - build -1)
        diamond += f"{' ' * position}{letter}{' ' * ((build*2) + 1)}{letter}{' ' * position}\n"

    for build in range((where -2), -1, -1):
        letter = abc[build + 1]
        position = (where - build - 1)
        diamond += f"{' ' * position}{letter}{' ' * ((build*2) + 1)}{letter}{' ' * position}\n"

    if where > 0:
        diamond += f"{' ' * where}A{' ' * where}\n" # last A line with spaces

    print(diamond)

    return diamond.splitlines()
    """

    """
    print("\n")
    abc = "abcdefghijklmnopqrstuvwxyz".upper()
    where = abc.index(letter)  # the index position of the given letter in alphabet, B = 1
    size = max(where * 2 + 1, 1)  # this is how many columns and lines the diamond should have

    diamond = f"{' ' * where}A{' ' * where}\n" # first A line with spaces


    #for build in range(size - 2):
    #    diamond += f"{' ' * size}\n" # body of the diamond with spaces
    for build in range(0, where):
        letter = abc[build + 1]
        position = (where - build -1)
        diamond += f"{' ' * position}{letter}{' ' * ((build*2) + 1)}{letter}{' ' * position}\n"

    for build in range((where -2), -1, -1):
        letter = abc[build + 1]
        position = (where - build - 1)
        diamond += f"{' ' * position}{letter}{' ' * ((build*2) + 1)}{letter}{' ' * position}\n"


    if where > 0:
        diamond += f"{' ' * where}A{' ' * where}\n" # last A line with spaces
    """
    """
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
    """
    """
    print(f"\n{diamond}\n") # At this point we print out the diamond shape I think the exercise described.

    #diamond = diamond.replace("\n", "") # actual task does not require linebreaks
    #size -= 1

    diamond_list = diamond.splitlines()

    #for rebuild in range(0, len(diamond), size):
    #    diamond_list.append(diamond[rebuild:rebuild+size])

    print(diamond_list) # At this point we print out the diamond shape I think the exercise expects.

    return diamond_list
    """

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
