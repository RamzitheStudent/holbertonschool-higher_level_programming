#!/usr/bin/python3
"""Defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with a private size."""

    def __init__(self, size):
        """Initialize a new Square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return string representation: [Square] <size>/<size>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
