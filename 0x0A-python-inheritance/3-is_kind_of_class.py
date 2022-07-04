#!/usr/bin/python3
"""Module that checks if an object is an instance of
    or the object is an instance of a class that
    inherited from.
"""


def is_kind_of_class(obj, class):
    """function that returns true else false"""
    return isinstance(obj, class)
