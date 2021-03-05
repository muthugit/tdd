"""Test cases to test the given year is leap year"""
import unittest

from tdd.modules.leap_year import LeapYear


class TestLeapYear(unittest.TestCase):
    """Unit test cases for finding leap year"""
    def test_find_leap(self):
        """Find is 2000 is a leap year"""
        obj = LeapYear()
        res = obj.is_leap_year(2000)
        assert res is True

    def test_find_non_leap(self):
        """Find is 2001 is a leap year"""
        obj = LeapYear()
        res = obj.is_leap_year(2001)
        assert res is False
