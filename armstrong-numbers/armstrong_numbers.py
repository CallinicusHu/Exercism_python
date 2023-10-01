def is_armstrong_number(number):

    digits = number

    digits = [int(x) for x in str(digits)]
    #ezt nem értem micsoda és hogy működik, listát csinál a számból, de próbáltam saját fort írni és nem ment

    long = len(digits) #megméri a listám hosszát
    
    count = 0

    part = 0

    while count < long:
        part = part + (digits[count-1] ** long)
        count = count + 1
    
    if part == number:
        return True
    
    
    return False
