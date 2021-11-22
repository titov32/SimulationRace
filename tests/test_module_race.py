from race import Road


def test_end_distance_road():
    road = Road(120)
    assert road.end_distanсe(120)


def test_not_end_distance_road():
    road = Road(120)
    assert not road.end_distanсe(119)