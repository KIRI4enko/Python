'''
    Счётчик количества нажатий на кнопку
    Button press counter
'''
from tkinter import *


class App(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = 'Tk',
                 useTk: bool = True, sync: bool = False, use: str | None = None):
        super().__init__(screenName=screenName, baseName=baseName, className=className, useTk=useTk, sync=sync, use=use)
        self.geometry = ('250x250')
        self.btn = Button(text='Нажми', command=self.click_button, bg='gray')
        self.btn.pack()
        self.clicks = 0

    def click_button(self):
        self.clicks += 1
        self.btn['text'] = f'Нажатий: {self.clicks}'


App().mainloop()
