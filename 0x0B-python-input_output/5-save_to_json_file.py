#!/usr/bin/python3
"""Module that save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON representation"""
    json_str = json.dumps(list(my_obj)) 
    with open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(json_str)
