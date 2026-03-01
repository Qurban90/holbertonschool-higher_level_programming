#!/usr/bin/python3
"""Module that contains the is_same_class function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if obj is exactly an instance of a_class, else False.
    """
    return type(obj) is a_class
