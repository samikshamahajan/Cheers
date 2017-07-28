# class to approximate the value of alpha using bisection method

import math


class Alpha2:
    """
    Class containing method to calculate the value of alpha used in the program  using math library
    """

    def valueofalpha(self):
        """
        function to calculate value of alpha using bisection method
        :return: float value of alpha
        """
        lower = 0
        upper = math.pi
        for i in range(10):
            mid=(lower+upper)/2
            valueoffnatlower = self.fn(lower)
            valueoffnatmid = self.fn(mid)
            if valueoffnatlower * valueoffnatmid < 0:
                upper = mid
            else:
                lower = mid
        return (lower + upper)/2

    def fn(self,x):
        value = x-math.sin(x)-(math.pi/2)
        return value
