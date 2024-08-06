from figure import Figure
import math


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_a + self.side_b

    def get_area(self):
        return self.side_a * self.side_b

rectangle_perimeter = Rectangle(2, 5)
rectangle_area = Rectangle(2, 5)

