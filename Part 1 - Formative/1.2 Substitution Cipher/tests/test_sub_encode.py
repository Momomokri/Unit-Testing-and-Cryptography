from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode

class TestSubEncode(TestCase):
    def test_sub_encode_normal(self):
        self.assertEqual(sub_encode("GOBBLEDEGOOK", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "BHJJTXUXBHHD")

    def test_sub_encode_lowercase(self):
        self.assertEqual(sub_encode("gobbledegook", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "bhjjtxuxbhhd")

    def test_sub_encode_empty_insert(self):
        self.assertEqual(sub_encode("", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "")

    def test_sub_encode_whitespace(self):
        self.assertEqual(sub_encode("  ", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "  ")

    def test_sub_encode_upper_and_lowercase(self):
        self.assertEqual(sub_encode("GoBbLeDeGoOk", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "BhJjTxUxBhHd")

    def test_sub_encode_space_in_middle(self):
        self.assertEqual(sub_encode("GOBBLE DEGOOK", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "BHJJTX UXBHHD")