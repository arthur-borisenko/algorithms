import unittest
from simple_number.task import SimpleNumber


class TestSimpleNumber(unittest.TestCase):
    def test_simple_number(self):
        self.assertFalse(SimpleNumber.is_simple(12 * 66232))

    def test_simple_number_2(self):
        self.assertTrue(SimpleNumber.is_simple(194989))


if __name__ == '__main__':
    unittest.main()
