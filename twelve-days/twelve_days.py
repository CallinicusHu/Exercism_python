day = ["first", "second", "third", "fourth", "fifth", "sixth",
       "seventh", "eights", "ninths", "tenth", "elevenths", "twelfth"]
gifts = ["a Partridge in a Pear Tree.",
         "two Turtle Doves, ",
         "three French Hens, ",
         "four Calling Birds, ",
         "five Gold Rings, ",
         "six Geese-a-Laying, ",
         "seven Swans-a-Swimming, ",
         "eight Maids-a-Milking, ",
         "nine Ladies Dancing, ",
         "ten Lords-a-Leaping, ",
         "eleven Pipers Piping, ",
         "twelve Drummers Drumming, "]

def recite(start_verse, end_verse):


    song = []

    for verse in range(start_verse - end_verse + 1):
        song.append(f"On the {day[start_verse - end_verse + verse]} day of Christmas my true love gave to me: ")
        song.append(f"{presents(start_verse, end_verse)}")

    print("\n")
    print(song)

    return song

def presents(start_verse, end_verse):
    return "and ".join(gifts[item - 1] for item in range(end_verse, 0, -1))
