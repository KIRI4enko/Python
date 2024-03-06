'''
Крестики-нолики
Tic Tac Toe
'''
import tkinter as tk
from functools import partial


class KN(tk.Tk):
    def __init__(self):
        super().__init__()
        self.new_game()
        self.endgame()

    def create_game(self):
        self.buttons = []
        for i in range(3):
            buttons_line = []
            for j in range(3):
                btn = tk.Button(text='', width=3, command=partial(self.HOD, i, j), font='Arial 40')
                buttons_line.append(btn)
                btn.grid(row=i, column=j)
            self.buttons.append(buttons_line)
        self.label_player = tk.Label(self, text='Ходит 1-й  игрок', font='Arial 20')
        self.label_player.grid(columnspan=3, rowspan=2)

    def new_game(self):
        self.choice_player = 0
        self.end_game = False
        self.create_game()

    def retry(self):
        self.end.destroy()
        self.new_game()

    def endgame(self):
        if self.end_game:
            self.end = tk.Tk()
            self.label_player.destroy()
            if not self.tie:
                self.end_label = tk.Label(self.end, text=f'Выиграл {(self.choice_player - 1) % 2 + 1}-й игрок',
                                          font='Arial 30')
            else:
                self.end_label = tk.Label(self.end, text=f'Ничья',
                                          font='Arial 30')
            self.end_label.pack()
            self.btn_replay = tk.Button(self.end, text='Сыграть еще раз', command=self.retry, font='Arial 26')
            self.btn_replay.pack()

    def HOD(self, i, j):
        button = self.buttons[i][j]
        if button['text'] == '':
            if self.choice_player % 2 == 0:
                button['text'] = 'X'
                self.label_player['text'] = 'Ходит 2-й игрок'
            else:
                button['text'] = 'O'
                self.label_player['text'] = 'Ходит 1-й игрок'
        self.choice_player += 1
        self.diags()
        self.rows()
        self.columns()
        self.Tie()
        self.endgame()

    def Tie(self):
        if not self.end_game:
            self.tie = True
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j]['text'] == '':
                        self.tie = False
                        break
                if not self.tie:
                    break
            if self.tie:
                self.end_game = True

    def diags(self):
        main = []
        second = []
        for i in range(3):
            main.append(self.buttons[i][i]['text'])
            second.append(self.buttons[i][-1 - i]['text'])
        if main.count('X') == 3 or main.count('O') == 3 or second.count('X') == 3 or second.count('O') == 3:
            self.end_game = True

    def rows(self):
        for i in range(3):
            prev = self.buttons[i][0]['text']
            end = True
            for j in range(1, 3):
                if self.buttons[i][j]['text'] != prev or self.buttons[i][j]['text'] == '':
                    end = False
                    break
            if end:
                break
        if end:
            self.end_game = True

    def columns(self):
        for i in range(3):
            prev = self.buttons[0][i]['text']
            end = True
            for j in range(1, 3):
                if self.buttons[j][i]['text'] != prev or self.buttons[j][i]['text'] == '':
                    end = False
                    break
            if end:
                break
        if end:
            self.end_game = True


KN().mainloop()
