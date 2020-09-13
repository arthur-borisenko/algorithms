import unittest
from graphs.minPathFloydWarshall.Task import Task
from util.TestUtil import *

class TestStringMethods(unittest.TestCase):

    def test_console_example(self):
        console_test("test line",
                     lambda: Task().echo(),
                     lambda out_text: self.assertEqual(out_text, "test line"))

if __name__ == '__main__':
    unittest.main()
