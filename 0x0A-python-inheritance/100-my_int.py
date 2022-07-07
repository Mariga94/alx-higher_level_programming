#!/usr/bin/python3
"""Defines class MyInt"""


class MyInt(int):
    """Invert"""
    def __eq__(self, other):
        """Override =="""
        return self.equal != other
    
    def __ne__(self, other):
        """Override != """
        return self.equal == other
