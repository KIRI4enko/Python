''' 
Перестановка двух столбцов
Rearranging two columns
'''

import numpy as np


def main():
    size_mtrx = [0]
    while len(size_mtrx) <= 1 or len(size_mtrx) > 2:
        string = input('Введите через запятую размеры двумерного numpy массива: ')
        if string == '':
            print('ОШИБКА!!!')
        else:
            try:
                size_mtrx = list(map(int, string.split(',')))
            except ValueError:
                if len(size_mtrx) <= 1 or len(size_mtrx) > 2:
                    print('ОШИБКА!!!')
    mtrx = np.random.randint(1, 10, size_mtrx)
    print(*mtrx, sep='\n')
    nums = ''
    while nums == '' or max(size_mtrx) < maxim:
        nums = input('Введите через запятую номера двух столбцов, которые необходимо поменять местами: ')
        maxim = max(list(map(int, nums.split(','))))
        if nums != '':
            numbers = list(map(lambda x: int(x) - 1, nums.split(',')))
    for string in mtrx:
        string[numbers[0]], string[numbers[1]] = string[numbers[1]], string[numbers[0]]
    print(*mtrx, sep='\n')


if __name__ == '__main__':
    main()
