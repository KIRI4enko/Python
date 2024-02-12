'''Перестановки с заданным числом повторов
Написать функцию, возвращающую все последовательности на основе представленного алфавита,
в которых элементы повторяются не более K раз.
На вход подаётся алфавит (строка уникальных символов) и число K.'''


def permutations(az, prefix, n, k):  # az - alphabet, n - length, k - replacement
    if n == 0:
        return [prefix]
    res = []
    for i in az:
        next_prefix = prefix + [i]
        next_az = ''
        for a in az:
            if next_prefix.count(a) < k:
                next_az += a
        p = permutations(next_az, next_prefix, n - 1, k)
        for perm in p:
            res.append(perm)
    return res


def main(az, k):
    for i in permutations(az, [], len(az), k):
        print(''.join(i))


string = input('Введите алфавит с уникальными символами: ')
count = int(input('Введите число K: '))
if __name__ == '__main__':
    main(string, count)

