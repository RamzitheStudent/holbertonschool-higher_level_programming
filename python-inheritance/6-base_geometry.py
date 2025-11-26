#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class with an unimplemented area method."""

    def area(self):
        """Raise an exception for unimplemented area method."""
        raise Exception("area() is not implemented")
