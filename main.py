from car import Track, Car, Moto
from config import LEN_CIRCLE, TRACKS, MOTOS, CARS
from time import sleep


def run():
    the_end=False
    racers = []
    print("Помещаем на старт грузовики")
    for track in TRACKS:
        racers.append(Track(*TRACKS[track]))
    print("Помещаем на старт лекговушки")
    for car in CARS:
        racers.append(Car(*CARS[car]))
    print("Помещаем на старт мотоциклы")
    for moto in MOTOS:
        racers.append(Moto(*MOTOS[moto]))

    for racer in racers:
        racer.start()
    print('_'*20)
    print('Начинаем движение')
    while not the_end:
        for racer in racers:
            racer.move()
            if LEN_CIRCLE <= racer.odometer:
                print(f'{racer} приехал первый')
                the_end = True
        sleep(5)
        if the_end:
            print('Гонка завершена')
            answer = input('Напишите "1"  если продолжаем гонку')
            if answer == '1':
                the_end = False


if __name__ == '__main__':
    run()
