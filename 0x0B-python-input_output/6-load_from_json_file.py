#!/usr/bin/python3
"""Creates Object"""
import json


def load_from_json_file(filename):
    """Read obj"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
