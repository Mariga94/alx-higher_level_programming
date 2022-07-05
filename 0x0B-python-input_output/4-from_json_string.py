#!/usr/bin/python3
"""Module  that takes a string and returns an Object"""


def from_json_string(my_str):
    """JSON string representation"""
    return json.loads(my_str)
