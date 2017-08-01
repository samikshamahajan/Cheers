import math
from alpha_value2 import Alpha2
from alpha_value import Alpha
from MyMath import MyMath


class LengthCalculator:

    def calculate_length1(self, radius):
        """
        function to calculate Length of overlapping circle using library
        :param radius: value of radius in float
        :return:
        """
        alpha = Alpha2()
        lengthofline = 2 * radius * (1 - math.cos(alpha.valueofalpha() / 2))
        return lengthofline

    def calculate_length2(self, radius):
        """
        function to calculate Length of overlapping circle without using library
        :param radius: value of radius in float
        :return:
        """
        alpha = Alpha()
        mymath = MyMath()
        lengthofline = 2 * radius * (1 - mymath.cosine(alpha.valueofalpha() / 2, 5))
        return lengthofline
