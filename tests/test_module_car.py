from car import Vehicle, Car, Track


def test_move():
    transport = Vehicle(0, 100)
    transport.move()
    assert transport.odometer == 100


def test_punchure_func():
    transport = Vehicle(9, 100)
    assert transport.get_puncture()


def test_punchure_move():
    transport = Vehicle(9, 100)
    transport.move()
    assert transport.odometer == 0


def test_not_punchure():
    transport = Vehicle(0, 100)
    assert not transport.get_puncture()


def test_car():
    car = Car(0, 70, 2)
    assert ((car.__str__() == 'Легковой автомобиль вместимость 2') and
            (car.capacity == 2))


def test_track():
    track = Track(0, 50, 200)
    assert ((track.type_ == 'Грузовик') and
            (track.carrying == 200))
