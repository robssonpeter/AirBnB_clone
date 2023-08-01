#!/usr/bin/python3
""" Unit test for user model """
import unittest
from models.place import Place


class TestUser(unittest.TestCase):

    def test_uid(self):
        self.assertEqual(type(Place.id), type("hello"))
