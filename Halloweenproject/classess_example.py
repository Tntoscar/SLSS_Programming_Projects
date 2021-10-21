# Classes Example

# Create some classes and objectimport math
import math


class Shape:
    """Represents a 2-dimensional polygon

    Attributes:
        num_sides: An integercount of the sides
        side_length: A floatof side length
    """

    def __init__(self):
        """Creates a new shape with new default values."""
        self.num_sides = 4
        self.side_length = 10.0

    def area(self) -> float:
        """Return the area of a square."""
        return self.side_length ** 2

    def perimeter(self) -> float:
         """Return the perimeter of a square"""
         return self.side_length * 4

class Circle(Shape):
    """Represents a circle which is a shape.

    Attributes:
        radius: A float indicating the radius
    """
    def __init__(self, radius: float = 5):
        """Creates a circle with default radius of 5"""
        # Call the superclass constructor
        super().__init__()

        self.radius = radius
        self.num_sides = 1
    def area(self) -> float:
        """returns the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Returns the perimeter of the circle. 2 * pi * r """
        return math.pi * self.radius * 2

some_shape = Shape()
print(some_shape.area())
print(some_shape.perimeter())

some_circle = Circle(10)
print(some_circle.area())
print(some_circle.perimeter())