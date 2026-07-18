"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 0

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    Parameters:
        number_of_layers (int): takes the number_of_layers you want to add to the lasagna and multiplys by 2.           Assume each layer takes 2 minutes to prepare.
        
    Returns:
        int: The prepare time (in minutes) derived from number_of_layers * 2.

    Function that takes the number of layers one wants to add to the lasagna as
    an argument and returns how many minutes the preparation time will take.
    """
    PREPARATION_TIME = number_of_layers*2
    return PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate the total elapsed time for baking & prepping.

    Parameters:
        number_of_layers (int): takes the number_of_layers you want to add to the lasagna and multiplys by 2.           Assume each layer takes 2 minutes to prepare.
        elapsed_bake_time (int): The baking time already elapsed added to the preparation time derived from
        number_of_layers * 2

    Returns:
        int: The elapsed time (in minutes) derived from number_of_layers * 2 + elapsed_bake_time.

    Function that calculates the preparation time and adds it to the elapsed time to return the minutes spent
    in the kitchen.
    """
    return number_of_layers*2 + elapsed_bake_time


#  (you can copy and then alter the one from bake_time_remaining.)
