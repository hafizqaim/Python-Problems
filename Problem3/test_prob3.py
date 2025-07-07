import unittest
from .prob3 import create_phone_number

class TestCreatePhoneNumber(unittest.TestCase):
    """Test cases for the create_phone_number function."""

    def test_valid_number(self):
        """Test with a standard, valid list of numbers."""
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")

    def test_not_a_list(self):
        """Test that a non-list input raises a TypeError."""
        with self.assertRaises(TypeError):
            create_phone_number("1234567890")

    def test_incorrect_length(self):
        """Test that a list with the wrong number of elements raises a ValueError."""
        with self.assertRaises(ValueError):
            create_phone_number([1, 2, 3])

    def test_contains_non_integer(self):
        """Test that a list with a non-integer element raises a ValueError."""
        with self.assertRaises(ValueError):
            create_phone_number([1, 2, 3, 4, 'a', 6, 7, 8, 9, 0])

    def test_contains_number_greater_than_9(self):
        """Test that a list with a number greater than 9 raises a ValueError."""
        with self.assertRaises(ValueError):
            create_phone_number([1, 2, 3, 4, 10, 6, 7, 8, 9, 0])
            
    def test_contains_negative_number(self):
        """Test that a list with a negative number raises a ValueError."""
        with self.assertRaises(ValueError):
            create_phone_number([1, 2, 3, 4, -5, 6, 7, 8, 9, 0])


if __name__ == '__main__':
    unittest.main()
