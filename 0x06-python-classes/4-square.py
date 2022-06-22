#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """defines design a square"""

    def __init__(self, size=0):
        """initialize data
        Args:
        size (int): Size of a new square.
        """
    self.__size = size
    if not type(size) is int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    def area(self):
        """calculate area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """get the value of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of square"""
        if not type(value) is int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
