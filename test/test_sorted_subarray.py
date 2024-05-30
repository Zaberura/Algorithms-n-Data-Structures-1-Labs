import unittest

from src.sorted_subarray import find_max_sorted_subarray


class TestFindMaxSortedSubarray(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(find_max_sorted_subarray([]), 1)

    def test_single_element(self):
        self.assertEqual(find_max_sorted_subarray([5]), 1)

    def test_sorted_array(self):
        self.assertEqual(find_max_sorted_subarray([1, 2, 3, 4, 5]), 5)

    def test_unsorted_array(self):
        self.assertEqual(find_max_sorted_subarray([5, 3, 4, 8, 6, 7]), 3)

    def test_decreasing_array(self):
        self.assertEqual(find_max_sorted_subarray([5, 4, 3, 2, 1]), 1)

    def test_mixed_array(self):
        self.assertEqual(find_max_sorted_subarray([1, 2, 4, 3, 5, 6, 2, 7]), 3)


if __name__ == '__main__':
    unittest.main()
