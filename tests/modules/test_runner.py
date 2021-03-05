"""Test case to find the runner from the given string
input will be the numbers with space
find out the second largest number in the input
"""
import unittest
from tdd.modules.runner import Runner

case1 = "6 5 5 2 6"
case1_exp = 5


class TestRunner(unittest.TestCase):
    def test_find_runner(self):
        """Test case 1"""
        obj = Runner()
        res = obj.find(case1)
        assert res == case1_exp
