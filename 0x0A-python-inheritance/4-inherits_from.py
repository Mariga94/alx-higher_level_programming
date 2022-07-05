#!/usr/bin/python3
"""Module that checks if the object is an instance
    of a class that inherited(directly or indirectly)
    from the specified class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj.
    Returns:
        True, if the object is an instance of a class
        else, False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
