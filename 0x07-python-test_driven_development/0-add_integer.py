#!/usr/bin/python3
"""function that add two integers"""


def add_integer(a, b=98):
    """
    Args:
        a (int): The first parameter.
        b (int): The second parameter. Defaults to 98.

    Returns:
        sum: Sum of a and b.

    Raises:
        TypeError: if a or b are not integers or floats

    """
    sum = 0
    if type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)


    if not type(a) is int:
        raise TypeError("a must be an integer")
    elif not type(b) is int:
        raise TypeError("b must be an integer")

    sum = a + b
    return sum
