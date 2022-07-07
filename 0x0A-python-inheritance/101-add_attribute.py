#!/usr/bin/python3
"""Defines a function that adds attr"""

def add_attribute(obj, attr, val):
    """function that adds a new attribute to
    an object if it's possible
    
    Args:
        obj (any): object where to add the attr
        attr (str): name of the attribute
        val (any): value of attribute

    Raises:
        TypeError: If the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can;t add new attribute")
    setattr(obj, attr, val)
