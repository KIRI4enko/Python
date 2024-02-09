'''Перестановки с заданным числом повторов
Написать функцию, возвращающую все последовательности на основе представленного алфавита,
в которых элементы повторяются не более K раз.
На вход подаётся алфавит (строка уникальных символов) и число K.


def posl(az, prefix, n, k):  # az - alphabet, n - len, k - replacement
    if n == 0:
        return [prefix]
    res = []
    for i in az:
        next_prefix = prefix + [i]
        next_az = ''
        for a in az:
            if next_prefix.count(a) < k:
                next_az += a
        p = posl(next_az, next_prefix, n - 1, k)
        for perm in p:
            res.append(perm)
    return res


def main(az, k):
    for i in posl(az, [], len(az), k):
        print(''.join(i))


string = input('Введите алфавит с уникальными символами: ')
count = int(input('Введите число K: '))
if __name__ == '__main__':
    main(string, count)
'''  # Перестановки с заданным числом повторов
''' 
from random import randint

a = []
N = randint(1, 100)
for i in range(N):
    a.append(randint(1, 10000))
print(a)


def qsort(list):
    if len(list) <= 1:
        return list
    else:
        m = list[0]
        mid = []
        less = []
        bet = []
        for i in list:
            if i < m:
                less.append(i)
            elif i > m:
                bet.append(i)
            else:
                mid.append(i)
        return qsort(less) + mid + qsort(bet)


print(qsort(a))

'''  # Сортировка
''' Разбиение на неубывающие слагаемые
Дано натуральное число n. 
Выведите всевозможные его разбиения на слагаемые, упорядоченные в порядке неубывания. 
Сами разбиения необходимо выводить в лексикографическом порядке.


def summa(n, prefix):
    if sum(prefix) == n:
        return [prefix]
    elif sum(prefix) > n:
        return [None]
    elif sum(prefix) < n:
        res = []
        az = (range(1, n + 1))
        new_az = az
        if len(prefix) != 0:
            new_az = list(filter(lambda x: x >= prefix[-1], az))
        for i in new_az:
            next_prefix = prefix + [i]
            p = summa(n, next_prefix)
            for a in p:
                if a != None:
                    res.append(a)
        return res


n = int(input('Введите число: '))


def main(n):
    for i in summa(n, []):
        print(*i, sep=' ')


if __name__ == '__main__':
    main(n)
'''  # Разбиение на неубывающие слагаемые
''' Разбиение на k невозрастающих слагаемых
Даны натуральные числа n и k (1 <= k <= n).
Выведите всевозможные разбиения числа n на k слагаемых, 
упорядоченных в порядке невозрастания. 
Сами разбиения необходимо выводить в лексикографическом порядке.


def f(n, k, prefix):
    if sum(prefix) == n and k == 0:
        return [prefix]
    elif sum(prefix) > n:
        return [None]
    res = []
    new_az = range(1, n + 1)
    if len(prefix) != 0:
        new_az = list(filter(lambda x: x <= prefix[-1], new_az))
    for i in new_az:
        next_prefix = prefix + [i]
        p = f(n, k - 1, next_prefix)
        for a in p:
            if a != None:
                res.append(a)
    return res


def main(n, k):
    for i in f(n, k, []):
        print(*i, sep=' ')


l = list(map(int, input('Введите число N и число K (в одну строку через пробел): ').split()))

if __name__ == '__main__':
    main(l[0], l[1])
'''  # Разбиение на k невозрастающих слагаемых
''' Метод Симпсона
Посчитать площадь(интеграл) функции f от a до b.
Функция f и a, b задаются через параметры.
Площадь параболы может быть найдена суммированием площадей 6 прямоугольников равной ширины.
Высота первого из них должна быть равна f(a), со второго по пятый — f(m), шестого — f(b).
def integral(f, a, b):
    step = (b - a) / 6
    area = 0
    y = f(a)
    area += step * y
    for i in range(1,5):
        x = a + step * (i+0.5)
        y = f(x)
        area += step * y
    y = f(b)
    area += step * y
    return area

f = lambda x: x
print(integral(f,1,5))'''  # Метод Симпсона
'''
import os

file_name = input('Имя файла: ')
if os.path.exists(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        for string in file:
            print(string, end='')
else:
    with open(file_name, mode='w', encoding='utf-8') as file:
        string = ' '
        while string != '':
            string = input('Введите данные: ')
            file.write(string + '\n')
'''  # Работа с файлами и ОС
'''
# Задание 1
def func1(n):
    res = []
    for i in range(1, n + 1):
        res.append(i)
    return res

# Задание 2
def func2(w):
    iof = w.split()
    res = ''
    for i in range(3):
        res += iof[i][0] + '.'
    return res

# Задание 3
from functools import reduce
nums = (2,3,5,2)
def func3(nums):
    return (reduce(lambda a, b: a * b, nums))


# Задание 4
def func4(w1, w2):
    return len(w1) == len(w2)

# Задание 5
regions = ["Томская область", "Московская область", "Ленинградская область"]
cities = ["Томск", "Москва", "Санкт-Петербург"]
pop = [1051, 8594, 2027]
result = zip(regions,cities,pop)
for r in result:
    print(f'{r[0]}: столица {r[1]}, население {r[2]} тыс. человек.')
'''  # Аттестация (2 модуль)
'''
import csv
import math
with open('output.csv', 'w') as file:
    csv_file = csv.writer(file)
    r = int(input("Введите радиус: "))
    d_alpha = float(input('Введите шаг по углу: '))
    results = []
    alpha = 0
    while alpha <= 360.0:
        alpha_rad = alpha * math.pi / 180.0
        x = math.cos(alpha_rad) * r
        y = math.sin(alpha_rad) * r
        results.append([alpha, x, y])
        alpha += d_alpha

    for line in results:
        csv_file.writerow(line)
'''  # Движение по окружности по заданному углу(значения записываются в файл)
''' На вход программе подается текстовый файл следующего вида:
Символы алфавита …{N}… Символы алфавита
Где N – целое число (таких конструкций может быть несколько)
Необходимо открыть файл, прочитать его содержимое и запросить у пользователя ввести N строк,
на которые необходимо будет заменить соответствующую цифру в новом созданном файле
Например:
Гипотенуза равна корню из {0} квадратов {2}
Гипотенуза равна корню из суммы квадратов катетов

with open('input.txt', mode='r', encoding='utf-8') as file_input:
    i = file_input.read()
    print(i)
    numbers = []
    for x in range(len(i)):
        if i[x] == '{':
            y = x + 1
            num = ''
            while i[y] != '}':
                num += i[y]
                y += 1
            numbers.append(int(num)) # Нашли номера
    print(numbers)
    with open('output.txt', mode='w', encoding='utf-8') as file_output:
        for x in numbers:
            N = input('Замените {'f'{x}''}: ')
            i = i.replace('{'f'{x}''}', N, 1)
        print(i + ' (Записано в файл output.txt)')
        file_output.write(i)
'''  # Замена в файле
''' Функция, которая возвращает квадратную матрицу с числами от 1 до n^2
import numpy

def matrix(n):
    mtrx = numpy.arange(1, n**2 + 1).reshape(n, n)
    return mtrx

if __name__ == '__main__':
    n = int(input('Введите число n: '))
    print(matrix(n))
'''  # Numpy: Квадратная матрица с числами от 1 до n^2
''' Рассмотрим массив 16 на 16, как получить сумму блоков (размер блока 4x4)
import numpy as np

mass = np.random.randint(1,10,(16,16))
print(mass)
s = np.array([[0]*4]*4)
for i in range(4):
    su = 0
    for j in range(4):
        s[i][j] = np.sum(mass[i * 4:(i + 1) * 4, j:(j + 1) * 4] ) - su
        su += s[i][j]
print(s)'''  # Numpy: Сумма блоков
'''
import numpy as np

n = int(input())
n1 = n
mtrx = np.random.randint(1,100,(5,5))
mtrx_flat = np.bincount(mtrx.flatten())
maxim = []
len_flat = len(mtrx_flat) - 1
i = 0
while n > 0:
    if mtrx_flat[-1 - i] != 0:
        maxim.append(len_flat - i)
        n -= 1
    i += 1

print(f'{n1} наибольших значения: ', *maxim)'''  # Numpy: Получить n наибольших значений массива
'''
import numpy as np

arr1 = np.random.randint(1,10,(3,3)).flatten()
arr2 = np.random.randint(1,10,(3,3)).flatten()
print(arr1,arr2,sep='\n')
boo = arr1 == arr2
inds = []
for i in range(len(boo)):
    if boo[i] == True:
        inds.append(i)

if len(inds) == 0:
    print('Нет совпадающих элементов')
else:
    inds = ', '.join(list(map(str,inds)))
    print('Индексы, в которых элементы совпадают: ', inds)'''  # Numpy: Получить индексы, в которых элементы совпадают.
'''
import numpy as np

mass = np.random.randint(1,21,(3,3))

ms = np.bincount(mass.flatten())

cnt = np.count_nonzero(ms)'''  # Numpy: Подсчитать количество уникальных значений в numpy массиве.
''' Написать функцию, вычисляющую скользящее среднее (среднее по части элементов массива)
import numpy as np

def moving_average(arr: np.ndarray, window_size:int) -> np.ndarray:
    res = []
    for i in range(len(arr) - (window_size - 1)):
        res += [sum(arr[i:i+window_size]) / window_size]
    return np.array(res)
m = np.array([8,8,3,7,7,0,4,2,5,2])
print(moving_average(m, 3))'''  # Numpy: Cкользящее среднее
''' Поменять 2 случайных столбца в двумерном numpy массиве 

import numpy as np
def main():
    size_mtrx = [0]
    while len(size_mtrx) <= 1 or len(size_mtrx) > 2:
        string = input('Введите через запятую размеры двумерного numpy массива: ')
        if string == '':
            print('ОШИБКА!!!')
        else:
            try: size_mtrx = list(map(int, string.split(',')))
            except ValueError:
                if len(size_mtrx) <= 1 or len(size_mtrx) > 2:
                    print('ОШИБКА!!!')
    mtrx = np.random.randint(1,10,size_mtrx)
    print(mtrx)
    nums = ''
    while nums == '' or max(size_mtrx) < maxim:
        nums = input('Введите через запятую номера двух столбцов, которые необходимо поменять местами: ')
        maxim = max(list(map(int, nums.split(','))))
        if nums != '':
            numbers = list(map(lambda x: int(x) - 1, nums.split(',')))
    for string in mtrx:
        string[numbers[0]], string[numbers[1]] = string[numbers[1]], string[numbers[0]]
    print(mtrx)

if __name__ == '__main__':
    main()
'''  # Numpy: Перестановка двух столбцов
''' Пример: ab2[dr3[x]] -> abdrxxxdrxxx

def normalize(string):
    result = ''
    az = 'abcdefghijklmnopqrstuvwxyz'
    nums = '0123456789'
    az += az.upper()
    for s in range(len(string)):
        if string[s] in az:
            result += string[s]
        else:
            if string[s] in nums:
                n = string[s]
                f = 1
                while string[s+f] != '[':
                    n += string[s+f]
                    f += 1
                indl = s + 1
                indp = string.find(']', -1)
                return result + int(n) * normalize(string[indl + 1 : indp])
    return result

print(normalize('a2[b2[c]4[d]]'))'''  # Задача с собеседования GOOGLE
'''
def generate_password(len=8):
    from random import choice
    az = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    az += [i.upper() for i in az] + [str(a) for a in range(10)]
    return ''.join([choice(az) for _ in range(len)])


print(generate_password(10))'''  # Генератор пароля
'''
import time
def close_friday_13(date: time.struct_time = time.localtime()):
    import time
    seconds = time.mktime(date)
    cnt_day = 0
    date = time.localtime(seconds)
    sec = 60 * 60 * 24
    while 1 > 0:
        if date.tm_wday == 4 and date.tm_mday == 13:
            break
        else:
            cnt_day += 1
            seconds += sec
            date = time.localtime(seconds)
    print(time.strftime('%d.%m.%Y', date))
    return cnt_day
print(close_friday_13())'''  # Ближайшая пятница 13
'''
from functools import wraps
n = int(input('Количество вызовов функции: '))

def twice(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
    return wrapper


def repeat(n:int):
   def inner_func(function):
       @wraps(function)
       def wrapper(*args,**kwargs):

           for i in range(n):
               print(function(*args,**kwargs))
           return
       return wrapper
   return inner_func

@repeat(n)
def hello():
    return 'HELLO world'

hello()'''  # Декоратор, позволяющий вызвать ф-ию заданное количество раз
'''
from functools import wraps


def logger(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        res = None
        try:
            res = function(*args,**kwargs)
        except TypeError:
            print('Вы неправильно ввели аргументы')
        except ZeroDivisionError:
            print('НЕЛЬЗЯ ДЕЛИТЬ НА 0!!!')
        else:
            print(f'Выполнилась фунцкия {function.__name__},\nкоторая приняла в себя два аргумента', *args,*kwargs.values(), f'.\nРезультат: {res}')
        finally:
            return res
    return wrapper


@logger
def div(a:(float,int),b:(float,int)):
    return a/b

div(10,2)'''  # Декоратор-логгер
'''
from functools import wraps


def cache(size):
    cache_dir = {}

    def f(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            name = str(function.__name__) + '(' + ','.join(list(map(str, args))) + ')'

            if name in cache_dir.keys():
                print('Есть в кэше ', name,'и равен ->' ,cache_dir[name])
                return cache_dir[name]

            else:
                cache_dir[name] = function(*args, **kwargs)
                if size is not None:
                    if len(cache_dir) > size:
                        cache_dir.pop(list(cache_dir.keys())[0])

            print(cache_dir)
            return cache_dir[name]
        return wrapper

    return f

@cache(None)
def f(a):
    return a**2

for i in range(1,11):
    f(i)

for i in range(10,0,-1):
    f(i)

'''  # Декоратор-оптимизатор(свой lru_cache)
'''
class init_id:
    cnt = 1

    def __init__(self):
        self.id = init_id.cnt
        init_id.cnt += 1


class Soldiers(init_id):
    __counter = 1

    def __init__(self, team: str):
        super().__init__()
        self.team = team
        self.hero = None

    def go_to_hero(self, hero):
        if hero.team == self.team and type(hero) == Heroes:
            self.hero = hero
            return hero
        else:
            return None

    def __str__(self):
        if self.hero is not None:
            return f'Soldier ID: {self.id}, Team: {self.team}, Hero: {self.hero.id}'
        else:
            return f'Soldier ID: {self.id}, Team: {self.team}'


class Heroes(init_id):
    __counter = 1

    def __init__(self, team: str):
        super().__init__()
        self.team = team
        self.level = 1

    def increase_level(self):
        self.level += 1

    def __str__(self):
        return f'Hero ID: {self.id}, Team: {self.team}, Level: {self.level}'


import random

hero_red = Heroes('RED')
hero_blue = Heroes('BLUE')
teams = ['RED', 'BLUE']
team_red = [hero_red]
team_blue = [hero_blue]
for i in range(2, random.randint(2, 10)):
    if random.choice(teams) == 'RED':
        team_red.append(Soldiers('RED'))
    else:
        team_blue.append(Soldiers('BLUE'))

if len(team_red) > len(team_blue):
    hero_red.increase_level()
elif len(team_blue) > len(team_red):
    hero_blue.increase_level()

print('RED', len(team_red), *[i for i in team_red], sep='\n')
print('\n\nBLUE', len(team_blue), *[i for i in team_blue], '\n\n', sep='\n')
print(hero_red)
print(hero_blue)'''  # Солдаты и герои
'''
import random


class Card:
    suit_list = ['БУБИ', 'ЧЕРВЫ', 'ПИКИ', 'КРЕСТИ']
    nums_list = list(map(str, range(6, 11))) + ['Валет', "Дама", "Король", "Туз"]

    def __init__(self, suit_number: int, value: int):
        self.suit = Card.suit_list[suit_number]
        self.value = Card.nums_list[value]

    def __str__(self):
        return f'{self.value} {self.suit}'


class DeckOfCards:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for value in range(9):
                self.deck.append(Card(suit_number=suit, value=value))

    def __str__(self):
        return '\n'.join(list(map(str, self.deck)))

    def Shuffle_Deck(self):
        random.shuffle(self.deck)

    def Peak_Card(self):
        return self.deck.pop(0)





Deck = DeckOfCards()
print(Deck)
Deck.Shuffle_Deck()
print('*'*100)
print(Deck)
print('=='*100)
P1 = []
P2 = []
while len(Deck.deck) != 0:
    P1.append(Deck.Peak_Card())
    P2.append(Deck.Peak_Card())

print(*P1,sep='\n')
print('=='*100)
print(*P2,sep='\n')
'''  # Колода карт
'''
class Equipment:
    def __init__(self, manufacter: str, model_name: str, year: int):
        self.manufacture = manufacter
        self.model_name = model_name
        self.year = year

    def __str__(self):
        return f'{self.manufacture} {self.model_name} {self.year}'

    def action(self):
        print('Не определен')

class Scaner(Equipment):
    def __init__(self, manufacture: str, model_name: str, year: int):
        super().__init__(manufacture, model_name, year)

    def action(self):
        print('Сканирует')

class Xerox(Equipment):
    def __init__(self, manufacture: str, model_name: str, year: int):
        super().__init__(manufacture, model_name, year)

    def action(self):
        print('Копирует')

class Printer(Equipment):
    def __init__(self, manufacture: str, model_name: str, year: int, is_color: bool):
        super().__init__(manufacture, model_name, year)
        self.is_color = is_color

    def __str__(self):
        return str(super().__str__()) + (' цветной' if self.is_color else  ' черно-белый')

    def action(self):
        print('Печатает')


scaner = Scaner('HP', 'model', 2020)
xerox = Xerox('HP', 'model', 2021)
printer = Printer('HP', 'model', 2019, False)

print(scaner)
scaner.action()
print(xerox)
xerox.action()
print(printer)
printer.action()'''
'''
import math


class Car:
    def __init__(self, x: float = 0, y: float = 0, angle: int = 0):
        self._x = x
        self._y = y
        self._angle = angle%360
        self._cnt_pass = 0
        self._cnt_money = 0

    def move(self, s: float = 0, angle: int = 0):
        self._angle = (self._angle + angle)%360
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
        super().enter(cnt_pass_enter,cnt_enter)

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
    bus.exit(10)
    print(bus)
    bus.enter(2)
    print(bus)
except WrongPassengerCount:
    print('Неверное кол-во пассажиров')


'''  # Движение машины(ООП)
'''

class Client:
    unique_id = 1
    client_base = []

    def __init__(self, full_name: str, data_vk, size_vk: int, percent_vk: int):
        self._id = Client.unique_id
        self._full_name = full_name
        self._data_vk = data_vk
        self._size_vk = size_vk
        self._percent_vk = percent_vk
        Client.unique_id += 1
        Client.client_base.append(self)

    def __str__(self):
        return f'{self._id}\t{self._full_name}\t{self._data_vk}\t{self._size_vk}\t{self._percent_vk}'


class Bank:
    def __init__(self):
        self._client_base = Client.client_base

    def __str__(self):
        return '\n'.join([Client.__str__(client) for client in self._client_base])

    def showByMoney(self,money):
        for client in self._client_base:
            if client._size_vk > money:
                print(client)

    def showByProc(self,proc):
        for client in self._client_base:
            if client._percent_vk > proc:
                print(client)

    def showByCode(self,id):
        for client in self._client_base:
            if client._id == id:
                print(client)
                return
c3 = Client('qwert','228',1337,1)
bank = Bank()
c1 = Client('abc', '123', 20000, 15)
c2 = Client('ZXC', '777', 50000, 13)
print(bank)
print('='*100)
bank.showByMoney(10000)
print('='*100)
bank.showByCode(3)
print('='*100)
bank.showByProc(14)'''  # Банк(ООП)
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


cilyn = Cilynder(3, 5, 2)
print(cilyn)
print(cilyn.calculateVolume())
print(cilyn.calculateWeight())'''  # Фигуры(ООП)
'''
class SnowFlake:
    def __init__(self, n: int):
        self.n = n
        self._snow = [['-' for _ in range(n)] for _ in range(n)]
        for i in range(n):
            self._snow[i][i] = '*'
            self._snow[i][-1-i] = '*'
            self._snow[n//2][i] = '*'
            self._snow[i][n//2] = '*'

    def snow(self):
        for i in self._snow:
            print(''.join(i))

    def thaw(self,n: int):
        for i in range(n):
            for j in range(self.n):
                self._snow[i][j] = '-'
                self._snow[-1-i][j] = '-'
                self._snow[j][i] = '-'
                self._snow[j][-1-i] = '-'
        return n

    def thicken(self):
        buf = [[i for i in line] for line in self._snow]
        for i in range(1,self.n - 1):
            for j in range(1,self.n - 1):
                if self._snow[i][j] == '*':
                    buf[i-1][j] = '*'
                    buf[i][j-1] = '*'
                    buf[i+1][j] = '*'
                    buf[i][j+1] = '*'
        self._snow = buf

snow = SnowFlake(15)
snow.snow()
print(snow.thaw(1))
snow.snow()
snow.thicken()
snow.snow() '''  # Снежинка(ООП)
'''
import random


def bubble_sort(_list: list):

    list = [i for i in _list]

    changed = True
    while changed:
        changed = False
        for i in range(len(list) - 1):

            if list[i] > list[i + 1]:
                list[i + 1], list[i] = list[i], list[i + 1]

                changed = True

    return list


a = [random.randint(1, 1000) for _ in range(10)]


def insertion_sort(_list: list):
    list = [i for i in _list]
    for i in range(1, len(list)):
        key_elem = list[i]
        j = i - 1

        while j >= 0 and list[j] > key_elem:

            list[j + 1] = list[j]
            print(list)
            j -= 1

        list[j + 1] = key_elem

    return list


def cocktail(_lst: list):
    lst = [i for i in _lst]
    for i in range(len(lst) // 2):
        changed = False
        for j in range(i + 1, len(lst) - i):
            if lst[j] < lst[j - 1]:
                lst[j],lst[j-1] = lst[j-1],lst[j]
                changed = True
        if not changed:
            break
        for j in range(len(lst) - i - 1, i, -1):
            if lst[j] < lst[j - 1]:
                lst[j],lst[j-1] = lst[j-1],lst[j]
                changed = True
        if not changed:
            break
    return lst

print(a)
print(cocktail(a ))'''
'''

import tkinter as tk


def draw_circle(c: tk.Canvas, x, y, r, width=3, color='black'):
    c.create_oval(x - r, y - r, x + r, y + r, width=width, outline=color)


root = tk.Tk()

canvas = tk.Canvas(width=1200, height=1000)

canvas.create_line(100, 600, 1100, 600, arrow='last', width=1)
canvas.create_line(600, 1100, 600, 100, arrow='last', width=5)


def f(x):
    if x != 0:
        return 6666 / x
    return 100000000000000


for x in range(-500, 500):
    y = -f(x)
    x_next = x + 1
    y_next = -f(x_next)
    canvas.create_line(x+600, y+600, x_next+600, y_next+600, width=3)

canvas.pack()
root.mainloop()'''  # График y = 1/x
'''
from tkinter import *


class PaintApp:
    def __init__(self, root: Tk):
        self.root = root
        self.canvas: Canvas = Canvas(self.root, width=800, height=600)
        self.width = 1
        self.canvas.pack()
        self.is_draw = False
        self.prev_x = None
        self.prev_y = None
        self.red = 0
        self.green = 0
        self.blue = 0
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.canvas.bind('<MouseWheel>', self.up_width)
        self.canvas.bind_all('<Shift-MouseWheel>', self.down_width)
        self.canvas.bind_all('r', self.up_red)
        self.canvas.bind_all('<Shift-R>', self.down_red)
        self.canvas.bind_all('g', self.up_green)
        self.canvas.bind_all('<Shift-G>', self.down_green)
        self.canvas.bind_all('b', self.up_blue)
        self.canvas.bind_all('<Shift-B>', self.down_blue)
        self.fill = f'#{hex(self.red )[2:]}{hex(self.green)[2:]}{hex(self.blue)[2:]}'

    def up_red(self, event):
        if self.red <= 14:
            self.red += 1

    def down_red(self, event):
        if self.red >= 2:
            self.red -= 1

    def up_green(self, event):
        if self.green <= 14:
            self.green += 1

    def down_green(self, event):
        if self.green >= 2:
            self.green -= 1

    def up_blue(self, event):
        if self.blue <= 14:
            self.blue += 1

    def down_blue(self, event):
        if self.blue >= 2:
            self.blue -= 1

    def up_width(self, event):
        self.width += 1
        print(self.width)

    def down_width(self, event):
        if self.width >= 2:
            self.width -= 2
            print('Толщина = ', self.width)

    def draw(self, event):
        if self.is_draw:
            self.fill = f'#{hex(self.red)[2:]}{hex(self.green)[2:]}{hex(self.blue)[2:]}'
            if self.prev_x and self.prev_y:
                self.canvas.create_line(self.prev_x, self.prev_y, event.x, event.y, width=self.width, fill=self.fill)
        self.prev_x = event.x
        self.prev_y = event.y

    def start_draw(self, event):
        self.is_draw = True

    def reset(self, event):
        self.is_draw = False
        self.prev_x = None
        self.prev_y = None


root = Tk()
paint_app = PaintApp(root)
root.mainloop()
'''  # Paint
'''from tkinter import *


class App(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = 'Tk',
                 useTk: bool = True, sync: bool = False, use: str | None = None):
        super().__init__(screenName=screenName, baseName=baseName, className=className, useTk=useTk, sync=sync, use=use)
        self.geometry = ('250x250')
        self.btn = Button(text='Нажми', command=self.click_button, bg='gray')
        self.btn.pack()
        self.clicks = 0

    def click_button(self):
        self.clicks += 1
        self.btn['text'] = f'Нажатий: {self.clicks}'


App().mainloop()'''  # Кол-во нажатий на кнопку
'''from tkinter import *

root = Tk()
c = Canvas(width=300,height=100, bg='white')
c.focus_set()
c.pack()

ball = c.create_oval(140,40,160,60,fill='red')
c.bind('<Left>', lambda e: c.move(ball, -2,0))
c.bind('<Right>', lambda e: c.move(ball, 2,0))
c.bind('<Up>', lambda e: c.move(ball, 0,-2))
c.bind('<Down>', lambda e: c.move(ball,0 ,2))


root.mainloop()'''  # Red Ball
'''
from tkinter import *
import re

root = Tk()
root.geometry('600x400')


def change_mode():
    if btnmode['text'] == 'Из градусов Цельсия в Фаренгейты':
        btnmode['text'] = 'Из градусов Фаренгейта в Цельсия'
        lbl2['text'] = lbl2['text'].replace('Цельсиях', 'Фаренгейтах')
    else:
        btnmode['text'] = 'Из градусов Цельсия в Фаренгейты'
        lbl2['text'] = lbl2['text'].replace('Фаренгейтах', 'Цельсиях')


label = Label(root, text='Калькулятор температуры \n', font='Arial 20')
lbl2 = Label(root, text='Введите температуру в Цельсиях', font='Arial 18')
btnmode = Button(root, text='Из градусов Цельсия в Фаренгейты', command=change_mode, font='Arial 20')


def is_valid(new: str):
    res = re.match(r"(\+|\-)?\d+(\.\d+)?$", new)
    return res is not None


def answer():
    ans['text'] = 'Ответ :'
    num = ent.get()
    if num != '':
        num = float(num)
        if btnmode['text'] == 'Из градусов Цельсия в Фаренгейты':
            ans['text'] += str(round(num * 9 / 5 + 32, 3))
        else:
            ans['text'] += str(round((num - 32) * 5 / 9, 3))


ent = Entry(root, validate="key", validatecommand=(root.register(is_valid), "%P"))
btnans = Button(root, text='Найти', command=answer)
ans = Label(root, font='Arial 25', text='Ответ: ')

label.pack()
btnmode.pack()
lbl2.pack()
ent.pack()
btnans.pack()
ans.pack()

root.mainloop()'''  # Калькулятор тем-ры
'''from tkinter import *
from functools import partial


root = Tk()

first_op = 0
last_op = '+'


def insert(c: str):
    label['text'] += c


def plus():
    global first_op, last_op
    first_op = float(label['text'])
    label['text'] = ''
    last_op = '+'

def clear():
    global first_op,last_op
    label['text'] = ''
    first_op = 0
    last_op = ''


def minus():
    global first_op, last_op
    first_op = float(label['text'])
    label['text'] = ''
    last_op = '-'

def proiz():
    global first_op, last_op
    first_op = float(label['text'])
    label['text'] = ''
    last_op = '*'

def delen():
    global first_op, last_op
    first_op = float(label['text'])
    label['text'] = ''
    last_op = '/'


def eq():
    global first_op, last_op
    try:
        label['text'] = f'{commands[last_op](first_op, float(label["text"]))}'
    except ZeroDivisionError:
        label['text'] = 'ТЫ ЕБЛАН'
        #clear()

commands = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    'C': clear
}
label = Label(root, text='', font='Arial 30')
label.grid(columnspan=5)
btns_text = ['789/', '456*', '123+', '0-=C']
btns = []
for i, line in enumerate(btns_text):
    rowbtns = []
    for j, c in enumerate(line):
        btn = Button(text=str(c), padx=3, pady=3, width=3, font='Arial 25')
        if c.isdigit():
            btn['command'] = partial(insert, c)
        elif c == '=':
            btn['command'] = eq
        elif c == '+':
            btn['command'] = plus
        elif c == 'C':
            btn['command'] = clear
        elif c == '-':
            btn['command'] = minus
        elif c == '*':
            btn['command'] = proiz
        elif c == '/':
            btn['command'] = delen
        btn.grid(row=i + 1, column=j)
        rowbtns.append(btn)
    btns.append(rowbtns)

root.mainloop()'''  # КАЛЬКУЛЯТОР
'''from tkinter import *


def up():
    global square
    coords = canvas.coords(square)
    if coords[1] >= 5:
        canvas.move(square, 0, -1)
    root.after(10, up)


def down():
    global square, geo
    coords = canvas.coords(square)
    if coords[3] <= geo[1] - 5:
        canvas.move(square, 0, 1)
    root.after(10, down)


def left():
    global square, geo
    coords = canvas.coords(square)
    if coords[0] >= 5:
        canvas.move(square, -1, 0)
    root.after(10, left)


def right():
    global square, geo
    coords = canvas.coords(square)
    if coords[2] <= geo[0] - 5:
        canvas.move(square, 1, 0)
    root.after(10, right)


geo = [800, 600]

root = Tk()
canvas = Canvas(root, width=geo[0], height=geo[1], bg='gray')
canvas.pack()
square = canvas.create_rectangle(10, 10, 110, 110, fill='#11FF11',width=2)

root.bind('<Up>', lambda e: up())
root.bind('<Down>', lambda e: down())
root.bind('<Left>', lambda e: left())
root.bind('<Right>', lambda e: right())
'''
'''import tkinter as tk
import random


class MoveRect(tk.Tk):

    def __init__(self, w=1440, h=900, sq_size=60):
        super().__init__()
        self.canvas = tk.Canvas(self, width=w, height=h, bg='#112F11')
        self.btnX = tk.Button(self, text='ВЫЙТИ', command=self.Exit, foreground='red', bg='white')

        self.btnX.pack()
        self.count = 1
        self.Count = tk.Label(self, text=f'СЧЁТ :{self.count}', font='Arial 18', foreground='white', bg='black')
        self.Count.pack()
        self.w = w
        self.h = h
        self.canvas.pack()
        self.coords = []
        self.exit = False
        self.apple = None
        self.sq_size = int(sq_size)
        self.squares = [self.canvas.create_rectangle((i * sq_size, 0),
                                                     ((i - 1) * sq_size, sq_size),
                                                     fill=f'#111F11') for i in range(self.count, 0, -1)
                        ]
        self.vector = (self.sq_size, 0)
        self.bind_all('<Up>', lambda e: self.up())
        self.bind_all('<Down>', lambda e: self.down())
        self.bind_all('<Left>', lambda e: self.left())
        self.bind_all('<Right>', lambda e: self.right())
        self.apple_alive = False
        self.canvas.create_line(0, 0, 0, h, width=3, fill='white')
        self.canvas.create_line(w, 0, w, h, width=3, fill='white')
        self.canvas.create_line(0, h, w, h, width=3, fill='white')
        self.canvas.create_line(0, 0, w, 0, width=3, fill='white')

    def motion(self):
        self.coords = []
        self.die = False

        self.prev_coords = self.canvas.coords(self.squares[-1])

        for i in range(len(self.squares)):

            self.c = list(map(lambda e: e - 1, self.canvas.coords(self.squares[i])[0:2]))
            if self.c in self.coords:
                self.die = True
                break
            else:
                self.coords.append(self.c)
        self.coordhead = self.canvas.coords(self.squares[0])
        if self.coordhead[0] < 0 or self.coordhead[1] < 0 or self.coordhead[
            2] > self.w or self.coordhead[3] > self.h:
            self.die = True

        if not self.die:
            coords_h = self.canvas.coords(self.squares[0])
            self.canvas.move(self.squares[0], *self.vector)

            for i in range(2, len(self.squares) + 1):
                self.canvas.moveto(self.squares[i - 1], *list(self.coords[i - 2]))

            if not self.apple_alive:
                self.squares.append(self.canvas.create_rectangle(self.prev_coords, fill=f'#111F11'))

            self.after(100-self.count, self.motion)
            self.spawn_apple()
            self.eat_apple()

        else:
            self.DIE()
        self.coordhead = self.canvas.coords(self.squares[0])

    def DIE(self):

        self.Die = tk.Tk()
        label = tk.Label(self.Die, text='ВЫ ПРОИГРАЛИ \n '
                                        f'Счёт :{self.count}', foreground='black', font='Arial 32')
        label.pack()
        btnretry = tk.Button(self.Die, text='Сыграть еще раз', command=self.retry, width=20, height=2,
                             font='Arial 18', )
        btnretry.pack()
        btnexit = tk.Button(self.Die, text='Закрыть', command=self.Exit, width=20, height=2, font='Arial 18', )
        btnexit.pack()

    def eat_apple(self):
        if self.apple_alive:
            coords_head = self.canvas.coords(1)
            coords_apple = self.canvas.coords(self.apple)

            eat = True
            for i in range(4):
                if coords_head[i] != coords_apple[i]:
                    eat = False
            if eat:
                self.count += 1
                self.Count['text'] = f'Счёт :{self.count}'
                self.apple_alive = False
                self.canvas.delete(self.apple)

    def spawn_apple(self):
        if not self.apple_alive:
            dw = self.w // self.sq_size - 1
            dh = self.h // self.sq_size - 1

            free = False
            while not free:
                rnd = [random.randint(0, dw), random.randint(0, dh)]
                self.coord_apple = [rnd[0] * self.sq_size,
                                    rnd[1] * self.sq_size,
                                    (rnd[0] + 1) * self.sq_size,
                                    (rnd[1] + 1) * self.sq_size]
                for i in range(len(self.squares)):
                    self.coord = self.canvas.coords(self.squares[i])
                    for j in range(4):
                        if self.coord[j] != self.coord_apple[j]:
                            free = True

            self.apple = self.canvas.create_oval(self.coord_apple, fill='red', width=2)
            self.apple_alive = True

    def up(self):
        if self.vector != (0, self.sq_size):
            self.vector = (0, -self.sq_size)

    def down(self):
        if self.vector != (0, -self.sq_size):
            self.vector = (0, self.sq_size)

    def right(self):
        if self.vector != (-self.sq_size, 0):
            self.vector = (self.sq_size, 0)

    def left(self):
        if self.vector != (self.sq_size, 0):
            self.vector = (-self.sq_size, 0)

    def retry(self):
        moveApp.destroy()
        self.Die.destroy()

    def Exit(self):
        global exit
        exit = True
        self.destroy()
        if self.die:
            self.Die.destroy()


if __name__ == '__main__':
    exit = False
    while not exit:
        moveApp = MoveRect()
        moveApp.motion()
        moveApp.mainloop()'''  # ЗМЕЙКА
'''import tkinter as tk
from functools import partial


class KN(tk.Tk):
    def __init__(self):
        super().__init__()
        self.new_game()
        self.endgame()

    def create_game(self):
        self.buttons = []
        for i in range(3):
            buttons_line = []
            for j in range(3):
                btn = tk.Button(text='', width=3, command=partial(self.HOD, i, j), font='Arial 40')
                buttons_line.append(btn)
                btn.grid(row=i, column=j)
            self.buttons.append(buttons_line)
        self.label_player = tk.Label(self, text='Ходит 1-й  игрок', font='Arial 20')
        self.label_player.grid(columnspan=3, rowspan=2)

    def new_game(self):
        self.choice_player = 0
        self.end_game = False
        self.create_game()

    def retry(self):
        self.end.destroy()
        self.new_game()

    def endgame(self):
        if self.end_game:
            self.end = tk.Tk()
            self.label_player.destroy()
            if not self.tie:
                self.end_label = tk.Label(self.end, text=f'Выиграл {(self.choice_player - 1) % 2 + 1}-й игрок',
                                      font='Arial 30')
            else:
                self.end_label = tk.Label(self.end, text=f'Ничья',
                                          font='Arial 30')
            self.end_label.pack()
            self.btn_replay = tk.Button(self.end, text='Сыграть еще раз', command=self.retry, font='Arial 26')
            self.btn_replay.pack()

    def HOD(self, i, j):
        button = self.buttons[i][j]
        if button['text'] == '':
            if self.choice_player % 2 == 0:
                button['text'] = 'X'
                self.label_player['text'] = 'Ходит 2-й игрок'
            else:
                button['text'] = 'O'
                self.label_player['text'] = 'Ходит 1-й игрок'
        self.choice_player += 1
        self.diags()
        self.rows()
        self.columns()
        self.Tie()
        self.endgame()

    def Tie(self):
        if not self.end_game:
            self.tie = True
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]['text'] == '':
                        self.tie = False
                        break
                if not self.tie:
                    break
            if self.tie:
                self.end_game = True


    def diags(self):
        main = []
        second = []
        for i in range(3):
            main.append(self.buttons[i][i]['text'])
            second.append(self.buttons[i][-1 - i]['text'])
        if main.count('X') == 3 or main.count('O') == 3 or second.count('X') == 3 or second.count('O') == 3:
            self.end_game = True

    def rows(self):
        for i in range(3):
            prev = self.buttons[i][0]['text']
            end = True
            for j in range(1, 3):
                if self.buttons[i][j]['text'] != prev or self.buttons[i][j]['text'] == '':
                    end = False
                    break
            if end:
                break
        if end:
            self.end_game = True

    def columns(self):
        for i in range(3):
            prev = self.buttons[0][i]['text']
            end = True
            for j in range(1, 3):
                if self.buttons[j][i]['text'] != prev or self.buttons[j][i]['text'] == '':
                    end = False
                    break
            if end:
                break
        if end:
            self.end_game = True


KN().mainloop()'''  # Крестики-нолики
'''
from bs4 import BeautifulSoup
import requests

res = requests.get('https://quotes.toscrape.com/')
Quotes = []
Authors = []
Tags = []

if res:
    soup = BeautifulSoup(res.text, 'lxml')

    for q in soup.find_all('div', class_='quote'):
        quote = q.find('span', class_='text').text
        author = q.find('small').text
        tags = [i.text for i in q.findAll('a', class_='tag')]

        Quotes.append(quote)
        Authors.append(author)
        Tags.append(tags)

else:
    print(res.status_code)

for i in zip(Quotes,Authors,Tags):
    ans = f'Цитата: {i[0]}\nАвтор: {i[1]}\nТеги: {", ".join(i[2])}'
    print(ans)
    print('='*50)
'''  # Парсер цитат(1 страница)
'''from bs4 import BeautifulSoup
import requests
number_page = 1
res = requests.get(f'https://quotes.toscrape.com/')
Quotes = []
Authors = []
Tags = []


if res:
    soup = BeautifulSoup(res.text, 'lxml')
    while True:
        soup = BeautifulSoup(res.text, 'lxml')
        print(number_page)
        for q in soup.find_all('div', class_='quote'):
            quote = q.find('span', class_='text').text
            author = q.find('small').text
            tags = [i.text for i in q.findAll('a', class_='tag')]
            print(quote,author,sep='\n')
            print(*tags,sep=', ')
            print('='*70)
            Quotes.append(quote)
            Authors.append(author)
            Tags.append(tags)
        if soup.find('li', class_='next'):
            number_page += 1
            res = requests.get(f'https://quotes.toscrape.com/page/{number_page}')
        else:
            break

else:
    print(res.status_code)
'''  # Парсер цитат(все страницы)
'''from bs4 import BeautifulSoup
import requests

base_url = 'https://books.toscrape.com/catalogue/'
pages = {}
for number_page in range(1, 11):
    page = []
    url = base_url + f'category/books_1/page-{number_page}.html'
    res = requests.get(url)
    if res:
        bsoup = BeautifulSoup(res.text, 'lxml')
        for li in bsoup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
            title = li.findNext('h3').text
            price = li.findNext('p', class_='price_color').text[1::]
            a_book = li.findNext('h3').findNext('a')
            url_book = base_url + a_book['href'][6:]
            res_book = requests.get(url_book)
            if res_book:
                soup_book = BeautifulSoup(res_book.text, 'lxml')
                trs = soup_book.find_all('tr')
                upc = trs[0].findNext('td').text
                availability = trs[5].findNext('td').text
                page.append([title, price, upc, availability])
                print(title, price, upc, availability,'='*50,sep='\n')
            else:
                print('Ссылка на книгу не найдена')

        pages[f'{number_page}'] = page
    else:
        print('ERROR!!!')

#for num, page in pages.items():
    #print(num, page)
'''  # Парсер книг, их стоимости, UPC, кол-во(10 первых страниц)
'''from bs4 import BeautifulSoup
import requests
main_url = 'https://books.toscrape.com/'
res = requests.get('https://books.toscrape.com/catalogue/category/books_1/page-1.html')
root = BeautifulSoup(res.text, 'lxml')
img = root.find('img')
img_url = main_url + img['src'][9:]
img_res = requests.get(img_url)
print(img_res)
with open('img.jpg', 'wb') as f:
    f.write(img_res.content)'''  # Скачивание img
'''
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
res = requests.get(url)
winners = []
if res:
    soup = BeautifulSoup(res.text, 'lxml')
    table = soup.find('table')
    for tr in table.find_all('tr')[1:]:
        tds = tr.find_all_next('td')
        film = tds[0].text
        if tds[0].find('b'):
            year = tds[1].text
            nomin = tds[3].text
            if '[' in nomin:
                nomin = nomin[:nomin.find('[')]
            winner = [film, year, int(nomin)]
            winners.append(winner)
            

else:
    print(res.status_code)
for f in winners:
    print(f'Фильм {f[0]} в {f[1]} году выиграл в {f[2]} номинациях')
    '''  # Парсер таблицы(фильмы победители)
'''from bs4 import BeautifulSoup
import requests

main_url = 'https://rating.unecon.ru/'
url = main_url + 'index.php'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
courses = soup.find('li')
peoples = []
for a in courses.find_all('a'):
    if a.text == '4 курс':
        url_course = main_url + a['href']
        course_get = requests.get(url_course)
        soup_course = BeautifulSoup(course_get.text, 'lxml')
        napravs = soup_course.find_all('li')[3]
        for div in napravs.find_all('div', class_='options'):
            for a in div.findAllNext('a')[1:2]:
                url_naprav = main_url + a['href']
                naprav_get = requests.get(url_naprav)
                soup_naprav = BeautifulSoup(naprav_get.text, 'lxml')
                table = soup_naprav.find('table')
                tbody = table.find('tbody')
                for tr in tbody.find_all('tr'):
                    tds = tr.find_all('td')
                    cnt_pred = 0
                    full_name = tds[1].text
                    if full_name == '':
                        continue
                    number_group = tds[2].text
                    for pred in tds[3:-1]:
                        if pred.text != '':
                            cnt_pred += 1

                    try:
                        e_ball = float(tds[-1].text) / cnt_pred
                    except:
                        e_ball = 0
                    if e_ball > 100:
                        print(a.text)
                        print(full_name,number_group,e_ball)
                    peoples.append([e_ball, number_group, full_name])

peoples.sort()
for p in peoples[::-1]:
    print(*p,sep='\n')
    print('='*50)'''  # Парсер студентов
'''from bs4 import BeautifulSoup
import requests


def stringing(string):
    az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    az += az.lower() + '0123456789'
    flag = ''
    for i in string:
        if i in az:
            flag += i
    return flag


main_url = 'https://stackoverflow.com'
request = requests.get(main_url + '/users')
if request:
    soup_main = BeautifulSoup(request.text, 'lxml')
    list_users = soup_main.find('div', class_='d-grid grid__4 lg:grid__3 md:grid__2 sm:grid__1 g12')
    for user in list_users.find_all('div', class_='grid--item'):
        user_details = user.find('div', class_='user-details')
        user_a = user_details.find('a')
        user_name = stringing(user_a.text)
        user_url = main_url + user_a['href']
        request_user = requests.get(user_url)
        if request_user:
            soup_user = BeautifulSoup(request_user.text, 'lxml')
            user_stats = soup_user.find('div', class_='s-card fc-light bar-md').find_all('div',
                                                                                         class_='flex--item md:fl-auto')
            user_answers = stringing(user_stats[2].find('div').text)
            user_question = stringing(user_stats[3].find('div').text)
            number_page = 1
            badges_url = user_url + f'?tab=badges&sort-recent&page={number_page}'
            request_user_badges = requests.get(badges_url)
            list_badges = []
            cnt_pages = 1
            if request_user_badges:
                soup_badges = BeautifulSoup(request_user_badges.text, 'lxml')
                cnt_pages = int(
                soup_badges.find('div', class_='s-pagination site1 themed pager float-right').find_all('a')[-2].text
                                )
            else:
                print(request_user_badges.status_code)
            while number_page <= cnt_pages:
                badges_url = user_url + f'?tab=badges&sort-recent&page={number_page}'
                request_user_badges = requests.get(badges_url)
                if request_user_badges:
                    soup_badges = BeautifulSoup(request_user_badges.text, 'lxml')
                    div_badges = soup_badges.find('div',
                                                  class_='d-grid g16 grid__4 lg:grid__3 md:grid__2 sm:grid__1 py8')
                    for badge in div_badges.find_all('div', class_='grid--item'):
                        name_badge = badge.find('a').text
                        name_badge = name_badge.replace('\xa0', '')
                        list_badges.append(name_badge)
                else:
                    print(request_user_badges.status_code)
                number_page += 1
            print(f'{user_name}: {user_answers} answers, {user_question} questions \n'
                  f'Badges: {", ".join(list_badges)}.\n')
        else:
            print(request_user.status_code)
else:
    print(request.status_code)'''  # Парсер на аттестацию
'''
import requests
import json

iz = input('Из какой валюты вы хотите перевести: ')
v = input('В какую валюту вы хотите перевести: ')
pairs = iz + v
value = float(input(f'Сколько {iz} у вас есть: '))
response = requests.get('https://currate.ru/api/', params={"get": "rates", "key": input('API-KEY: '), "pairs": pairs})
# API-KEY 17d5ad9e6b9d1023a978257019b16bca

json_obj = json.loads(response.content)
if json_obj['status'] == 200:
    data = json_obj['data']
    print(f'1 {iz} = {data[pairs]} {v}')
    print(f'Вы можете получить {round(float(data[pairs]) * value, ndigits=4)} {v}')
else:
    print(f'ERROR {json_obj["status"]}')
    print(json_obj)'''  # Конвертер валют с API
'''
import requests
import json

url = 'https://codeforces.com/api/user.ratedList?activeOnly=true&includeRetired=false'

response = requests.get(url)
countryes = set(input('Введите страны через пробел: ').split())
number = 1
if response:
    json_obj = json.loads(response.content)
    if json_obj['status'] == 'OK':
        results = json_obj['result']
        for man in results:
            if 'country' in man and man['country'] in countryes:
                print(number, '-', man['handle'], man['rating'], man['country'])
            number += 1
    else:
        print('status not OK')
else:
    print(response.status_code)'''  # API топ стран на Codeforce
'''
def Deg(grad: int):
    res = ''
    if 0 <= grad <= 30 or 330 <= grad <= 360:
        res = 'Северный'
    elif 30 < grad < 60:
        res = 'Северо-Восточный'
    elif 60 <= grad <= 120:
        res = 'Восточный'
    elif 120 <= grad <= 150:
        res = 'Юго-Восточный'
    elif 150 < grad < 210:
        res = "Южный"
    elif 210 <= grad <= 240:
        res = "Юго-Западный"
    elif 240 < grad < 300:
        res = 'Западный'
    elif 300 <= grad < 330:
        res = "Северо-Западный"
    return res

import requests
import json

city = input('Введите город: ')
url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid=eb455c3ca80dc6c8d0078171ff5cab0b"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

if response:
    data_city = json.loads(response.content)
    if len(data_city):
        city = data_city[0]['name']
        lat = data_city[0]['lat']
        lon = data_city[0]['lon']
        weather_ulr = f'https://api.openweathermap.org/data/2.5/weather?lang=ru&lat={lat}&lon={lon}&appid=eb455c3ca80dc6c8d0078171ff5cab0b&units=metric'
        response_weather = requests.get(weather_ulr)
        if response_weather:
            data_weather = json.loads(response_weather.content)
            temp = data_weather['main']['temp']
            wind_speed = data_weather['wind']['speed']
            wind_deg = data_weather['wind']['deg']
            description = data_weather['weather'][0]['description']
            print(f'Температура в г.{city} {temp} градусов Цельсия, ветер {Deg(wind_deg)}, скорость {wind_speed} м/с, {description}')

        else:
            print('Погода не найдена', response_weather.status_code)
    else:
        print('Город не найден', city)
else:
    print('ERROR', response.status_code)

'''  # Прогноз погоды по названию города
'''
import aiohttp
import asyncio
import time

ts = time.time_ns()


async def get_poke(session, url):
    async with session.get(url) as response:
        p = await response.json()
        return f'{p["id"]} - {p["name"]}: {p["height"]}'


async def parse():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{i}'
            tasks.append(asyncio.ensure_future(get_poke(session, url)))

        pokemons = await asyncio.gather(*tasks)
        for p in pokemons:
            print(p)


asyncio.run(parse())

print('Time:', (time.time_ns() - ts) / (10 ** 6), 'ms')'''  # Асинхрон
'''
import json
import matplotlib.pyplot as plt
import requests

url = 'https://codeforces.com/api/user.rating'
handle = input('Хэндл пользователя: ')
response = requests.get(url, params={'handle': handle})
rating = []

if response:
    json_result = json.loads(response.content)
    #print(json_result)
    for contest in json_result['result']:
        rating.append(contest['newRating'])
    plt.plot(rating)
    plt.ylabel('PTS')
    plt.title(f'История рейтинга пользователя под ником {handle}')
    plt.show()
else:
    print('ERROR', response.status_code)'''  # Рейтинг пользователя CodeForce(с диаграммой)
'''

def download_image(title, url):
    with open(f'{title}.jpeg', 'wb') as f:
        f.write(requests.get(url).content)

import requests
data = input('Текст: ')
size = input('Размер QR-кода через "х": ')
url = f'http://api.qrserver.com/v1/create-qr-code/?data={data}&size={size}'

download_image(f'{data},{size}', url)'''  # Генерация QR-кода по заданному тексту и размеру
