import unittest
from MyMath import MyMath


class TestMyMath(unittest.TestCase):
    """
    class to test various function in MyMath class
    """
    mymath = MyMath()

    def test_sine(self):
        """
        to test the value of sin
        :return: ok if test passes
        """
        self.assertEqual(MyMath.sine(self.mymath, 3, 5), 0.14112)

    def test_cosine(self):
        """
        to test value of cosine
        :return: ok if test passes
        """
        self.assertEqual(MyMath.cosine(self.mymath, 3, 5), -0.98999)

    def test_power(self):
        """
        to test value of power
        :return: ok if test passes
        """
        self.assertEqual(MyMath.power(self.mymath, 4, 3), 64)

    def test_factorial(self):
        """
        to test factorial value
        :return: ok if test passes
        """
        self.assertEqual(MyMath.factorial(self.mymath, 6), 720)

    def test_valueofpi(self):
        """
        to test value of pi
        :return: ok if test passes
        """
        self.assertEqual(MyMath.valueofpi(self.mymath), 3.1415826535897198)
