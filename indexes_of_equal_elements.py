'''
    Индексы, в которых элементы совпадают.
    indexes where the elements match.
'''
import numpy as np

arr1 = np.random.randint(1,10,(3,3)).flatten()
arr2 = np.random.randint(1,10,(3,3)).flatten()
print(arr1,arr2,sep='\n')
boo = arr1 == arr2
inds = []
for i in range(len(boo)):
    if boo[i]:
        inds.append(i)

if len(inds) == 0:
    print('Нет совпадающих элементов')
else:
    inds = ', '.join(list(map(str,inds)))
    print('Индексы, в которых элементы совпадают: ', inds)
