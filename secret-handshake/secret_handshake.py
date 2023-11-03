def commands(binary_str):

    # I actually didn't need these
    """
    wink = [0, 0, 0, 0, 1] #00001 = wink
    double = [0, 0, 0, 1, 0] # 00010 = double
    blink = [0, 0, 1, 0, 0]  #  00100 = close your eyes
    jump = [0, 1, 0, 0, 0] # 01000 = jump
    reverse = [1, 0, 0, 0, 0] # 10000 = Reverse the order of the operations in the secret handshake.
    """
    # I actually didn't need these

    # this works but I don't like it
    """
    if binary_str[4] == "1":
        handshake.append("wink")

    if binary_str[3] == "1":
        handshake.append("double blink")

    if binary_str[2] == "1":
        handshake.append("close your eyes")

    if binary_str[1] == "1":
        handshake.append("jump")

    if binary_str[0] == "1":
        handshake.reverse()
        
    """
    # this works but I don't like it
    #however this have the lest amount of variables needed to operate

    #better?
    """
    for ind, one in enumerate(binary_str):
        if one == "1":
            if ind == 0:
                handshake.append("wink")
            if ind == 1:
                handshake.append("double blink")
            if ind == 2:
                handshake.append("close your eyes")
            if ind == 3:
                handshake.append("jump")
            if ind == 4:
                handshake.reverse()
    """
    # better?


    handshake = []

    binary_str = list(binary_str)
    binary_str.reverse()

    print(binary_str)

    secret = ["wink", "double blink", "close your eyes", "jump"]

    for ind, one in enumerate(secret):
        if "1" == binary_str[ind]:
            handshake.append(one)

    if binary_str[4] == "1":
        handshake.reverse()

    # fewer lines but more (+1) variables and not fewer processes run through

    print(handshake)
    return handshake

commands("10011")