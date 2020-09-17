import unittest
from sorting.mySort.Sort import *


class TestStringMethods(unittest.TestCase):

    def test_static_menthod_example(self):
        numbers = [1, 1, 22, 324, 444, 404, 243, 11]
        expected_result = [1, 1, 11, 22, 243, 324, 404, 444]
        result = Sort.sort3(numbers)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
