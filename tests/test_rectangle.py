from src.Rectangle import Rectangle
import pytest

def test_rectangle_area_positive(api_server):
    side_a, side_b = api_server
    r = Rectangle(side_a, side_b)
    assert r.get_area() == 15
