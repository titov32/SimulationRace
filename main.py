from car import Track, Car, Moto
from config import *
from time import sleep
THE_END = False
def run():
    global THE_END
    racers = []
    print("Помещаем на старт грузовики")
    t1=Track(0.3, 50, carrying=20)

    print("Помещаем на старт лекговушки")
    c1 = Car(0.15, 50, capacity=2)
    print("Помещаем на старт мотоциклы")
    m1 = Moto(0.1, 60)
    racers.extend([t1, c1, m1])
    for racer in racers:
        racer.start()

    while not THE_END:

        for racer in racers:
            racer.move()
            if LEN_CIRCLE <= racer.odometer:
                print(f'{racer} завершил движение')
                THE_END = True
        sleep(1)
        if THE_END:
            print('Гонка завершена')
            answer = input('Напишите "1"  если продолжаем гонку')
            if answer=='1':
                THE_END = False



if __name__ == '__main__':
    run()