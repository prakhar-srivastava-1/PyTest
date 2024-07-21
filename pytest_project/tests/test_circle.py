import math
import pytest
import source.shapes as shapes


class TestCircle:
    """Class-based tests for Circle class
    """

    def setup_method(self, method):
        """This function is responsible for setting up the pre-requisites
        ,i.e., objects for completing the unit tests.

        Args:
            method (function object): function object passed as argument
        """
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        """This function is responsible for removing the objects which 
        were setup during setup_method.

        Args:
            method (function object): function object passed as argument
        """
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        """function to test if circle area is being calculated correctly
        """
        assert self.circle.area() == math.pi * self.circle.radius * self.circle.radius

    def test_perimeter(self):
        """function to test if circle area is being calculated correctly
        """
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
