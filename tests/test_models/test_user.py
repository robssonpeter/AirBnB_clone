#!/usr/bin/python3
""" Unit test for user model """
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_uid(self):
        self.assertEqual(type(User.id), type("hello"))

    def test_email(self):
        self.assertEqual("@" in User.email or User.email == '', True)

    def test_password(self):
        self.assertEqual(type(User.password), type("hello"))

    def test_first_name(self):
        self.assertEqual(type(User.first_name), type("hello"))

    def test_last_name(self):
        self.assertEqual(type(User.last_name), type("hello"))
