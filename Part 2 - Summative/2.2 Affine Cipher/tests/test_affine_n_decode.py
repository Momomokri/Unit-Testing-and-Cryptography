from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_decode

class TestAffineNDecode(TestCase):
    def test_affine_n_decode_normal(self):
        self.assertEqual(affine_n_decode("XUHN", 2, 3, 121), "COOL")

    def test_affine_n_decode_lowercase(self):
        self.assertEqual(affine_n_decode("xuhn", 2, 3, 121), "COOL")

    def test_affine_n_decode_empty_insert(self):
        self.assertEqual(affine_n_decode("", 2, 3, 121), "")

    def test_affine_n_decode_whitespace(self):
        self.assertEqual(affine_n_decode("  ", 2, 3, 121), "")

    def test_affine_n_decode_space_in_middle(self):
        self.assertEqual(affine_n_decode("XU HN", 2, 3, 121), "COOL")

    def test_affine_n_decode_punctuation(self):
        self.assertEqual(affine_n_decode("XUHN!", 2, 3, 121), "COOL")

    def test_affine_n_decode_numbers(self):
        self.assertEqual(affine_n_decode("XUHN9", 2, 3, 121), "COOL")