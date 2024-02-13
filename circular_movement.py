'''
Движение по окружности по заданному углу(значения записываются в файл)
Circular movement at a given angle (values are written to a file)
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

