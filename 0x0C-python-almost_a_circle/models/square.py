#!/usr/bin/python3
"""Defines a Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the class Rectangle
        Args:
            *args (ints): new values
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            **kwargs (dictionary):
        """
        if args and len(args) > 0:
            for arg in range(len(args)):
                if arg == 0:
                    if args[arg] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[arg]
                elif arg == 1:
                    self.size = args[arg]
                elif arg == 2:
                    self.size = args[arg]
                elif arg == 3:
                    self.x = args[arg]
                elif arg == 4:
                    self.y = args[arg]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(self.size, self.size, self.x, self.y)
                        else:
                            self.id = value
                    elif key == "size":
                        self.size = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Return string representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
