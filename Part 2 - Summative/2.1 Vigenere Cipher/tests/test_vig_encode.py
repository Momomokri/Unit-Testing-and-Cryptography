from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class TestVigEncode(TestCase):
    def test_vig_encode_normal(self):
        self.assertEqual(vig_encode("GOBBLEDEGOOK", "TEST"), "ZSTUDIVXZSFC")

    def test_vig_encode_lowercase(self):
        self.assertEqual(vig_encode("gobbledegook", "TEST"), "zstudivxzsfc")

    def test_vig_encode_empty_insert(self):
        self.assertEqual(vig_encode("", "TEST"), "")

    def test_vig_encode_whitespace(self):
        self.assertEqual(vig_encode("__", "TEST"), "SD")

    def test_vig_encode_upper_and_lowercase(self):
        self.assertEqual(vig_encode("GoBbLeDeGoOk", "TEST"), "ZsTuDiVxZsFc")

    def test_vig_encode_space_in_middle(self):
        self.assertEqual(vig_encode("GOBBLE_DEGOOK", "TEST"), "ZSTUDIRWXKFGC")

    def test_vig_encode_punctuation(self):
        self.assertEqual(vig_encode("GOBBLEDEGOOK!", "TEST"), "ZSTUDIVXZSFC")

    def test_vig_encode_numbers(self):
        self.assertEqual(vig_encode("GOBBLEDEGOOK9", "TEST"), "ZSTUDIVXZSFC")