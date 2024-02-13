''' Функция, которая возвращает квадратную матрицу с числами от 1 до n^2
    Square matrix with numbers from 1 to n^2'''


import numpy

def matrix(n):
    mtrx = numpy.arange(1, n**2 + 1).reshape(n, n)
    return mtrx

if __name__ == '__main__':
    n = int(input('Введите число n: '))
    print(matrix(n))

