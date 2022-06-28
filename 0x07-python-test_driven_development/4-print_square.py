#!/usr/bin/python3


def print_square(size):
    """
    Args:
        size (int): size of a square
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        square = size ** size
        for i in range(size):
            for i in range(size):
                print("#", end="")
            print()
