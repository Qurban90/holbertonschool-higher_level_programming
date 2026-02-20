#!/usr/bin/python3
"""
This is the "4-print_square" module.
It provides one function, print_square(size).
"""


def print_square(size):
    """
    Prints a square with the character #.
    Args:
        size: the length of the square's side.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        if not isinstance(size, float):
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
