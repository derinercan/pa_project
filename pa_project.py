from geometry import Point, Line

def test_distance():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance_to(p2) == 5.0

def test_line_length():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    line = Line(p1, p2)
    assert line.length() == 5.0

def test_slope():
    p1 = Point(0, 0)
    p2 = Point(2, 2)
    line = Line(p1, p2)
    assert line.slope() == 1.0