#!/usr/bin/python3
""" The testing class for file storage"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_all(self):
        self.assertEqual(type(FileStorage().all()), type({}))
