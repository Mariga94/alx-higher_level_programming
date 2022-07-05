#!/usr/bin/python3
"""Module that writes to a file"""


def write_file(filename="", text=""):
    """write text to filename"""
    open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(text)
