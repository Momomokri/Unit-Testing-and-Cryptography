from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode

class TestAffineEncode(TestCase):
    def test_affine_encode_normal(self):
        self.assertEqual(affine_encode("GOBBLEDEGOOK", 3, 3), "VTGGKPMPVTTH")

    def test_affine_encode_lowercase(self):
        self.assertEqual(affine_encode("gobbledegook", 3, 3), "vtggkpmpvtth")

    def test_affine_encode_empty_insert(self):
        self.assertEqual(affine_encode("", 3, 3), "")

    def test_affine_encode_whitespace(self):
        self.assertEqual(affine_encode("  ", 3, 3), "  ")

    def test_affine_encode_upper_and_lowercase(self):
        self.assertEqual(affine_encode("GoBbLeDeGoOk", 3, 3), "VtGgKpMpVtTh")

    def test_affine_encode_space_in_middle(self):
        self.assertEqual(affine_encode("GOBBLE DEGOOK", 3, 3), "VTGGKP MPVTTH")

    def test_affine_encode_punctuation(self):
        self.assertEqual(affine_encode("GOBBLEDEGOOK!", 3, 3), "VTGGKPMPVTTH!")

    def test_affine_encode_numbers(self):
        self.assertEqual(affine_encode("GOBBLEDEGOOK9", 3, 3), "VTGGKPMPVTTH9")