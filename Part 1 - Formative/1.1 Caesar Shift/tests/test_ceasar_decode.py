from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode

class TestCeasarDecode(TestCase):
    def test_caesar_decode_normal(self):
        self.assertEqual(caesar_decode("LTGGQJIJLTTP", 5), "GOBBLEDEGOOK")

    def test_caesar_decode_lowercase(self):
        self.assertEqual(caesar_decode("ltggqjijlttp", 5), "gobbledegook")

    def test_caesar_decode_empty_insert(self):
        self.assertEqual(caesar_decode("", 5), "")

    def test_caesar_decode_whitespace(self):
        self.assertEqual(caesar_decode("  ", 5), "  ")

    def test_caesar_decode_upper_and_lowercase(self):
        self.assertEqual(caesar_decode("LtGgQjIjLtTp", 5), "GoBbLeDeGoOk")

    def test_caesar_decode_space_in_middle(self):
        self.assertEqual(caesar_decode("LTGGQJ IJLTTP", 5), "GOBBLE DEGOOK")