#!/usr/bin/python3
"""
Module that defines a function to append text to a file
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF8 text file.

    Args:
        filename (str): Name of the file.
        text (str): Text to append.

    Returns:
        int: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
