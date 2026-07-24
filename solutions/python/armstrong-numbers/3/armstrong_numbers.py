"""Module to evaluate if a given number is an Armstrong number."""

def is_armstrong_number(number):
    """Return True if number is an Armstrong number, otherwise False.
    
    Parameter:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, otherwise False.
    """
    
    number_as_string = str(number) 
    digits = len(number_as_string) 
    number_splitted = tuple(number_as_string) 
    number_sum = 0
    
    for digit in number_splitted:
        number_sum += int(digit)**digits

    return number == number_sum