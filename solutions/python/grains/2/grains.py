import math

def square(number):
    if not 0 < number < 65:
        raise ValueError("square must be between 1 and 64")
    return math.pow(2, number - 1)
def total():
    return int((math.pow(2,63) * 2))-1