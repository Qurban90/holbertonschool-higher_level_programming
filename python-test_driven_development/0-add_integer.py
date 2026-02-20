#!/usr/bin/python3
"""
This is the "0-add_integer" module.
It provides one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).
    Args:
        a: first number
        b: second number, default 98
    Returns:
        Sum of a and b as an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
