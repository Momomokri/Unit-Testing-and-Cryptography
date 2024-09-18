from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode

class TestAffineDecode(TestCase):
    def test_affine_decode_normal(self):
        self.assertEqual(affine_decode("VTGGKPMPVTTH", 3, 3), "GOBBLEDEGOOK")

    def test_affine_decode_lowercase(self):
        self.assertEqual(affine_decode("vtggkpmpvtth", 3, 3), "gobbledegook")

    def test_affine_decode_empty_insert(self):
        self.assertEqual(affine_decode("", 3, 3), "")

    def test_affine_decode_whitespace(self):
        self.assertEqual(affine_decode("  ", 3, 3), "  ")

    def test_affine_decode_upper_and_lowercase(self):
        self.assertEqual(affine_decode("VtGgKpMpVtTh", 3, 3), "GoBbLeDeGoOk")

    def test_affine_decode_space_in_middle(self):
        self.assertEqual(affine_decode("VTGGKP MPVTTH", 3, 3), "GOBBLE DEGOOK")

    def test_affine_decode_punctuation(self):
        self.assertEqual(affine_decode("VTGGKPMPVTTH!", 3, 3), "GOBBLEDEGOOK!")

    def test_affine_decode_numbers(self):
        self.assertEqual(affine_decode("VTGGKPMPVTTH9", 3, 3), "GOBBLEDEGOOK9")