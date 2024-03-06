'''
    Перевод температуры из градусов Цельсия в градусы Фаренгейта и наоборот
    Converting temperature from degrees Celsius to degrees Fahrenheit and vice versa
'''
from tkinter import *
import re

root = Tk()
root.geometry('600x400')


def change_mode():
    if btnmode['text'] == 'Из градусов Цельсия в Фаренгейты':
        btnmode['text'] = 'Из градусов Фаренгейта в Цельсия'
        lbl2['text'] = lbl2['text'].replace('Цельсиях', 'Фаренгейтах')
    else:
        btnmode['text'] = 'Из градусов Цельсия в Фаренгейты'
        lbl2['text'] = lbl2['text'].replace('Фаренгейтах', 'Цельсиях')


label = Label(root, text='Калькулятор температуры \n', font='Arial 20')
lbl2 = Label(root, text='Введите температуру в Цельсиях', font='Arial 18')
btnmode = Button(root, text='Из градусов Цельсия в Фаренгейты', command=change_mode, font='Arial 20')


def is_valid(new: str):
    res = re.match(r"(\+|\-)?\d+(\.\d+)?$", new)
    return res is not None


def answer():
    ans['text'] = 'Ответ :'
    num = ent.get()
    if num != '':
        num = float(num)
        if btnmode['text'] == 'Из градусов Цельсия в Фаренгейты':
            ans['text'] += str(round(num * 9 / 5 + 32, 3))
        else:
            ans['text'] += str(round((num - 32) * 5 / 9, 3))


ent = Entry(root, validate="key", validatecommand=(root.register(is_valid), "%P"))
btnans = Button(root, text='Найти', command=answer)
ans = Label(root, font='Arial 25', text='Ответ: ')

label.pack()
btnmode.pack()
lbl2.pack()
ent.pack()
btnans.pack()
ans.pack()

root.mainloop()
