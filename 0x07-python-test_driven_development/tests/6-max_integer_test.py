#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test when the list contains positive integers."""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        """Test when the list is unordered."""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test when an empty list is passed."""
        result = max_integer([])
        self.assertIsNone(result)

    # Add more test cases here for other scenarios, edge cases, or boundary values

if __name__ == '__main__':
    unittest.main()
