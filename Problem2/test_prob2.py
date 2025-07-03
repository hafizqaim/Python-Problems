# Problem2/test_prob2.py
import unittest
from .prob2 import recursive_sum

class TestRecursiveSumFunction(unittest.TestCase):
    def test_multi_digit_number(self):
        self.assertEqual(recursive_sum(493193), 2)

    def test_single_digit_number(self):
        self.assertEqual(recursive_sum(5), 5)

    def test_zero(self):
        self.assertEqual(recursive_sum(0), 0)
        
    def test_negative_number(self):
        self.assertEqual(recursive_sum(-50), 0)
    
    def test_two_digit_number(self):
        self.assertEqual(recursive_sum(18), 9)

    def test_large_number(self):
        self.assertEqual(recursive_sum(987654321), 9)

if __name__ == '__main__':
    unittest.main()
