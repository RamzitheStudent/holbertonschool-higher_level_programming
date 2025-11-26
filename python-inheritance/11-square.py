#!/usr/bin/python3
"""Defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with private size, inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return string representation: [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
