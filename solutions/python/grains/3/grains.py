def square(number):
    if 1 <= number <=64 :
        return 2 ** (number - 1)
    """This is a docstring which 
    describes the ValueError"""
    # when the square value is not in the acceptable range
    raise ValueError("square must be between 1 and 64")


def total():
    total_grains = 0
    for squares in range(64):
        total_grains += 2 ** squares
    return total_grains
        
    
    
