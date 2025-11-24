#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Student class with first_name, last_name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
       	self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of Student.
        If attrs is a list of strings, return only those attributes.
        Otherwise return all attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        using values from the json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
