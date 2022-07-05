#!/usr/bin/python3
"""Module that reads a text-file"""


def read_file(filename=""):
    #f = open(filename, 'r', encoding="utf-8")
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    f.closed
