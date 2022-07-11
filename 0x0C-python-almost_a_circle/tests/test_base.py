#!/usr/bin/python3
"""Defines unittests for base.py

"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test class for Base"""
    
    def test_nb_objects(self):
        Base._Base__nb_objects = 0

    def test_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_none(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique(self):
        b1 = Base(1)
        self.assertEqual(1, b1.id)


