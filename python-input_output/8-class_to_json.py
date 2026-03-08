#!/usr/bin/python3
"""
Module that defines a function returning the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization.

    Args:
        obj: instance of a class

    Returns:
        dict: dictionary representation of the object
    """
    return obj.__dict__
