#!/usr/bin/python3


class Rectangle:

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
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
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            for i in range(self.__width):
                for i in range(self.__height):
                    print('#', end="")
                print()

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height) 

    def __del__(self):
        print('Bye rectangle...')
