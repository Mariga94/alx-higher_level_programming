#!/usr/bin/python3
"""unitest for max_intege([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integers."""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        self.assertEqual(max_integer([1,2,3,4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([4,3,2,1]), 4)

    def test_one_element_in_list(self):
        """Test an one element in a list"""
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        """Test floats in a list"""
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4.0)
    
    def test_string(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["Hello", "Python", "make"]), "make")

    if __name__ == '__main__':
        unittest.main()
