#!/usr/bin/python3
"""
Module that defines an abstract class Animal and its subclasses Dog and Cat.
Uses the ABC package to ensure proper implementation of abstract methods.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Base Class Animal.
    Cannot be instantiated directly.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method sound that must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass Dog that inherits from Animal.
    """

    def sound(self):
        """
        Implementation of the sound method for Dog.
        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass Cat that inherits from Animal.
    """

    def sound(self):
        """
        Implementation of the sound method for Cat.
        Returns:
            str: "Meow"
        """
        return "Meow"
