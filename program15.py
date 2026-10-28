from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Vector(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def area(self):
        return 0

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius})"


v1 = Vector(3, 4)
v2 = Vector(2, 5)

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Addition:", v1 + v2)
print("Magnitude of Vector 1:", v1.magnitude())
print("Vectors equal:", v1 == v2)
print("Vector 1 smaller than Vector 2:", v1 < v2)

c1 = Circle(5)
c2 = Circle(3)

print("\nCircle 1:", c1)
print("Circle 1 Area:", round(c1.area(), 2))
print("Circle 2 Area:", round(c2.area(), 2))
print("Circle 1 has greater area:", c1.area() > c2.area())
