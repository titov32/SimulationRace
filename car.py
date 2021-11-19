from random import randint


class Vehicle:
    def __init__(self, puncture, speed):
        self.puncture = puncture
        self.speed = speed
        self.type_ = 'Транспорт'

    def print_specifications(self):
        return f'Скорость {self.speed}, вероятность прокола {self.puncture}'
  
    def start(self):
        print(f'{self.type_} начал движение {self.print_specifications()}')


class Track(Vehicle):
    def __init__(self, puncture, speed, carrying):
        Vehicle.__init__(self, puncture, speed)
        self.carrying = carrying
        self.type_ = 'Грузовик'

    def start(self):
        print(f'Грузовик начал движение {self.print_specifications()}, вместимость {self.carrying}')


class Moto(Vehicle):
    def __init__(self, puncture, speed, sidecar=False):
        Vehicle.__init__(self, puncture, speed)
        self.sidecar = sidecar
        self.type_ = 'Мотоцикл'


class Car(Vehicle):
    def __init__(self, puncture, speed, capacity=False):
        Vehicle.__init__(self, puncture, speed)
        self.capacity = capacity
        self.type_ = 'Легковой автомобиль'
