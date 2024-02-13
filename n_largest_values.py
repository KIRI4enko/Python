''' n наибольших значений массива
    n largest array values'''

import numpy as np

n = int(input())
n1 = n
mtrx = np.random.randint(1, 100, (5, 5))
mtrx_flat = np.bincount(mtrx.flatten())
maxim = []
len_flat = len(mtrx_flat) - 1
i = 0
while n > 0:
    if mtrx_flat[-1 - i] != 0:
        maxim.append(len_flat - i)
        n -= 1
    i += 1

print(f'{n1} наибольших значения: ', *maxim)
