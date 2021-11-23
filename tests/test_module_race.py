from race import Road
import pytest


@pytest.mark.parametrize("distance, is_end_distance", [(119, False),
                                      (120, True)])
def test_end_distance_road(distance, is_end_distance):
    road = Road(120)
    assert road.end_distance(distance) == is_end_distance
