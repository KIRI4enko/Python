'''
Количество уникальных значений в numpy массиве.
Number of unique values in the numpy array.
'''

import numpy as np

mass = np.random.randint(1, 21, (3, 3))

ms = np.bincount(mass.flatten())

cnt = np.count_nonzero(ms)
