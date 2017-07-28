# This program calculate the length of line segment of overlapping circle by using libraries
from xml.dom import minidom
import math
from alpha_value import Alpha


class LengthCalculator:
    """
    In this class length of overlapping circle is calculated by using math libraries
    """
    alpha = Alpha()

    def __init__(self,radius):
        """

        :param radius:
        """
        self.radius = radius

    def calculate_length(self):
        """
        function to calculate Length of overlapping circle
        """
        lengthofline = 2*self.radius*(1-math.cos(self.alpha.valueofalpha()/2))
        return lengthofline


option = 0
xml = minidom.Document()
cheers = xml.createElement("cheers")
xml.appendChild(cheers)

inputs = xml.createElement("inputs")
inputs.setAttribute("type","radius")

outputs = xml.createElement("outputs")
outputs.setAttribute("type","length")
while option != 2:
    try:
        print("-----------------\nEnter an option\n-----------------\n1.Calculate Length\n2.Exit\n------------------\n")
        option = int(input())
        if option == 1:
            r = float(input("Enter radius: "))
            radius = xml.createElement("radius")
            radius.setAttribute("type","float")
            radius.appendChild(xml.createTextNode(str(r)))
            inputs.appendChild(radius)
            length = LengthCalculator(r)
            l=length.calculate_length()
            print("Length of the Line Segment is: ",l)
            len = xml.createElement("length")
            len.setAttribute("type","float")
            len.appendChild(xml.createTextNode(str(l)))
            outputs.appendChild(len)
        elif option != (1 and 2):
            print("Error!:  Please enter valid choice")
    except ValueError:
        print("Invalid input")

cheers.appendChild(inputs)
cheers.appendChild(outputs)
print(xml.toprettyxml())
print("Program Terminated")
