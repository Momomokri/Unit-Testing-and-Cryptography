from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class TestCeasarEncode(TestCase):
    def test_caesar_encode_normal(self):
        self.assertEqual(caesar_encode("GOBBLEDEGOOK", 5), "LTGGQJIJLTTP")

    def test_caesar_encode_lowercase(self):
        self.assertEqual(caesar_encode("gobbledegook", 5), "ltggqjijlttp")

    def test_caesar_encode_empty_insert(self):
        self.assertEqual(caesar_encode("", 5), "")

    def test_caesar_encode_whitespace(self):
        self.assertEqual(caesar_encode("  ", 5), "  ")

    def test_caesar_encode_upper_and_lowercase(self):
        self.assertEqual(caesar_encode("GoBbLeDeGoOk", 5), "LtGgQjIjLtTp")

    def test_caesar_encode_space_in_middle(self):
        self.assertEqual(caesar_encode("GOBBLE DEGOOK", 5), "LTGGQJ IJLTTP")

    def test_caesar_encode_punctuation(self):
        self.assertEqual(caesar_encode("GOBBLEDEGOOK!", 5), "LTGGQJIJLTTP!")

    def test_caesar_encode_numbers(self):
        self.assertEqual(caesar_encode("GOBBLEDEGOOK9", 5), "LTGGQJIJLTTP9")