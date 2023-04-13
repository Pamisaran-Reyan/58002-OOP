class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.14159

    def Perimeter(self):
        print("Perimeter: " ,2 * self.pi * self.radius)

    def Area(self):
        print("Area: " ,self.pi * self.radius * self.radius)

radius = float(input("Radius: "))
per = Circle(radius)
per.Perimeter()
are = Circle(radius)
are.Area()

