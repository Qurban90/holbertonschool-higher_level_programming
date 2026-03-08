#!/usr/bin/python3
"""
Module that defines a function that writes a string to a text file (UTF-8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns
    the number of characters written.

    Args:
        filename (str): name of the file
        text (str): text to write into the file

    Returns:
        int: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
