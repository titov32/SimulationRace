from car import Track, Car, Moto
from time import sleep
from config import LEN_CIRCLE


class Simulation:
    def __init__(self, tracks, motos, cars):
        self.racers = []
        self.the_end = False
        self.road = Road(LEN_CIRCLE)
        self.winner = None
        for track in tracks:
            self.racers.append(Track(*tracks[track]))
        for car in cars:
            self.racers.append(Car(*cars[car]))
        for moto in motos:
            self.racers.append(Moto(*motos[moto]))

    def start(self):
        for racer in self.racers:
            print(racer.start())
        print('_' * 20)
        print('Начинаем движение')

    def run(self):
        while not self.the_end:
            for racer in self.racers:
                print(racer.move())
                sleep(0.1)
                if self.road.end_distance(racer.odometer):
                    print(f'{racer} приехал первый')
                    self.the_end = True
                    self.winner = racer
            print('__Прошел еще один отрезок времени__')
            sleep(2)
            if self.the_end:
                print('Гонка завершена')
                print(f'Победитель {self.winner}')
                answer = input('Напишите "1"  если продолжаем гонку')
                if answer == '1':
                    self.the_end = False


class Road:
    def __init__(self, len_circle: int):
        self.len_circle = len_circle

    def end_distance(self, odometer: int) -> bool:
        if self.len_circle <= odometer:
            return True
        else:
            return False
    # TODO можно добавить разные типы дорог и влияние на вероятность прокола
