#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Describes how a square should be designed"""

    def __init__(self, size=0):
        """initializes data"""
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
