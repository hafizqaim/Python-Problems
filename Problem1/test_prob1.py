import unittest
from .prob1 import diff_of_lists

class TestDiffOfLists(unittest.TestCase):
    """Test suite for the diff_of_lists function."""

    def test_standard_difference(self):
        """Test a basic case with a clear difference."""
        self.assertCountEqual(diff_of_lists([1, 2, 3, 4], [2, 4, 5]), [1, 3])

    def test_no_difference(self):
        """Test when all items from the first list are in the second."""
        self.assertCountEqual(diff_of_lists([1, 2], [1, 2, 3, 4]), [])

    def test_first_list_has_duplicates(self):
        """Test that duplicates in the first list are handled correctly."""
        self.assertCountEqual(diff_of_lists([1, 1, 2, 3, 3], [1, 4]), [2, 3, 3])
 
    def test_negative_numbers(self):
        """Test behavior with negative numbers."""
        self.assertCountEqual(diff_of_lists([-1, -2, -3], [-2, -4]), [-1, -3])
        self.assertCountEqual(diff_of_lists([-1, 0, 1], [0, 1]), [-1])

    def test_empty_lists(self):
        """Test behavior with empty lists."""
        self.assertCountEqual(diff_of_lists([1, 2, 3], []), [1, 2, 3])
        self.assertCountEqual(diff_of_lists([], [1, 2, 3]), [])
        self.assertCountEqual(diff_of_lists([], []), [])

    def test_non_list_iterable_input(self):
        """Test that tuples are handled correctly."""
        self.assertCountEqual(diff_of_lists((1, 2, 3), (2, 4)), [1, 3])
        self.assertCountEqual(diff_of_lists([1, 2, 3], (2, 4)), [1, 3])

    def test_raises_value_error_for_none_input(self):
        """Test that a ValueError is raised for None inputs."""
        with self.assertRaises(ValueError):
            diff_of_lists(None, [1, 2])
        with self.assertRaises(ValueError):
            diff_of_lists([1, 2], None)
        with self.assertRaises(ValueError):
            diff_of_lists(None, None)

    def test_raises_type_error_for_non_integers(self):
        """Test that a TypeError is raised for lists containing non-integers."""
        with self.assertRaises(TypeError):
            diff_of_lists([1, "a", 3], [1, 2])
        with self.assertRaises(TypeError):
            diff_of_lists([1, 2, 3], [1, "b"])
        with self.assertRaises(TypeError):
            diff_of_lists([1, 2.5, 3], [1, 2])

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
