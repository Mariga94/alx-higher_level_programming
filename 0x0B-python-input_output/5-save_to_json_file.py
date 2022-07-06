#!/usr/bin/python3
"""Module that save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON representation"""

    with open(filename, 'w', encoding='utf-8') as myFile:
        json.dump(my_obj, myFile)
