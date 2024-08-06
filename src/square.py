import math
from figures_homework.src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a, side_b):
        super().__init__(side_a, side_b)

#    def get_perimeter(self):
#        return self.side_a + self.side_a + self.side_a + self.side_a

#    def get_area(self):
#        return self.side_a ** 2

square_perimeter = Square(5,5)
square_area = Square(5,5)

