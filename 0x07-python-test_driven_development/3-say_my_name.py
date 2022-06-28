#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name (str): the first name
        last_name (str): the last name

    Returns:
        String

    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print('My name is {} {}'.format(first_name, last_name))
