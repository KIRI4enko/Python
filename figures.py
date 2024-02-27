'''
    Нахождение объема, массы фигуры(ООП)
    Finding the volume, mass of a figure (OOP)
'''
import abc
import math


class Figure:
    def __init__(self, p: float):
        self.p = p

    @abc.abstractmethod
    def calculateVolume(self) -> float:
        pass

    def calculateWeight(self) -> float:
        return self.calculateVolume() * self.p


class Cube(Figure):
    def __init__(self, side: float, p: float):
        super().__init__(p)
        self.side = side

    def __str__(self):
        return f'Куб со стороной {self.side} и плотностью {self.p}'

    def calculateVolume(self) -> float:
        return self.side ** 3


class Sphere(Figure):
    def __init__(self, r: float, p: float):
        super().__init__(p)
        self.r = r

    def __str__(self):
        return f'Шар с радиусом {self.r} и плотностью {self.p}'

    def calculateVolume(self) -> float:
        return 0.75 * math.pi * self.r ** 3


class Cilynder(Figure):
    def __init__(self, r: float, h: float, p: float):
        super().__init__(p)
        self.r = r
        self.h = h

    def __str__(self):
        return f'Цилиндр с радиусом основания {self.r}, высотой {self.h}, плотностью {self.p}'

    def calculateVolume(self) -> float:
        return self.h * math.pi * self.r ** 2


cilynder = Cilynder(3, 5, 2)
print(cilynder)
print(cilynder.calculateVolume())
print(cilynder.calculateWeight())
