import unittest
from alpha_value import Alpha
from alpha_value2 import Alpha2


class TestAlphaValues(unittest.TestCase):
    """
    class to test the value of alpha
    """
    alpha = Alpha()
    alpha2 = Alpha2()

    def test_valueofalpha(self):
        """
        function to test value of alpha which does not use library for calculation
        :return:
        """
        self.assertEqual(Alpha.valueofalpha(self.alpha), 2.3086337371350236)

    def test_valueofalpha2(self):
        """
        function to test value of alpha which uses library for calculation
        :return:
        """
        self.assertEqual(Alpha2.valueofalpha(self.alpha2), 2.3086410857678903)
