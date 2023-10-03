#!/usr/bin/python3
"""Module for Rectangle unit tests.

    TestRectangle_init
    TestRectangle_to_json_string
    TestRectangle_save_to_file
    TestRectangle_from_json_string
    TestRectangle create
    TestRectangle_load_from_file
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
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


    def tearDown(self):
        """Cleans up after each test_method."""
        pass

    if __name__ == '__main__':
        unittest.main()
