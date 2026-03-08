#!/usr/bin/python3
"""
Module that defines a function that reads a UTF8 text file
and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): name of the file to read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
