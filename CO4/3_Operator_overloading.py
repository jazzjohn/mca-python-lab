# Create a class rectangle with private attributes length and width. overlead '<' operator to compare the area of two reactangles

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


r1 = Rectangle(4, 5)
r2 = Rectangle(6, 3)
if r1 < r2:
    print("Area of r1 is smaller")
else:
    print("Area of r2 is smaller")
