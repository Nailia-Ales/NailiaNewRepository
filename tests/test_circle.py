from src.circle import Circle
import pytest

def test_circle_area_positive(api_for_circle):
    side_a = api_for_circle
    r = Circle(side_a)
    assert r.get_area() == 28.274333882308138