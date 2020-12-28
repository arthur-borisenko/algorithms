import unittest
from simpleNumber.task import SimpleNumber

class TestSimpleNumber(unittest.TestCase):
    def test_simple_number(self):
        self.assertFalse(SimpleNumber.isSimple(12*66232))
    def test_simple_number_2(self):
        self.assertTrue(SimpleNumber.isSimple(194989))

if __name__ == '__main__':
    unittest.main()
