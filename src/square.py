import math
from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("...")
        super().__init__(side_a, side_a)
        self.name = "Square"
