from src.figure import Figure
import math

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if not all([side_a, side_b, side_c]):
            raise ValueError
        if side_a + side_b <= side_c and side_a + side_c <= side_b and side_b + side_c <= side_a:
            raise ValueError
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        return (self.side_a + self.side_b + self.side_c) / 2
