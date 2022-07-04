#!/usr/bin/python3
"""Module that checks if an objec is an instance of a
    specified class
"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly
    an instance of the specified class otherwise False
    Args:
        obj - param1
        a_class - param2
    return:
        True if obj is instance of a_class, otherwise
        False
    """
    return type(obj) is a_class
