'''
    Калькулятор
    Calculator
'''
from tkinter import *
from functools import partial


root = Tk()

first_op = 0
last_op = '+'


def insert(c: str):
    label['text'] += c


def plus():
    global first_op, last_op
    first_op = float(label['text'])
    label['text'] = ''
    last_op = '+'

def clear():
    global first_op,last_op
    label['text'] = ''
    first_op = 0
    last_op = ''


def minus():
    global first_op, last_op
    first_op = float(label['text'])
    label['text'] = ''
    last_op = '-'

def proiz():
    global first_op, last_op
    first_op = float(label['text'])
    label['text'] = ''
    last_op = '*'

def delen():
    global first_op, last_op
    first_op = float(label['text'])
    label['text'] = ''
    last_op = '/'


def eq():
    global first_op, last_op
    try:
        label['text'] = f'{commands[last_op](first_op, float(label["text"]))}'
    except ZeroDivisionError:
        label['text'] = 'ТЫ ЕБЛАН'
        #clear()

commands = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    'C': clear
}
label = Label(root, text='', font='Arial 30')
label.grid(columnspan=5)
btns_text = ['789/', '456*', '123+', '0-=C']
btns = []
for i, line in enumerate(btns_text):
    rowbtns = []
    for j, c in enumerate(line):
        btn = Button(text=str(c), padx=3, pady=3, width=3, font='Arial 25')
        if c.isdigit():
            btn['command'] = partial(insert, c)
        elif c == '=':
            btn['command'] = eq
        elif c == '+':
            btn['command'] = plus
        elif c == 'C':
            btn['command'] = clear
        elif c == '-':
            btn['command'] = minus
        elif c == '*':
            btn['command'] = proiz
        elif c == '/':
            btn['command'] = delen
        btn.grid(row=i + 1, column=j)
        rowbtns.append(btn)
    btns.append(rowbtns)

root.mainloop()
