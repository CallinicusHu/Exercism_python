def response(hey_bob):

    bob = hey_bob.strip()

    reply = ["Sure.", "Whoa, chill out!", "Calm down, I know what I'm doing!", "Fine. Be that way!", "Whatever."]

    x = 5
    


    if len(bob) < 1:
        x = 3
    
    elif (bob[-1] == "?") and hey_bob.isupper():
        x = 2
    
    elif bob[-1] == "?":
        x = 0

    elif bob.isupper():
        x = 1
    
    else:
        x = 4


    
    return reply[x]
