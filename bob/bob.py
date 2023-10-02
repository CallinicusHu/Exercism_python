def response(hey_bob):
    """
    bob = hey_bob.strip()

    reply = ["Sure.", "Whoa, chill out!", "Calm down, I know what I'm doing!", "Fine. Be that way!", "Whatever."]
  
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
    """
   
    if len(hey_bob.strip()) < 1: return "Fine. Be that way!"
    elif (hey_bob.strip()[-1] == "?") and hey_bob.isupper(): return "Calm down, I know what I'm doing!"
    elif hey_bob.strip()[-1] == "?":return "Sure."
    elif hey_bob.isupper(): return "Whoa, chill out!"
    else: return "Whatever."