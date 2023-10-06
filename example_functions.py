# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

def my_adder(a: int | float, b: int | float, c: int | float) -> int | float:
    """Computes the sum

    This function adds the three numbers given.

    Args:
        a: A number, integer of float
        b: A number, integer of float
        c: A number, integer of float
    
    Returns:
        The sum of a, b, and c as float, or as an integer if the three where integers.
    """
    
    # this is the summation
    out = a + b + c
    
    return out


def my_thermo_stat(temp: int, desired_temp: int) -> str:
    """Determines the status of thermostat
    
    This function determines the status of the thermostat based on temperature and desired temperature.

    Args:
        temp: Current temperature as an integer
        desired_temp: Desired temperature as an integer
    
    Returns:
        A string with the status of the thermostat.
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status

 
def have_digits(s: str) -> bool:
    """Checks if a string has digits in it

    Args:
        s: A string
    
    Returns:
        A boolean telling whether the string given has any digits (numbers) in it.
    """
    
    out = 0
    
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out
    
 
