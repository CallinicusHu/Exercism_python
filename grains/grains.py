def square(number):
    # when the square value is not in the acceptable range        
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64") 

    return 2 ** (number-1)

def total():
    return 2 ** 64 - 1 
