# test_stats_calculator.py

import unittest
from .prob5 import calculate_seconds, seconds_to_time, stats

class TestTeamStats(unittest.TestCase):
    """
    Complete test suite for the team statistics calculator,
    covering all three functions.
    """

    ## ----------------------------------------
    ## Tests for calculate_seconds
    ## ----------------------------------------
    def test_calculate_seconds_valid_input(self):
        """Test that a standard, valid string is converted to seconds correctly."""
        self.assertEqual(calculate_seconds("01|01|01,00|01|00"), [3661, 60])

    def test_calculate_seconds_empty_input(self):
        """Test that an empty string returns an empty list."""
        self.assertEqual(calculate_seconds(""), [])

    def test_calculate_seconds_skips_malformed_data(self):
        """Test that invalid entries are skipped and valid ones are processed."""
        self.assertEqual(calculate_seconds("01|00|00,a|b|c,00|00|30"), [3600, 30])

    def test_calculate_seconds_skips_negative_values(self):
        """Test that entries with negative time components are skipped."""
        self.assertEqual(calculate_seconds("01|00|00,-1|10|20,00|00|15"), [3600, 15])

    def test_calculate_seconds_handles_messy_spacing(self):
        """Test robust parsing with extra spaces and trailing commas."""
        self.assertEqual(calculate_seconds(" 0|1|0 , 0|0|5, "), [60, 5])


    ## ----------------------------------------
    ## Tests for seconds_to_time
    ## ----------------------------------------
    def test_seconds_to_time_valid_input(self):
        """Test conversion of seconds to a formatted time string."""
        self.assertEqual(seconds_to_time(3661), "01|01|01")
        self.assertEqual(seconds_to_time(0), "00|00|00")

    def test_seconds_to_time_handles_type_error(self):
        """Test that the helper function does not crash on invalid types."""
        self.assertEqual(seconds_to_time("not a number"), "00|00|00")
        self.assertEqual(seconds_to_time(None), "00|00|00")

    ## ----------------------------------------
    ## Tests for the main stats function
    ## ----------------------------------------
    def test_stats_even_number_of_runners(self):
        """Test main function with an even number of runners."""
        data = "02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|32|34, 2|17|17"
        expected = "Range: 00|31|17 Average: 02|27|10 Median: 02|24|57"
        self.assertEqual(stats(data), expected)

    def test_stats_handles_non_string_input(self):
        """Test that non-string input is handled without crashing."""
        self.assertEqual(stats(None), "Error: Input must be a string.")
        self.assertEqual(stats([1, 2, 3]), "Error: Input must be a string.")

    def test_stats_handles_only_invalid_data(self):
        """Test a string with only malformed data returns the correct error."""
        self.assertEqual(stats("a|b|c, d|e|f"), "Error: No valid race times found in input.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
