# class to approximate the value of alpha using bisection method

from MyMath import MyMath


class Alpha:
    """
    Class containing method to calculate the value of alpha used in the program without using any libraries
    """
    mymath = MyMath()

    def valueofalpha(self):
        """
        function to calculate value of alpha using bisection method
        :return: float value of alpha
        """
        lower = 0
        upper = self.mymath.valueofpi()
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
        value = x-self.mymath.sine(x,5)-(self.mymath.valueofpi()/2) # expression
        return value
