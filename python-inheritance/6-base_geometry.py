#!/usr/bin/python3
"""Module that defines a BaseGeometry class."""


class BaseGeometry:
    """A class for geometry-related objects."""

    def area(self):
        """Public instance method that raises an Exception.

        Raises:
            Exception: with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
