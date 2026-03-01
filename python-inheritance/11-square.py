#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
(Based on 10-square.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        Format: [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
