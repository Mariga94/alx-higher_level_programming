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

    def area(self):
        """calculate the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with `#` """
        if self.width == 0 or self.height == 0:
            print("")
            return
        for g in range(self.y):
            print("\n")
        for i in range(self.height):
            for h in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Return string representation"""
        string = "[" + self.__class__.__name__ + "] " + "(" + str(self.id)
        string += ") " + str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width) + "/" + str(self.height)
        return string

    def update(self, *args):
        """update the class Rectangle
        Args:
            *args (ints): new values
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
        """
        if args and len(args) > 0:
            for arg in range(len(args)):
                if arg == 0:
                    if args[arg] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[arg]
                elif arg == 1:
                    self.width = args[arg]
                elif arg == 2:
                    self.height = args[arg]
                elif arg == 3:
                    self.x = args[arg]
                elif arg == 4:
                    self.y = args[arg]
