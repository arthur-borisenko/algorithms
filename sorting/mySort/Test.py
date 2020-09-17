import unittest
import random
from sorting.mySort.Sort import *


class TestStringMethods(unittest.TestCase):
    def test_my_second_sort_example_1(self):
        numbers = [1, 1, 22, 324, 444, 404, 243, 11]
        expected_result = [1, 1, 11, 22, 243, 324, 404, 444]
        result = Sort.my_second_sort(numbers)
        self.assertEqual(expected_result, result)

    def test_my_second_sort_example_2(self):
        n = 1000
        numbers = []
        for i in range(n):
            numbers.append(random.randint(1, n * 10000))

        expected_result = numbers.copy()
        expected_result.sort()
        result = Sort.my_second_sort(numbers)
        self.assertEqual(expected_result, result)

    def test_my_first_sort_example_1(self):
        numbers = [1, 1, 22, 324, 444, 404, 243, 11]
        expected_result = [1, 1, 11, 22, 243, 324, 404, 444]
        result = Sort.my_first_sort(numbers)
        self.assertEqual(expected_result, result)

    def test_my_first_sort_example_2(self):
        n = 1000
        numbers = []
        for i in range(n):
            numbers.append(random.randint(1, n * 10000))

        expected_result = numbers.copy()
        expected_result.sort()
        result = Sort.my_first_sort(numbers)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
