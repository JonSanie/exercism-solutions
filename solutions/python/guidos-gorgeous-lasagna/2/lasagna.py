"""Lasagna functions"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(in_oven: int):
    """Calculate the bake time remaining.
    
    Parameters:
        in_oven (int): The time the lasagna has been baking.
        
    Returns:
        int: The remaining bake time based on EXPECTED_BAKE_TIME.
    """

    return EXPECTED_BAKE_TIME - in_oven

def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the preparation time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        
    Returns:
        int: The total preparation time in minutes.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.

    Returns:
        int: The total time elapsed (in minutes) preparing and baking.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time
