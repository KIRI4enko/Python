''' Cумма блоков 4х4 в матрице 16х16
    The sum of 4x4 blocks in a 16x16 matrix'''


import numpy as np

mass = np.random.randint(1,10,(16,16))
print(mass)
s = np.array([[0]*4]*4)
for i in range(4):
    su = 0
    for j in range(4):
        s[i][j] = np.sum(mass[i * 4:(i + 1) * 4, j:(j + 1) * 4]) - su
        su += s[i][j]
print(s)
