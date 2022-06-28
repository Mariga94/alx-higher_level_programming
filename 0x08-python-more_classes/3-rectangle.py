#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """initialize data"""
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

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rec
