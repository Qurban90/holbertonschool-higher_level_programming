#!/usr/bin/env python3
"""
Module that demonstrates serialization and deserialization
of a custom Python object using pickle.
"""
import pickle


class CustomObject:
    """
    Custom object with serialization support.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file and return it.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
