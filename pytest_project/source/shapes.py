import math


class Shape(object):

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class which inherits from Shape

    Args:
        Shape (Custom class): User-defined Shape class
    """

    def __init__(self, radius) -> None:
        """Constructor for Circle class

        Args:
            radius (float): the radius of instantiated circle
        """
        self.radius = radius

    def area(self):
        """Calculates the area of the circle

        Returns:
            float: area of the circle in square units
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """Calculates the perimeter (circumference) of the circle

        Returns:
            float: perimeter (circumference) of the circle in units
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class which inherits from Shape

    Args:
        Shape (Custom class): User-defined Shape class
    """

    def __init__(self, length, width) -> None:
        """Constructor for Rectangle class

        Args:
            length (float): the length of instantiated Rectangle
            width (float): the width of instantiated Rectangle
        """
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle

        Returns:
            float: area of the rectangle in square units
        """
        return self.length * self.width

    def perimeter(self):
        """Calculates the perimeter of the rectangle

        Returns:
            float: perimeter of the rectangle in units
        """
        return 2 * (self.length + self.width)
