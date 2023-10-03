#!/usr/bin/python3
"""Module for Rectangle unit tests.

    TestRectangle_init
    TestRectangle_area
    TestRectangle_display
    TestRectangle_update
    TestRectangle_dictionary
"""
from typing import Any
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import AbstractContextManager, redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    """Tests the Base class."""

    def setUp(self):
        """Imports module, instantiates class"""
        self.set = Rectangle(1, 2, 5, 6, 34)

    def test_width_getter(self):
        self.assertEqual(self.set.width, 1)

    def test_height_getter(self):
        self.assertEqual(self.set.height, 2)

    def test_x_getter(self):
        self.assertEqual(self.set.x, 5)

    def test_y_getter(self):
        self.assertEqual(self.set.y, 6)

    def test_id_getter(self):
        self.assertEqual(self.set.id, 34)

    def test_id_setter(self):
        self.set.width = 7
        self.assertEqual(self.set.width, 7)

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

    if __name__ == '__main__':
        unittest.main()
