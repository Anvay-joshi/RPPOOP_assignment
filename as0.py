from polygon import *


class rectangle(polygon):
    def get_no_of_sides(self):
        return 4;

    def __init__(self, length = 0, breadth = 0):
        self.length = length
        self.breadth = breadth

    def set_dimensions(self, l, b):
        self.length = l
        self.breadth = b

    def get_dimensions(self):
        return (self.length, self.breadth)

    def report_dimensions(self):
        print("Polygon: rectangle\nlength:",str(self.length),"\nbreadth:",str(self.breadth))

    def get_area(self):
        return (self.length * self.breadth)
    
    def get_perimeter(self):
        return (2*(self.length + self.breadth))

class square(rectangle):
    def __init__(self,side = 0):
        self.length = side
        self.breadth = side

    def report_dimensions(self):
        print("Polygon: square\nside length:",self.length) 

    def set_dimensions(self, s):
        self.length = s
        self.breadth = s

    def get_dimensions(self):
        return self.length

class triangle(polygon):
    def __init__(self, a = 0, b = 0, c = 0):
        self.a = a
        self.b = b
        self.c = c
        self.sides = 3

    def set_dimensions(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_dimensions(self):
        return (self.a, self.b, self.c)

    def report_dimensions(self):
        print("Polygon: triangle\nside 1:",self.a,"\nside 2:",self.b,"\nside 3:",self.c)
        
    def get_perimeter(self):
        return (self.a + self.b + self.c)

    def get_area(self):
        s = (self.a + self.b + self.c)/2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area


rec1 = rectangle()
print("no of sides is:",rec1.get_no_of_sides())
rec1.set_dimensions(3,4)
rec1_dim = rec1.get_dimensions()
print(rec1_dim)
rec1.report_dimensions()
print("area is:",rec1.get_area())
print("perimeter is:",rec1.get_perimeter())

print("\n\n\n")

sq1 = square()
print("no of sides is:",sq1.get_no_of_sides())
sq1.set_dimensions(5)
sq1_dim = sq1.get_dimensions()
print(sq1_dim)
sq1.report_dimensions()
print("area is:",sq1.get_area())
print("perimeter is:",sq1.get_perimeter())

print("\n\n\n")

tri1 = triangle()
print("no of sides is:",tri1.get_no_of_sides())
tri1.set_dimensions(3,4,5)
tri1_dim = tri1.get_dimensions()
print(tri1_dim)
tri1.report_dimensions()
print("area is:",tri1.get_area())
print("perimeter is:",tri1.get_perimeter())
