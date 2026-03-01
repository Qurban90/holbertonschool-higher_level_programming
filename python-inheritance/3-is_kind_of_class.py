#!/usr/bin/python3
"""Module that contains the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if obj is an instance or inherited instance, else False.
    """
    return isinstance(obj, a_class)
