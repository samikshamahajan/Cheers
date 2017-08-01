# This program calculate the length of line segment of overlapping circle without using libraries
from xml.dom import minidom
from length_calculator import LengthCalculator


class Cheers:
    """
    In this class length of overlapping circle is calculated without using any libraries
    """
    def __init__(self, radius):
        """
        constructor
        :param radius:
        """
        self.radius = radius
option = 0
xml = minidom.Document()
root = xml.createElement("cheers")
xml.appendChild(root)

inputs = xml.createElement("inputs")
inputs.setAttribute("type", "radius")

outputs = xml.createElement("outputs")
outputs.setAttribute("type", "length")
while option != 2:
    try:
        print("-----------------\nEnter an option\n-----------------\n1.Calculate Length\n2.Exit\n------------------\n")
        option = int(input())
        if option == 1:
            r = float(input("Enter radius: "))
            if r < 0:
                print("Radius must not be negative")
            else:
                radius = xml.createElement("radius")
                radius.setAttribute("type", "float")
                radius.appendChild(xml.createTextNode(str(r)))
                inputs.appendChild(radius)
                length = LengthCalculator()
                l = LengthCalculator.calculate_length2(length, r)
                print("Length of the Line Segment is: ", l)
                len = xml.createElement("length")
                len.setAttribute("type", "float")
                len.appendChild(xml.createTextNode(str(l)))
                outputs.appendChild(len)
        elif option != (1 and 2):
            print("Error!:  Please enter valid choice")
    except ValueError:
        print("Invalid input")
print("Program Terminated")

root.appendChild(inputs)
root.appendChild(outputs)
print(xml.toprettyxml())
xml.writexml(open('result.xml', 'w'), indent=" ", addindent=" ", newl="\n")
xml.unlink()
