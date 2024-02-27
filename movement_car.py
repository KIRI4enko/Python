'''
Движение машины, автобуса, посадка пассажиров
Movement of a car, bus, boarding passengers
'''
import math


class Car:
    def __init__(self, x: float = 0, y: float = 0, angle: int = 0):
        self._x = x
        self._y = y
        self._angle = angle % 360
        self._cnt_pass = 0
        self._cnt_money = 0

    def move(self, s: float = 0, angle: int = 0):
        self._angle = (self._angle + angle) % 360
        self._y += round(math.sin(math.pi * (self._angle / 180)), ndigits=2) * s
        self._x += round(math.cos(math.pi * (self._angle / 180)), ndigits=2) * s

    def __str__(self):
        return f'Машина находится в ({self._x},{self._y}), смотрит на {self._angle} градусов \n Внутри {self._cnt_pass} пассажира(-ов) \n Заработано: {self._cnt_money}\n'

    def exit(self, cnt_pass_exit: int):
        if cnt_pass_exit > self._cnt_pass:
            raise WrongPassengerCount()
        else:
            self._cnt_pass -= cnt_pass_exit

    def enter(self, cnt_pass_enter: int, cnt_enter=80):
        self._cnt_pass += cnt_pass_enter
        self._cnt_money += cnt_enter * cnt_pass_enter


class Bus(Car):
    def __init__(self, x: float = 0, y: float = 0, angle: int = 0):
        super().__init__(x, y, angle)

    def __str__(self):
        return super().__str__().replace('Машина', 'Автобус')

    def enter(self, cnt_pass_enter: int, cnt_enter=35):
        super().enter(cnt_pass_enter, cnt_enter)

    def exit(self, cnt_pass_exit: int):
        super().exit(cnt_pass_exit)


class WrongPassengerCount(Exception):
    pass


try:
    car = Car()
    bus = Bus(angle=450)
    car.move(1, angle=60)
    print(car)
    car.move(3, -60)
    print(car)
    car.enter(3)
    print(car)
    bus.enter(5)
    print(bus)
    bus.exit(4)
    print(bus)
    bus.enter(2)
    print(bus)
except WrongPassengerCount:
    print('Неверное кол-во пассажиров')
