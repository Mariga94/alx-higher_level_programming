#!/usr/bin/python3
"""class that defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initialiazes the attributes"""
        self.__width = width
        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        if not type(height) is int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of rectangular"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
