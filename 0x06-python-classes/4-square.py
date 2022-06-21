#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """class that defines characteristics of a square"""
    def __init__(self, size=0):
        """initialize data"""
        self.__size = size
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        def area(self):
            """calculate area of a square"""
            return self.__size ** 2

        def size(self, value):
            """sets the value of square"""
            self.__size = value
