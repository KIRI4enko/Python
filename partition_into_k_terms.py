''' Разбиение на k невозрастающих слагаемых
Даны натуральные числа n и k (1 <= k <= n).
Выведите всевозможные разбиения числа n на k слагаемых, 
упорядоченных в порядке невозрастания. 
Сами разбиения необходимо выводить в лексикографическом порядке.'''


def partition(n, k, prefix):
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
        p = partition(n, k - 1, next_prefix)
        for a in p:
            if a != None:
                res.append(a)
    return res


def main(n, k):
    for i in partition(n, k, []):
        print(*i, sep=' ')


l = list(map(int, input('Введите число N и число K (в одну строку через пробел): ').split()))

if __name__ == '__main__':
    main(l[0], l[1])

