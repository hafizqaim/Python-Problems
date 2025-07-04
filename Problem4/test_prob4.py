# Problem4/test_prob4.py

import unittest
from .prob4 import missing_character # Import the function from your prob4.py file

class TestMissingCharacter(unittest.TestCase):
    """Test cases for the missing_character function."""

    def test_simple_gap(self):
        """Test a simple list with one missing character."""
        self.assertEqual(missing_character(['a', 'b', 'd']), 'c')

    def test_uppercase(self):
        """Test with uppercase letters."""
        self.assertEqual(missing_character(['X', 'Z']), 'Y')

    def test_no_missing_character(self):
        """Test a complete sequence where nothing is missing."""
        self.assertIsNone(missing_character(['a', 'b', 'c', 'd']))

    def test_multiple_gaps(self):
        """Test a list with multiple gaps."""
        self.assertEqual(missing_character(['a', 'c', 'e']), 'b')

    def test_numbers_in_list(self):
        """Test with a list that includes numbers."""
        self.assertIsNone(missing_character(['a', 'b', '1', 'c']))

    def test_special_characters(self):
        """Test with a list that includes special characters."""
        self.assertIsNone(missing_character(['a', 'b', '@', 'c']))

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(missing_character([]))

    def test_single_item_list(self):
        """Test with a list containing only one character."""
        self.assertIsNone(missing_character(['a']))

if __name__ == '__main__':
    unittest.main()
