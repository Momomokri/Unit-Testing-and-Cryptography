from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_encode

class TestAffineNEncode(TestCase):
    def test_affine_n_encode_normal(self):
        self.assertEqual(affine_n_encode("COOL", 2, 3, 121), "XUHN")

    def test_affine_n_encode_lowercase(self):
        self.assertEqual(affine_n_encode("cool", 2, 3, 121), "XUHN")

    def test_affine_n_encode_empty_insert(self):
        self.assertEqual(affine_n_encode("", 2, 3, 121), "")

    def test_affine_n_encode_whitespace(self):
        self.assertEqual(affine_n_encode("  ", 2, 3, 121), "")

    def test_affine_n_encode_space_in_middle(self):
        self.assertEqual(affine_n_encode("CO OL", 2, 3, 121), "XUHN")

    def test_affine_n_encode_punctuation(self):
        self.assertEqual(affine_n_encode("COOL!", 2, 3, 121), "XUHN")

    def test_affine_n_encode_numbers(self):
        self.assertEqual(affine_n_encode("COOL9", 2, 3, 121), "XUHN")