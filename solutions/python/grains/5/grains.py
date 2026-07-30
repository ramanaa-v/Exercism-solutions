"""Calculate the number of grains of wheat on a chessboard"""

def square(number):
    """Return the number of grains
    on a given square."""
    if 1 <= number <= 64:
        return 1 << number - 1
        # or: return 2 ** (number - 1)
        # or: return pow(2, number - 1)

    # when the square value is not in the acceptable range
    raise ValueError("square must be between 1 and 64")


def total():
    """Return the total number of grains
    on the chess board."""
    return (1 << 64) - 1
    # or: return 2 ** 64 - 1
    # or: return pow(2, 64) - 1
    
    
