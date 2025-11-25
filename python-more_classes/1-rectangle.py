#!/usr/bin/python3
class Rectangle:
    """Defines a rectangle with width and height, managed via properties."""

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        # Assigning values here automatically calls the setter properties defined below.
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the private instance attribute __width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the private instance attribute __width with validation.
        The setter method is decorated with "@width.setter" [3, 4].
        """
        if not isinstance(value, int):
            # Check if the value is an integer, otherwise raise TypeError
            raise TypeError("width must be an integer")
        if value < 0:
            # Check if the value is non-negative, otherwise raise ValueError
            raise ValueError("width must be >= 0")
        
        # Store the value in the private attribute [3]
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the private instance attribute __height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the private instance attribute __height with validation.
        """
        if not isinstance(value, int):
            # Check if the value is an integer, otherwise raise TypeError
            raise TypeError("height must be an integer")
        if value < 0:
            # Check if the value is non-negative, otherwise raise ValueError
            raise ValueError("height must be >= 0")
            
        self.__height = value
