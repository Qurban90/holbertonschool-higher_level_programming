#!/usr/bin/python3
"""Module that contains the inherits_from function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if obj is an instance of a class that inherited
        from a_class, but not the class itself. Otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
