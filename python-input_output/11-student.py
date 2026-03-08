#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    """
    Defines a student with first name, last name and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes contained
        in this list will be retrieved.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list):
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using values from a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
