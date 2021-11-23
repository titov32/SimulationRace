from car import Vehicle, Car, Track
import pytest


@pytest.mark.parametrize("punchure, speed, odometer", [(0, 100, 100),
                                                       (0, 50, 50),
                                                       (9, 100, 0)])
def test_move(punchure, speed, odometer):
    transport = Vehicle(punchure, speed)
    transport.move()
    assert transport.odometer == odometer


@pytest.mark.parametrize("punchure, speed, result", [(0, 100, False),
                                                     (9, 100, True)])
def test_punchure_func(punchure, speed, result):
    transport = Vehicle(punchure, speed)
    assert transport.get_puncture() == result


def test_car():
    car = Car(0, 70, 2)
    assert ((car.__str__() == 'Легковой автомобиль вместимость 2') and
            (car.capacity == 2))


def test_track():
    track = Track(0, 50, 200)
    assert ((track.type_ == 'Грузовик') and
            (track.carrying == 200))
