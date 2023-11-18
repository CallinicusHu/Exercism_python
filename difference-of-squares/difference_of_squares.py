def square_of_sum(number):

    squaresum = 0

    for summa in range(1, number + 1):
        squaresum += summa

    squaresum = squaresum ** 2

    return squaresum


def sum_of_squares(number):
    sumsquare = 0

    for square in range(1, number + 1):
        sumsquare += square ** 2

    return sumsquare


def difference_of_squares(number):
    return abs(sum_of_squares(number)-square_of_sum(number))
