"""easymoney.py -- a Python module for making business math easier to get right. 

Copyright (c) 2013 Jacek Artymiak

Permission is hereby granted, free of charge, to
any person obtaining a copy of this software and
associated documentation files (the "Software"), to
deal in the Software without restriction, including
without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to
whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice
shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL JACEK
ARTYMIAK BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of Jacek
Artymiak shall not be used in advertising or otherwise to
promote the sale, use or other dealings in this Software
without prior written authorization from Jacek Artymiak.
---
For more information write to jacek@artymiak.com.
"""

import calendar
import types
import time

# TODO: clean up the following three defs
class EasyMoneyError(Exception): pass
class TypeError(EasyMoneyError): pass
class ZeroDivisionError(EasyMoneyError): pass


class EasyMoney:

    """EasyMoney implements the canonical set of financial math functions 
    found in popular desktop spreadsheet software in a way that makes it easy
    to port existing spreadsheet formulas to Python.
    """


    def fDATE(self, y, m, d):

        """Implements: DATE(y, m, d)

        Returns internal serial number (aka. timestamp) that 
        represents a date written as year, month, day. 

        y -- year
        m -- month
        d -- day

        The range of y is architecture-dependent as is the timestamp 
        returned by fDATE().  Do *not* assume that timestamps from two
        different systems will be the same.  Always check timezones,
        epochs, etc.

        ###
        ### TODO: Verify
        ###
        """

        return calendar.timegm((y, m, d, 0, 0, 0))

    def fINT(self, n):

        """Returns integer value closest to the given number.

        Uses int(), which expects integers or integer strings or floats,
        but not float strings.  Can take longs, but not long strings.

        TODO:   more tests for boundary conditions, floats, longs, and 
            strings

        When you exceed the maximum values of int(), use long() or 
        fxlongINT()

        Maximum int() values are:

        -sys.maxint - 1 and sys.maxint

        The value of sys.maxint is architecture dependent, to find out 
        what it is, use:
        
        import sys
        print sys.maxint
        """

        return int(n)

    def fxlongINT(self, n):

        """Returns long integer value closest to the given number.

        FIXME:  Uses long(), which expects integers or integer strings or 
            floats, but not float strings.  Can take longs, but not 
            long strings.

        TODO:   more tests for boundary conditions, floats, longs, and 
            strings

        For smaller integers, use int() or fINT().

        Maximum value of a long integer is not defined.
        """

        return long(n)

    def fCODE(self, s):

        """Returns the numeric (ASCII) value of the first character in 
        the given string.
        """

        #if type(s) is not types.StringType:

        #   raise TypeError, 'the given s argument is not a string'

        return ord(s[0])


    # Simple interest calculations. TODO: FIXME, REMOVE, REFACTOR?


    def fvSimple(self, pv, ir):
        """pv -- present value of money
        ir -- interest rate (percent value, e.g. 10.5 for 10.5%)

        Returns simple future value of money
        """

        fv = pv + pv * ir / 100.0

        return fv

    def iSimple(self, pv, ir):
        i = pv * ir / 100.0
        return i

    def iSimpleFromFV(self, pv, fv):
        i = fv - pv
        return i

    def irSimple(self, pv, fv):
        ir = 100.0 * (fv - pv) / pv
        return ir

    def pvSimple(self, fv, i):
        pv = fv - i
        return pv

    def pvSimpleFromIR(self, fv, ir):
        pv = 100.0 * fv / (100.0 + 1.0 * ir)
        return pv

    def fvAdjusted(self, pv, ir, days, diy):
        fv = pv + pv * ir * days / (100.0 * diy)
        return fv

    def isLeapYear(self, year):

        leapYear = None

        year = int(year)

        if (year < 0):
            return leapYear

        if (year % 4 == 0):
            if (year % 100 != 0):
                leapYear = True
            else:
                if (year % 400 == 0):
                    leapYear = True 
                else:
                    leapYear = False
        else:
            leapYear = False

        return leapYear
    

def daysInA360DayYear(self, dStart, mStart, yStart, dEnd, mEnd, yEnd):

    days = None

    if (yStart < 0 or yEnd < 0):
        return days

    if (mStart < 1 or mEnd < 1):
        return days

    if (mStart > 12 or mEnd > 12):
        return days

    if (dStart < 1 or dEnd < 1):
        return days

    if (dStart > 31 or dEnd > 31):
        return days

    if (mStart == 1):

        if (dStart == 31):

            mStart = 2
            dStart = 1

    if (mStart == 2):

        if (leapYear(yStart)):

            if (dStart > 29):

                return days

        else:

            if (dStart > 28):

                return days

    if (mStart == 3):

        if (dStart == 31):

            mStart = 4
            dStart = 1

    if (mStart == 4):

        if (dStart > 30):

            return days

    if (mStart == 5):

        if (dStart == 31):

            mStart = 6
            dStart = 1

    if (mStart == 6):

        if (dStart > 30):

            return days

    if (mStart == 7):

        if (dStart == 31):

            mStart = 8
            dStart = 1

    if (mStart == 8):

        if (dStart == 31):

            mStart = 9
            dStart = 1

    if (mStart == 9):

        if (dStart > 30):

            return days

    if (mStart == 10):

        if (dStart == 31):

            mStart = 11
            dStart = 1

    if (mStart == 11):

        if (dStart > 30):

            return days

    if (mStart == 12):

        if (dStart == 31):

            yStart = yStart + 1
            mStart = 1
            dStart = 1

    if (mEnd == 1):

        if (dEnd == 31):

            mEnd = 2
            dEnd = 1

    if (mEnd == 2):

        if (leapYear(yEnd)):

            if (dEnd > 29):

                return days

            else:

                if (dEnd > 28):

                    return days

    if (mEnd == 3):

        if (dEnd == 31):

            mEnd = 4
            dEnd = 1

    if (mEnd == 4):

        if (dEnd > 30):

            return days

    if (mEnd == 5):

        if (dEnd == 31):

            mEnd = 6
            dEnd = 1

    if (mEnd == 6):

        if (dEnd > 30):

            return days

    if (mEnd == 7):

        if (dEnd == 31):

            mEnd = 8
            dEnd = 1

    if (mEnd == 8):

        if (dEnd == 31):

            mEnd = 9
            dEnd = 1

    if (mEnd == 9):

        if (dEnd > 30):

            return days

    if (mEnd == 10):

        if (dEnd == 31):

            mEnd = 11
            dEnd = 1

    if (mEnd == 11):

        if (dEnd > 30):

            return days

    if (mEnd == 12):

        if (dEnd == 31):

            yEnd = yEnd + 1
            mEnd = 1
            dEnd = 1

    yAdjust = (yEnd - yStart) * 360
    
    # check if the month is February
        # check if the day is 29
        # check if the year is a special year
            # yes? keep
            # no?  adjust accordingly
    # check if day is > 28

    days = days + yAdjust 

    return period


    # Array Functions


    def fEXPAND(self, eae):
        """EXPAND() (Array Function)
        eae -- enabled array expression
        """
        pass

    def fFREQUENCY(self, data, clases):
        """TODO
        """
        pass

    def fGROWTH(self, data_Y, data_X, new_data_X, function_type):
        """TODO
        """
        pass

    def fLINEST(self, data_Y, data_X, linear_type, stats):
        """TODO
        """
        pass

    def fLOGEST(self, data_Y, data_X, function_type, stats):
        """TODO
        """
        pass

    def fMDETERM(self, array):
        """TODO
        """
        pass

    def fMINVERSE(self, array):
        """TODO
        """
        pass

    def fMMULT(self, array1, array2):
        """TODO
        """
        pass

    def fNOEXPAND(self, eae):
        """NOEXPAND() (Array Function)
        eae -- enabled array expression
        """
        pass

    def fSUMPRODUCT(self, arrays):
        """TODO -- this functions typically takes up to 30 arrays, but we don't have to obey that rule.
        """
        pass

    def fSUMX2MY2(self, array_x, array_y):
        """TODO
        """
        pass

    def fSUMX2PY2(self, array_x, array_y):
        """TODO
        """
        pass

    def fSUMXMY2(self, array_x, array_y):
        """TODO
        """
        pass

    def fTRANSPOSE(self, array):
        """TODO
        """
        pass

    def fTREND(self, data_Y, data_X, new_data_X, linear_Type):
        """TODO
        """
        pass


    # Database Functions


    def DAVERAGE(self):
        pass

    def DCOUNT(self):
        pass

    def DCOUNTA(self):
        pass

    def DGET(self):
        pass

    def DMAX(self):
        """TODO
        """
        pass

    def DMIN(self):
        """TODO
        """
        pass

    def DPRODUCT(self):
        """TODO
        """
        pass

    def DSTDEV(self):
        """TODO
        """
        pass

    def DSTDEVP(self):
        """TODO
        """
        pass

    def DSUM(self):
        """TODO
        """
        pass

    def DVAR(self):
        """TODO
        """
        pass

    def DVARP(self):
        """TODO
        """
        pass


    # XXXFIXMEXXX Functions


    def AVERAGE(self, nLst):
        """Returns the arithmetic mean (average) value from the list of the arguments."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

        size = len(nLst)

        if size < 1:
            raise ZeroDivisionError, 'nLst has zero length'

        a = 0

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                raise TypeError, 'non-numeric list item'

        a = a + x

        return a * 1.0 / size

    def ABS(self, x):

        """Returns the absolute value of the argument.  The argument must be numeric."""

        if type(x) is types.IntType:

            return abs(x)

        elif type(x) is types.LongType:

            return abs(x)

        elif type(x) is types.FloatType:

            return abs(x)

        else:

            raise TypeError, 'non-numeric list item'

        # the definition of A in AVERAGEA is slightly extended. Calc or 
        # Excel allow us to use text strings, EasyMoney lets us use any 
        # non-numeric argument.  I don't know which is right.

    def AVERAGEA(self, nLst):

        """Returns the arithmetic mean (average) value from the list of the arguments.  Arguments may be non-numeric."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

            size = len(nLst)

            if size < 1:

                raise ZeroDivisionError, 'nLst has zero length'

                a = 0

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                continue 
        a = a + x

        return a * 1.0 / size

    def COUNT(self, nLst):

        """Returns the number of arguments in a list. Arguments must be numeric."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

        if len(nLst) < 1:

            raise ZeroDivisionError, 'nLst has zero length'

        a = 0

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                raise TypeError, 'non-numeric list item'
        a = a + 1

        return a

# the definition of A in COUNTA is slightly extended. Calc or Excel allow us to
# use text strings, EasyMoney lets us use any non-numeric argument.  I don't
# know which is right.

    def COUNTA(self, nLst):

        """Returns the number of arguments in a list. Arguments must be numeric."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

        return size(nLst)


    # Date Functions


    def fDATEVALUE(self):

        """TODO
        """

        return time.localtime()[2]

    def fDAY(self):

        """Returns current day.  Server localtime is used to determine the
        current day.  TODO: add timezone argument.
        """

        return time.localtime()[2]

    def fDAYS360(self):

        """Returns current day."""

        return time.localtime()[2]

    def fEDATE(self):

        """Returns current day."""

        return time.localtime()[2]

    def fEOMONTH(self):

        """Returns current day."""

        return time.localtime()[2]

    def fHOUR(self):

        """Returns current day."""

        return time.localtime()[2]

    def fMINUTE(self):

        """Returns current day."""

        return time.localtime()[2]

    def fMONTH(self):

        """Returns current day."""

        return time.localtime()[2]

    def fNETWORKDAYS(self):

        """Returns current day."""

        return time.localtime()[2]

    def fNOW(self):

        """Returns current day."""

        return time.localtime()[2]

    def fSECOND(self):

        """Returns current day."""

        return time.localtime()[2]

    def fTIME(self):

        """Returns current day."""

        return time.localtime()[2]

    def fTODAY(self):

        """Returns current day."""

        return time.localtime()[2]

    def fWEEKDAY(self):

        """Returns current day."""

        return time.localtime()[2]

    def fWORKDAY(self):

        """Returns current day."""

        return time.localtime()[2]

    def fYEAR(self):

        """Returns current day."""

        return time.localtime()[2]

    def fYEARFRAC(self):

        """Returns current day."""

        return time.localtime()[2]

    # Engineering Functions
    # Filter Functions
    # Financial Functions
    # Info Functions
    # Logical Functions
    # Lookup Functions
    # Math Functions
    # Operator Functions
    # Parser Functions
    # Statistical Functions
    # Text Functions

    def fGEOMEAN(self, nLst):

        """Returns the geometric mean value from the list of the arguments."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

        size = len(nLst)

        if size < 1:

            raise ZeroDivisionError, 'nLst has zero length'

        a = 1.0 

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                raise TypeError, 'non-numeric list item'

            a = a * x

        return pow(a, 1.0 / size)

    def HARMEAN(self, nLst):

        """Returns the harmonic mean value from the list of the arguments."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

            size = len(nLst)

        if size < 1:

            raise ZeroDivisionError, 'nLst has zero length'

        a = 0

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                raise TypeError, 'non-numeric list item'

            a = a + 1.0 / x

            a = a * (1.0 / size)

        return 1.0 / a

    def HOUR(self):

        """Returns current hour."""

        return time.localtime()[3]

    def LEN(self, s):

        """Returns the length of the given string."""

        return len(s)

    def LOWER(self, s):

        """Returns the lowercase version of the given string."""

        return s.lower()

    def MAX(self, nLst):

        """Returns the maximum value from the list of the numeric arguments."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

        if len(nLst) < 1:

            raise ZeroDivisionError, 'nLst has zero length'

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                raise TypeError, 'non-numeric list item'

        return max(nLst)

    def MAXA(self, nLst):

        """Returns the maximum value from the list of arguments with non-numeric arguments treated as 0."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

        if len(nLst) < 1:

            raise ZeroDivisionError, 'nLst has zero length'

        a = 0

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                nLst[a] = 0

            a = a + 1

        return max(nLst)

    def MEDIAN(self, nLst):

        """Returns the median value from the list of the numeric arguments."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

            size = len(nLst)

        if size < 1:

            raise ZeroDivisionError, 'nLst has zero length'

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                raise TypeError, 'non-numeric list item'

        if size == 1:

            return nLst[0]

        a = size % 2

        if a == 0:

            b = (nLst[size / 2] * 1.0 + nLst[(size / 2) - 1] * 1.0) / 2.0

        if a == 1:

            b = nLst[size / 2]

        return b

    def MIN(self, nLst):

        """Returns the minimum value from the list of the numeric arguments."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

        if len(nLst) < 1:

            raise ZeroDivisionError, 'nLst has zero length'

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                raise TypeError, 'non-numeric list item'

        return min(nLst)

    def MINA(self, nLst):

        """Returns the maximum value from the list of arguments with non-numeric arguments treated as 0."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

        if len(nLst) < 1:

            raise ZeroDivisionError, 'nLst has zero length'

            a = 0

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                nLst[a] = 0

            a = a + 1

        return min(nLst)

    def SUM(self, nLst):

        """Returns the sum of the arguments."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

            size = len(nLst)

        if size < 1:

            raise ZeroDivisionError, 'nLst has zero length'

        a = 0

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                continue

            a = a + x

        return a

    def SUMSQ(self, nLst):

        """Returns the sum of the squares of arguments."""

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

            size = len(nLst)

        if size < 1:

            raise ZeroDivisionError, 'nLst has zero length'

        a = 0

        for x in nLst[:]:

            if type(x) is types.IntType:

                pass

            elif type(x) is types.LongType:

                pass

            elif type(x) is types.FloatType:

                pass

            else:

                continue

        a = a + pow(x, 2)

        return a

    def MINUTE(self):

        """Returns current minute."""

        return time.localtime()[4]

    def MONTH(self):

        """Returns current month."""

        return time.localtime()[1]

    def NOW(self):

        """Returns a list of values that represent current time."""

        return time.localtime()

    def SECOND(self):

        """Returns current second."""

        return time.localtime()[5]

    def TIME(self):

        """Returns a list of three values: current hour, minute, and second."""

        h = time.localtime()[3]
        m = time.localtime()[4]
        s = time.localtime()[5]

        return [h, m, s]

    def TODAY(self):

        """Returns a list of three values: current year, month, and day."""

        y = time.localtime()[0]
        m = time.localtime()[1]
        d = time.localtime()[2]

        return [y, m, d]

    def TRIMMEAN(self, nLst, trim):

        """Returns the trimmed mean value from the list of the arguments.
        """

        if type(nLst) is not types.ListType:

            raise TypeError, 'nLst argument not a list'

        size = len(nLst)

        if size < 1:
            raise ZeroDivisionError, 'nLst has zero length'

            if trim >= 0.5:
                raise ArithmeticError, 'trim greater or equal 50%'

        if trim == 0.0:
            return self.AVERAGE(nLst)

        a = int(round(size * (trim / 2.0)))
        nLst = nLst[a:-a]
        return self.AVERAGE(nLst)


    def fUPPER(self, s):

        """Returns the uppercase version of the given string.
        """

        return s.upper()


#################################################################
##                    end of easymoney.py                      ##
#################################################################
