import unittest
from length_calculator import LengthCalculator


class TestLengthCalculator(unittest.TestCase):
    """
    class to test the calculated value of length
    """
    length = LengthCalculator()

    def test_calculate_length1(self):
        """
        test the value of length which is calculated using libraries
        :return: ok if test id passed
        """
        self.assertEqual(LengthCalculator.calculate_length1(self.length, 5), 5.954599952234471)

    def test_calculate_length2(self):
        """
        test the value of length which is calculated without using libraries
        :return: ok if test passed
        """
        self.assertEqual(LengthCalculator.calculate_length2(self.length, 5), 5.9546)