# class to approximate the value of alpha using bisection method

from MyMath import MyMath


class Alpha:
    mymath = MyMath()

# This function return the value of alpha

    def valueofalpha(self):
        lower = 0
        upper = self.mymath.valueofpi()
        i = 1
        for i in range(10):
            mid=(lower+upper)/2
            valueoffnatlower = self.fn(lower)
            valueoffnatmid = self.fn(mid)
            if valueoffnatlower * valueoffnatmid < 0:
                upper = mid
            else:
                lower = mid
        return (lower + upper)/2

# This function evaluate and return the result of  expression at a particular value

    def fn(self,x):
        value = x-self.mymath.sine(x)-(self.mymath.valueofpi()/2) # expression
        return value
