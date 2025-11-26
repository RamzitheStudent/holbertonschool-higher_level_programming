#!/usr/bin/python3
"""Defines a Rectangle class inheriting from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with private width and height."""

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
