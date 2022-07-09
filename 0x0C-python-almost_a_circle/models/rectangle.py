#!/usr/bin/python3
"""Defines a rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes data

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): co-ordinate x of the rectangle
            y (int): co-ordinate y of the rectangle

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than 1
            TypeError: if x or y is not an integer
            ValueError: if x or y is less than 0

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not type(value) is int:
            raise TypeError("Value must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

