from src.Triangle import Triangle
import pytest

def test_triangle_area_positive(api_for_triangle):
    side_a, side_b, side_c = api_for_triangle
    r = Triangle(side_a, side_b, side_c)
    assert r.get_area() == 6