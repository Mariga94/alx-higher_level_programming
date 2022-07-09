#!/usr/bin/python3
"""Defines a Base class"""


class Base:
    """Represents a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize data

        Args:
            id (int): id of object
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
