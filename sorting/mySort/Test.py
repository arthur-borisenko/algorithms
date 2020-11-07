import unittest
import random
from sorting.mySort.Sort import *


class TestStringMethods(unittest.TestCase):
    EXAMPLE_2_N = 10000
    EXAMPLE_2_DIGITS = 10

    def test_my_third_sort_example_1(self):
        numbers = [1, 1, 22, 324, 444, 404, 243, 11]
        expected_result = [1, 1, 11, 22, 243, 324, 404, 444]
        Sort.my_third_sort(numbers)
        self.assertEqual(expected_result, numbers)

    def test_my_third_sort_example_2(self):
        n = self.EXAMPLE_2_N
        numbers = []
        for i in range(n):
            numbers.append(random.randint(1, n * self.EXAMPLE_2_DIGITS))

        expected_result = numbers.copy()
        expected_result.sort()
        Sort.my_third_sort(numbers)
        self.assertEqual(expected_result, numbers)

    def test_standart_sort_example_2(self):
        n = self.EXAMPLE_2_N
        numbers = []
        for i in range(n):
            numbers.append(random.randint(1, n * self.EXAMPLE_2_DIGITS))

        expected_result = numbers.copy()
        expected_result.sort()
        numbers.sort()
        self.assertEqual(expected_result, numbers)

    def test_swap(self):
        numbers = [10, 1, 22, 324, 2, 404, 243, 11]
        expected_result = [10, 1, 404, 324, 2, 22, 243, 11]
        Sort.swap(numbers, 2, 5)
        self.assertEqual(expected_result, numbers)

    def test_find_min_index_example_1(self):
        numbers = [10, 1, 22, 324, 2, 404, 243, 11]
        expected_result = 4
        result = Sort.find_min_index(numbers, 2)
        self.assertEqual(expected_result, result)

    def test_find_min_index_example_2(self):
        numbers = [10, 1, 22, 324, 2, 404, 243, 11]
        expected_result = 7
        result = Sort.find_min_index(numbers, 6)
        self.assertEqual(expected_result, result)

    def test_my_second_sort_example_1(self):
        numbers = [1, 1, 22, 324, 444, 404, 243, 11]
        expected_result = [1, 1, 11, 22, 243, 324, 404, 444]
        result = Sort.my_second_sort(numbers)
        self.assertEqual(expected_result, result)

    def test_my_second_sort_example_2(self):
        n = self.EXAMPLE_2_N
        numbers = []
        for i in range(n):
            numbers.append(random.randint(1, n * self.EXAMPLE_2_DIGITS))

        expected_result = numbers.copy()
        expected_result.sort()
        result = Sort.my_second_sort(numbers)
        self.assertEqual(expected_result, result)

    def test_my_first_sort_example_1(self):
        numbers = [1, 1, 22, 324, 444, 404, 243, 11]
        expected_result = [1, 1, 11, 22, 243, 324, 404, 444]
        result = Sort.my_first_sort(numbers)
        self.assertEqual(expected_result, result)

    def deprecated_test_my_first_sort_example_2(self):
        n = self.EXAMPLE_2_N
        numbers = []
        for i in range(n):
            numbers.append(random.randint(1, n * self.EXAMPLE_2_DIGITS))

        expected_result = numbers.copy()
        expected_result.sort()
        result = Sort.my_first_sort(numbers)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
