import unittest
from sort import algorithms

arrays = [[1, 9, 8, 2, 3, 4, 5, 7, 6], [1], [2], [2, 1], [1, 2], [4, 6, 2], [1, 3, 9], [10, 8], [11, 31]]
expected = [[2, 4, 6, 8, 9, 7, 5, 3, 1], [1], [2], [2, 1], [2, 1], [2, 4, 6], [9, 3, 1], [8, 10], [31, 11]]


class AlgorithmsTests(unittest.TestCase):
    def test_split_and_sorted_approach(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.split_and_sorted_approach(array)
            self.assertTrue(result, expected[i])

    def test_no_split_and_sorted_approach(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.no_split_and_sorted_approach(array)
            self.assertTrue(result, expected[i])

    def test_full_sort_and_iterate_approach(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.full_sort_and_iterate_approach(array)
            self.assertTrue(result, expected[i])

    def test_bubble_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.bubble_sort(array)
            self.assertTrue(result, expected[i])

    def test_selection_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.selection_sort(array)
            self.assertTrue(result, expected[i])

    def test_insertion_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.insertion_sort(array)
            self.assertTrue(result, expected[i])

    def test_quick_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.quicksort(array)
            self.assertTrue(result, expected[i])


if __name__ == "__main__":
    unittest.main()
