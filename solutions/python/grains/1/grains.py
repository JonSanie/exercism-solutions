"""Grains of wheat on a chessboard"""

def square(number):
    """Calculates grains for any indivdual square"""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    return 2 ** (number - 1)


def total():
    """Calculates total grains on the entire board"""
    return 2 ** 64 - 1
