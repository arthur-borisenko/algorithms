import unittest

import test_fm.task
import os
import time

if not os.path.exists("tf"):
    open("tf", "x").close()


class Test(unittest.TestCase):
    def test_remove(self):
        test_fm.task.Task.rm("tf")
        self.assertFalse(os.path.exists("tf"), msg="File not removed.Bad func")

    def test_copy(self):
        if not os.path.exists("tf"):
            d = open("tf", "x")
            d.close()
        test_fm.task.Task.cp("tf", "tf.fnf.hl..fnf")
        self.assertTrue(os.path.exists("tf.fnf.hl..fnf"), msg="File not copied.Bad func")
        os.remove("tf.fnf.hl..fnf")

    def test_clean(self):
        if not os.path.exists("tf"):
            f = open("tf", "x")
            f.close()
        fill = open("tf", "a")
        fill.write("eeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        fill.close()
        time.sleep(0)
        test_fm.task.Task.cl("tf")
        time.sleep(0)
        f = open("tf", "r")
        cleaned = f.read()
        f.close()
        self.assertEqual("", cleaned)

    def test_read(self):
        if not os.path.exists("tf"):
            open("tf", "x").close()
        rd = test_fm.task.Task.rd("tf")
        self.assertEqual(second="", first=rd, msg="File not read.Bad func")
        os.remove("tf")

    def test_create(self):
        test_fm.task.Task.mk("tf")
        self.assertTrue(os.path.exists("tf"), msg="File not created.Bad func")
        if os.path.exists("tf"):
            os.remove("tf")


if __name__ == '__main__':
    unittest.main()
