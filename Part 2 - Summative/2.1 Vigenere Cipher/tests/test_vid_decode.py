from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode

class TestCeasarEncode(TestCase):
    def test_vig_decode_normal(self):
        self.assertEqual(vig_decode("ZSTUDIVXZSFC", "TEST"), "GOBBLEDEGOOK")

    def test_vig_decode_lowercase(self):
        self.assertEqual(vig_decode("zstudivxzsfc", "TEST"), "gobbledegook")

    def test_vig_decode_empty_insert(self):
        self.assertEqual(vig_decode("", "TEST"), "")

    def test_vig_decode_whitespace(self):
        self.assertEqual(vig_decode("SD", "TEST"), "")

    def test_vig_decode_upper_and_lowercase(self):
        self.assertEqual(vig_decode("ZsTuDiVxZsFc", "TEST"), "GoBbLeDeGoOk")

    def test_vig_decode_space_in_middle(self):
        self.assertEqual(vig_decode("ZSTUDIRWXKFGC", "TEST"), "GOBBLE_DEGOOK")

    def test_vig_decode_punctuation(self):
        self.assertEqual(vig_decode("ZSTUDIVXZSFC!", "TEST"), "GOBBLEDEGOOK")

    def test_vig_decode_numbers(self):
        self.assertEqual(vig_decode("ZSTUDIVXZSFC9", "TEST"), "GOBBLEDEGOOK")