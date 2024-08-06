from figure import Figure
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
        p = self.get_perimeter() / 2
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

