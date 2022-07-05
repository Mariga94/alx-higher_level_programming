#!/usr/bin/python3
"""Module that returns JSON representation to string"""
import json


def to_json_string(my_obj):
    """JSON representation to string"""
    return json.dumps(my_obj)
