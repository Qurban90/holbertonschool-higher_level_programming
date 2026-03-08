#!/usr/bin/python3
"""
Module that defines a function to create an object
from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        object: Python data structure from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
