#!/usr/bin/python3
"""Module for Base unit tests.

TestBase_init
TestBase_to_json_string
TestBase_save_to_file
TestBase_from_json_string
TestBase create
TestBase_load_from_file
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestBase(unittest.TestCase):
    """Tests the Base class."""

    def test_setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def test_tearDown(self):
        """Cleans up after each test_method."""
        pass

    def test_A_nb_objects_private(self):
        """Tests if nb_objects is private class attribute."""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_is_none(self):
        """Test if nb_objects is none"""

    if __name__ == '__main__':
        unittest.main()
