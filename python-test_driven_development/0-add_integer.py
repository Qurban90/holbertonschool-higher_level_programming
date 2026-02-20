#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).
    Raises TypeError if a or b are not integers/floats, or if they are NaN/Inf.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a != a or abs(a) > 1.7976931348623157e+308:
        raise TypeError("a must be an integer")
    if b != b or abs(b) > 1.7976931348623157e+308:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
