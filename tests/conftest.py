import pytest
import math


@pytest.fixture
def db():
    print("\nDataBase")
    yield
    print("\nEnd DataBase")


@pytest.fixture
def api_server(db):
    print("\nStart API")
    side_a = 3
    side_b = 5
    yield side_a, side_b
    print("\nEnd API")

@pytest.fixture
def api_for_triangle(db):
    print("\nStart API for triangle")
    side_a = 3
    side_b = 4
    side_c = 5
    yield side_a, side_b, side_c
    print("\nEnd API for triangle")


@pytest.fixture
def api_for_circle(db):
    print("\nStart API for circle")
    side_a = 3
    yield side_a
    print("\nEnd API for circle")