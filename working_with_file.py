'''
Работа с файлом и ОС
Если файл существует, в файл записывается информация
Если нет, то файл создается и записывается информация
Working with file and OS
'''
import os

file_name = input('Имя файла: ')
if os.path.exists(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        for string in file:
            print(string, end='')
else:
    with open(file_name, mode='w', encoding='utf-8') as file:
        string = ' '
        while string != '':
            string = input('Введите данные: ')
            file.write(string + '\n')

