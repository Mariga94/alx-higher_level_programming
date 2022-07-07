#!/usr/bin/python3
"""Defines a class square that inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square using Rectangle"""

    def __init__(self, size):
        """Initialize a new Square

        Args:
            size (int): The width and height of the new Square

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
