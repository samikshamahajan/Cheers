# This program calculate the length of line segment of overlapping circle by using libraries
from xml.dom import minidom
import math
from alpha_value2 import Alpha2
from length_calculator import LengthCalculator


class Cheers2:
    """
    In this class length of overlapping circle is calculated by using math libraries
    """
    alpha = Alpha2()

    def __init__(self, radius):
        """

        :param radius:
        """
        self.radius = radius

option = 0
while option != 2:
    try:
        print("-----------------\nEnter an option\n-----------------\n1.Calculate Length\n2.Exit\n------------------\n")
        option = int(input())
        if option == 1:
            r = float(input("Enter radius: "))
            length = LengthCalculator()
            l = LengthCalculator.calculate_length1(length, r)
            print("Length of the Line Segment is: ", l)
        elif option != (1 and 2):
            print("Error!:  Please enter valid choice")
    except ValueError:
        print("Invalid input")

print("Program Terminated")
