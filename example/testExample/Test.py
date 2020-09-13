import unittest
from example.testExample.Task import *
from util.TestUtil import *

class TestStringMethods(unittest.TestCase):

    def test_method_example(self):
        task = Task()
        self.assertEqual(task.method_example(), 1)

    def test_static_menthod_example(self):
        self.assertEqual(Task.staticmethod_example(), 1)

    def test_console_example(self):
        console_test("test line",
                     lambda: Task().console_example(),
                     lambda out_text: self.assertEqual(out_text, "test line"))

if __name__ == '__main__':
    unittest.main()
