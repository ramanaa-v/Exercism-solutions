"""Calculate the number of grains of wheat on a chessboard"""
def square(number):
    """Return the number of grains
    on a given square."""
    if 1 <= number <= 64:
        return 2 ** (number - 1)

    # when the square value is not in the acceptable range
    raise ValueError("square must be between 1 and 64")


def total():
    """Return the total number of grains
    on the chess board."""
    total_grains = 0
    for square_number in range(64):
        total_grains += 2 ** square_number
    return total_grains
    
    
