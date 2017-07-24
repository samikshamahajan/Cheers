class MyMath:
    def power(self, x , y):
        powr=1
        for i in range(y):
            powr *= x
        return powr

    def factorial(self,y):
        fact=1
        for i in range(y):
            fact+=fact*i
        return fact

    def sine(self,x):
        k=1
        sin=0
        for  i in range(50):
            v = 2*i+1
            sin += (self.power(x,v)*k)/self.factorial(v)
            k *= -1
        return sin

    def valueofpi(self):
        k = 1
        x = 0
        for i in range(100000):
            x += k/(2*i+1)
            k *= -1
        pi = x*4
        return(pi)

    def cosine(self,x):
        cos=0
        k=1
        for  i in range(50):
            cos += (self.power(x,2*i)*k)/self.factorial(2*i)
            k *= -1
        return cos
