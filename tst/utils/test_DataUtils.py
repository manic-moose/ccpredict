import unittest
from utils import DataUtils as dutils


class MyTestCase(unittest.TestCase):

    def test_isFloat(self):
        self.assertTrue(dutils.isFloat("38"))
        self.assertTrue(dutils.isFloat("38.1"))
        self.assertFalse(dutils.isFloat("99.x"))
        self.assertTrue(dutils.isFloat(" 0.3"))
        self.assertTrue(dutils.isFloat("53.7 "))
        self.assertFalse(dutils.isFloat("43. 8"))
        self.assertFalse(dutils.isFloat("45.7 99.3"))

    def test_isInteger(self):
        self.assertTrue(dutils.isInteger("4"))
        self.assertFalse(dutils.isInteger("xyz"))
        self.assertFalse(dutils.isInteger("123.0"))
        self.assertTrue(dutils.isInteger(" 532"))
        self.assertTrue(dutils.isInteger('893 '))
        self.assertFalse(dutils.isInteger('847 92'))
        self.assertFalse(dutils.isInteger('839x'))
        self.assertFalse(dutils.isInteger('88 8c8'))

    def test_isNumber(self):
        self.assertTrue(dutils.isFloat("38"))
        self.assertTrue(dutils.isFloat("38.1"))
        self.assertFalse(dutils.isFloat("99.x"))
        self.assertTrue(dutils.isFloat(" 0.3"))
        self.assertTrue(dutils.isFloat("53.7 "))
        self.assertFalse(dutils.isFloat("43. 8"))
        self.assertFalse(dutils.isFloat("45.7 99.3"))

if __name__ == '__main__':
    unittest.main()