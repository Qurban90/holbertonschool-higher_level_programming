#!/usr/bin/python3
"""
This module demonstrates the Mixin pattern in Python.
It defines SwimMixin, FlyMixin, and a Dragon class that uses both.
"""


class SwimMixin:
    """Mixin that provides swimming functionality."""

    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying functionality."""

    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from both SwimMixin and FlyMixin.
    Also has its own unique roar method.
    """

    def roar(self):
        """Prints roaring message."""
        print("The dragon roars!")
