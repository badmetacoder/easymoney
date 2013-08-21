"""Unit test for easymoney.py
"""

import easymoney
import unittest

emoney = easymoney.EasyMoney()

class KnownValues(unittest.TestCase):
    knownValues = ( ([0], 0.0),
                    ([1, 2L, 3.0], 2.0),
                    ([1, 0], 0.5),
                    ([1, 2], 1.5),
                    ([0, 0, 0, 1], 0.25) )

    def testAVERAGE(self):
        """getMean should give known result with known input"""
        for l, m in self.knownValues:
            result = emoney.AVERAGE(l)
            self.assertEqual(m, result)

class GetMeanBadInput(unittest.TestCase):
    def testEmptyString(self):
        self.assertRaises(emoney.TypeError, emoney.AVERAGE, '')

    def testEmptyList(self):
        self.assertRaises(emoney.ZeroDivisionError, emoney.AVERAGE, [])

    def testNonNumericInputString(self):
        self.assertRaises(emoney.TypeError, emoney.AVERAGE, "0")

    def testNonNumericInputStringElement(self):
        self.assertRaises(emoney.TypeError, emoney.AVERAGE, ["0"])

class TestDateFunctions(unittest.TestCase):
    def testDATEforNegativeYear(self):
        self.assertRaises(ValueError, emoney.fDATE, -1, 1, 1)
    def testDATEforNegativeFloatYear(self):
        self.assertRaises(TypeError, emoney.fDATE, -1.0, 1, 1)

class TestMathFunctions(unittest.TestCase):
    def testINTforZeroArgument(self):
        self.failUnlessEqual(emoney.fINT(0.0), 0)
    def testINTforFloatNegativeArgument(self):
        self.failUnlessEqual(emoney.fINT(-1.7), -1)
    def testINTforFloatPositiveArgument(self):
        self.failUnlessEqual(emoney.fINT(1.7), 1)
    def testINTforLongIntNegativeArgument(self):
        self.failUnlessEqual(emoney.fINT(-1000L), -1000)
    def testINTforLongIntPositiveArgument(self):
        self.failUnlessEqual(emoney.fINT(1000L), 1000)
    def testINTforLongIntStringNegativeArgument(self):
        self.assertRaises(ValueError, emoney.fINT, "1000L")
    def testINTforLongIntStringPositiveArgument(self):
        self.assertRaises(ValueError, emoney.fINT, "1000L")
    def testINTforIntStringNegativeArgument(self):
        self.failUnlessEqual(emoney.fINT("-1000"), -1000)
    def testINTforIntStringPositiveArgument(self):
        self.failUnlessEqual(emoney.fINT("1000"), 1000)
    def testINTforFloatStringNegativeArgument(self):
        self.assertRaises(ValueError, emoney.fINT, "-1.7")
    def testINTforFloatStringPositiveArgument(self):
        self.assertRaises(ValueError, emoney.fINT, "1.7")
    def testINTforStringArgument(self):
        self.assertRaises(ValueError, emoney.fINT, "python")

class TestTextFunctions(unittest.TestCase):
    def testCODEforNonStringValue(self):
        self.assertRaises(TypeError, emoney.fCODE, 1)
    def testCODEforTextString(self):
        self.failUnlessEqual(emoney.fCODE("easymoney"), 101)
    def testCODEforZeroNumericString(self):
        self.failUnlessEqual(emoney.fCODE("001 ref"), 48)
    def testCODEforOneNumericString(self):
        self.failUnlessEqual(emoney.fCODE("100 ref"), 49)

if __name__ == "__main__":
    unittest.main()
