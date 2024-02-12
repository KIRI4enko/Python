''' Разбиение на неубывающие слагаемые
Дано натуральное число n. 
Выведите всевозможные его разбиения на слагаемые, упорядоченные в порядке неубывания. 
Сами разбиения необходимо выводить в лексикографическом порядке.'''


def partition(n, prefix):
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
            p = partition(n, next_prefix)
            for a in p:
                if a is not None:
                    res.append(a)
        return res


n = int(input('Введите число: '))


def main(n):
    for i in partition(n, []):
        print(*i, sep=' ')


if __name__ == '__main__':
    main(n)

