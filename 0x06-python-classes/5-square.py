#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Defines the square design"""

    def __init__(self, size=0):
        """initializes data

        Args:
            size (int): size of the square

        """
        self.__size = size
        if not type(size) is int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the new size of the square"""
        if not type(value) is int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """calculate area of a square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the
        character #
        """
        if self.__size == 0:
            print()
        else:
            if self.__size == 0:
                print("")

            for i in range(0, self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print('')
