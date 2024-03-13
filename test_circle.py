"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import math

from circle import Circle
import unittest
class CircleTest(unittest.TestCase):

    def test_add_area_typical_value(self):
        self.circle1 = Circle(2)
        self.circle2 = Circle(3)
        new_value = math.hypot(self.circle1.get_radius(), self.circle2.get_radius())
        self.assertEqual(Circle(new_value).get_radius(), self.circle1.add_area(self.circle2).get_radius())
        self.assertEqual(Circle(new_value).get_area(), self.circle1.add_area(self.circle2).get_area())

    def test_add_area_zero_radius(self):
        self.circle1 = Circle(0)
        self.circle2 = Circle(2)
        new_value = math.hypot(self.circle1.get_radius(), self.circle2.get_radius())
        self.assertEqual(Circle(new_value).get_radius(), self.circle1.add_area(self.circle2).get_radius())
        self.assertEqual(Circle(new_value).get_area(), self.circle1.add_area(self.circle2).get_area())

    def test_exception_when_negative_radius(self):
        with self.assertRaises(Exception):
            circle = Circle(-48)

