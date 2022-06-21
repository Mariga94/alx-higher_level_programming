#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Describes how an square should be designed"""
    def __init__(self, size=0):
        """initializes data"""
        self.__size = size
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size**2
