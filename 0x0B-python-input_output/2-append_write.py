#!/usr/bin/python3
"""Module that append to a file"""


def append_write(filename="", text=""):
    """function that appends string to the end of a text file
        Args:
            filename (string) - file
            text (string) - text to be appended
    """
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
