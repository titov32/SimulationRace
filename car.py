from random import randint


class Vehicle:
    def __init__(self, puncture, speed):
        self.puncture = puncture
        self.speed = speed
        self.type_ = 'Транспорт'
        self.odometer = 0

    def print_specifications(self):
        return f'Скорость {self.speed}, вероятность прокола {self.puncture}'

    def start(self):
        print(f'{self.type_} начал движение {self.print_specifications()}')

    def move(self):
        """ расчет прохождения одного отрезка"""
        if not self.get_puncture():
            self.odometer += self.speed
            print('{}, проехал, {}'.format(self, self.odometer))
        else:
            print(f'Прокол колеса у {self}')

    def get_puncture(self):
        """ обработка прокола шины
        Если шанс прокола больше 9, прокол
        """
        puncture = randint(0, 99) * self.puncture
        if puncture > 9:
            return True
        else:
            return False


class Track(Vehicle):
    def __init__(self, puncture, speed, carrying):
        Vehicle.__init__(self, puncture, speed)
        self.carrying = carrying
        self.type_ = 'Грузовик'

    def __str__(self):
        return f'{self.type_} грузоподьемность {self.carrying}'


class Moto(Vehicle):
    def __init__(self, puncture, speed, sidecar=False):
        Vehicle.__init__(self, puncture, speed)
        self.sidecar = sidecar
        self.type_ = 'Мотоцикл'

    def __str__(self):
        if self.sidecar:
            return f'{self.type_} с коляской'
        else:
            return f'{self.type_} без коляски'


class Car(Vehicle):
    def __init__(self, puncture, speed, capacity=1):
        Vehicle.__init__(self, puncture, speed)
        self.capacity = capacity
        self.type_ = 'Легковой автомобиль'

    def __str__(self):
        return f'{self.type_} вместимость {self.capacity}'
