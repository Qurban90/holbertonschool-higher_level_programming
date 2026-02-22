#!/usr/bin/python3
"""Module that defines a square."""


class Square:
    """Class that represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
