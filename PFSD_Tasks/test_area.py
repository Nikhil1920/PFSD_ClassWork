import math


def area_of_circle(r):
    return math.pi*r*r


def area_of_triangle(h, b):
    return (h*b)/2


def area_of_square(s):
    return s*s


def test_circle():
    assert area_of_circle(4) == 50


def test_triangle():
    assert area_of_triangle(6, 4) == 12


def test_square():
    assert area_of_square(4) == 16
