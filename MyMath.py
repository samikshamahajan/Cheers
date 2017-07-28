# User Defined class to calculate some of the mathematical function values used in the program


class MyMath:
    """
    class containing various functions to calculate values of various mathematical functions
    """
    def power(self, x , y):
        """
        return the value of x^y
        :param x:
        :param y:
        :return: float value
        """
        powr = 1
        for i in range(y):
            powr *= x
        return powr

    def factorial(self,y):
        """
        function factorial(y) returns the factorial of the number y
        :param y:
        :return: integer value of factorial
        """
        fact = 1
        for i in range(y):
            fact += fact*i
        return fact

    def sine(self,x): # Function to calculate the value of sine(x) where x is in radian
        """
        function sine(x) is use to calculate and return the value of sine by using Taylor's theorem
        :param x:
        :return: float value of sine
        """
        k = 1
        sin = 0
        for i in range(50):
            v = 2*i+1
            sin += (self.power(x,v)*k)/self.factorial(v)
            k *= -1
        return sin

    def valueofpi(self):
        """
        function to calculate the value of pi using Leibniz series
        :return: float value of pi
        """
        k = 1
        x = 0
        for i in range(100000):
            x += k/(2*i+1)
            k *= -1
        pi = x*4
        return pi

    def cosine(self,x):
        """
        function cosine(x) is use to calculate and return the value of cosine of x by using Taylor's theorem
        :param x:
        :return: float value of cosine
        """
        cos=0
        k=1
        for  i in range(50):
            cos += (self.power(x,2*i)*k)/self.factorial(2*i)
            k *= -1
        return cos
