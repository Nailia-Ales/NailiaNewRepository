from src.square import Square
import pytest

def test_square_area_positive(api_server):
    side_a, _ = api_server
    r = Square(side_a)
    assert r.get_area() == 9