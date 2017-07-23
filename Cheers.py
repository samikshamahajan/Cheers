# Class to find the

from MyMath import MyMath
from alpha_value import Alpha


class Cheers:

    def __init__(self, radius):
        self.radius = radius

    mymath = MyMath()
    alpha = Alpha()
    def calculate_length(self):
        length = 2*self.radius*(1 - self.mymath.cosine(self.alpha.valueofalpha()/2))
        return length
print("Enter Radius: ")
r=0
try:
    r = float(input())
except:
    print("Invalid Input")
    exit(0)
if r < 0:
    print("Value of radius should not be negative")
else:
    cheers = Cheers(r)
    print(cheers.calculate_length())




