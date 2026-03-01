#!/usr/bin/python3
"""Module that contains the lookup function."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings containing attributes and methods.
    """
    return dir(obj)
