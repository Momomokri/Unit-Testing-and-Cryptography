from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode

class TestSubDecode(TestCase):
    def test_sub_decode_normal(self):
        self.assertEqual(sub_decode("BHJJTXUXBHHD", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "GOBBLEDEGOOK")

    def test_sub_decode_lowercase(self):
        self.assertEqual(sub_decode("bhjjtxuxbhhd", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "gobbledegook")

    def test_sub_decode_empty_insert(self):
        self.assertEqual(sub_decode("", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "")

    def test_sub_decode_whitespace(self):
        self.assertEqual(sub_decode("  ", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "  ")

    def test_sub_decode_upper_and_lowercase(self):
        self.assertEqual(sub_decode("BhJjTxUxBhHd", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "GoBbLeDeGoOk")

    def test_sub_decode_space_in_middle(self):
        self.assertEqual(sub_decode("BHJJTX UXBHHD", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "GOBBLE DEGOOK")

    def test_sub_decode_numbers(self):
        self.assertEqual(sub_decode("BHJJTXUXBHHD9", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "GOBBLEDEGOOK9")

    def test_sub_decode_punctuation(self):
        self.assertEqual(sub_decode("BHJJTXUXBHHD!", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "GOBBLEDEGOOK!")