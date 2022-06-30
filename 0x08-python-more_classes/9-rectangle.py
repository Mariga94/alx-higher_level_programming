#!/usr/bin/python3
""" class that defines a Rectangle
"""


class Rectangle:
    """Represents a rectangle"""

    """public class attribute that
        increments during each new instantiation
        decrements during each instance deletion
    """
    number_of_instances = 0

    """Public class attribute initiliazed to #
        Used as symbol for string representation
    """
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes data
            Args:
                width (int): width of the rectangle.
                height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
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
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the new value of width in a rectangle"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """"Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of an object"""
        if self.__width == 0 or self.__height == 0:
            return "\n"
        else:
            rectangle = []
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle.append(str(self.print_symbol))
                if i < self.__height - 1:
                    rectangle.append("\n")
            return "".join(rectangle)

    def __repr__(self):
        """Returns the string representantion of an object for machine use"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Destroys an instance of an object"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that compares two rectangles
            Args:
            rect_1 (int): first rectangle to compare
            rect_2 (int): second rectangle to compare
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    """Returns a rectangle instance with equal width and height"""
    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
