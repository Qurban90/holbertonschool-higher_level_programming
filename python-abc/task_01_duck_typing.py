#!/usr/bin/python3
"""
This module defines an abstract class Shape and its subclasses
Circle and Rectangle, demonstrating ABC and duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract Base Class Shape.
    Defines blueprint for area and perimeter.
    """

    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter."""
        pass


class Circle(Shape):
    """Concrete class Circle."""

    def __init__(self, radius):
        """Initializes Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculates area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class Rectangle."""

    def __init__(self, width, height):
        """Initializes Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape.
    Relies on duck typing (calls methods without type checking).
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
