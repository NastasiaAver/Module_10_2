import threading
import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        enemy = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            time.sleep(1)
            days += 1
            enemy -= self.power
            print(f'{self.name} сражается {days} дней..., '
                      f'осталось {enemy} воинов.')
        else:
            print(f'{self.name} одержал победу спустя {days} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
time.sleep(1)
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы окончились!')