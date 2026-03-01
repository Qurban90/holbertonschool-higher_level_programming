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
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:  # <--- Burada <= olmalıdır, təkcə < yox
            raise ValueError("{} must be greater than 0".format(name))
