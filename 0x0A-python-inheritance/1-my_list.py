#!/usr/bin/python3
"""Class MyList"""

class MyList(list):
    def print_sorted(self):
        """print list in ascending sort"""
        print(sorted(self))
