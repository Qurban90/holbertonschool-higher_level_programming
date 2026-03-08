#!/usr/bin/python3
"""
Module that defines a function to convert a JSON string
to a Python object.
"""
import json


def from_json_string(my_str):
    """
    Returns the Python data structure represented by a JSON string.

    Args:
        my_str (str): JSON string.

    Returns:
        object: Python representation of the JSON string.
    """
    return json.loads(my_str)
