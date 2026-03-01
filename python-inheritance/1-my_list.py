#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """A class that inherits from list and adds custom functionality."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
