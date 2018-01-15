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
        self.assertFalse(dutils.isFloat(" "))
        self.assertFalse(dutils.isFloat(""))

    def test_isInteger(self):
        self.assertTrue(dutils.isInteger("4"))
        self.assertFalse(dutils.isInteger("xyz"))
        self.assertFalse(dutils.isInteger("123.0"))
        self.assertTrue(dutils.isInteger(" 532"))
        self.assertTrue(dutils.isInteger('893 '))
        self.assertFalse(dutils.isInteger('847 92'))
        self.assertFalse(dutils.isInteger('839x'))
        self.assertFalse(dutils.isInteger('88 8c8'))
        self.assertFalse(dutils.isInteger(""))
        self.assertFalse(dutils.isInteger(" "))

    def test_isNumber(self):
        self.assertTrue(dutils.isNumber("38"))
        self.assertTrue(dutils.isNumber("38.1"))
        self.assertFalse(dutils.isNumber("99.x"))
        self.assertTrue(dutils.isNumber(" 0.3"))
        self.assertTrue(dutils.isNumber("53.7 "))
        self.assertFalse(dutils.isNumber("43. 8"))
        self.assertFalse(dutils.isNumber("45.7 99.3"))
        self.assertFalse(dutils.isNumber(""))
        self.assertFalse(dutils.isNumber(" "))
        self.assertFalse(dutils.isNumber(None))

if __name__ == '__main__':
    unittest.main()