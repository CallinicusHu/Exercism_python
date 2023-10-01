def steps(number):

    n = number
    count = 0

    if n < 1:
        raise ValueError("Only positive integers are allowed")

    while n != 1: 
        if ( n % 2 ) != 0:
            n = n * 3 + 1
            
        else:
            n = n / 2
            
        count = count + 1
        
    
 
    return count
