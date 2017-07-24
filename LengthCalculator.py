# This program calculate the length of line segment of overlapping circle by using libraries

import math
from alpha_value import Alpha


class LengthCalculator:

    alpha = Alpha()

    def __init__(self,radius):
        self.radius = radius


    def calculate_length(self):
        length = 2*self.radius*(1-math.cos(self.alpha.valueofalpha()/2))
        return length

r = float(input("Enter radius: "))
length = LengthCalculator(r)
print("Length of the Line Segment is: ",length.calculate_length())
