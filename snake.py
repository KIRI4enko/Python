'''
    Игра "Змейка"
    Game "Snake"
'''
import tkinter as tk
import random


class MoveRect(tk.Tk):

    def __init__(self, w=1440, h=900, sq_size=60):
        super().__init__()
        self.canvas = tk.Canvas(self, width=w, height=h, bg='#112F11')
        self.btnX = tk.Button(self, text='ВЫЙТИ', command=self.Exit, foreground='red', bg='white')

        self.btnX.pack()
        self.count = 1
        self.Count = tk.Label(self, text=f'СЧЁТ :{self.count}', font='Arial 18', foreground='white', bg='black')
        self.Count.pack()
        self.w = w
        self.h = h
        self.canvas.pack()
        self.coords = []
        self.exit = False
        self.apple = None
        self.sq_size = int(sq_size)
        self.squares = [self.canvas.create_rectangle((i * sq_size, 0),
                                                     ((i - 1) * sq_size, sq_size),
                                                     fill=f'#111F11') for i in range(self.count, 0, -1)
                        ]
        self.vector = (self.sq_size, 0)
        self.bind_all('<Up>', lambda e: self.up())
        self.bind_all('<Down>', lambda e: self.down())
        self.bind_all('<Left>', lambda e: self.left())
        self.bind_all('<Right>', lambda e: self.right())
        self.apple_alive = False
        self.canvas.create_line(0, 0, 0, h, width=3, fill='white')
        self.canvas.create_line(w, 0, w, h, width=3, fill='white')
        self.canvas.create_line(0, h, w, h, width=3, fill='white')
        self.canvas.create_line(0, 0, w, 0, width=3, fill='white')

    def motion(self):
        self.coords = []
        self.die = False

        self.prev_coords = self.canvas.coords(self.squares[-1])

        for i in range(len(self.squares)):

            self.c = list(map(lambda e: e - 1, self.canvas.coords(self.squares[i])[0:2]))
            if self.c in self.coords:
                self.die = True
                break
            else:
                self.coords.append(self.c)
        self.coordhead = self.canvas.coords(self.squares[0])
        if self.coordhead[0] < 0 or self.coordhead[1] < 0 or self.coordhead[
            2] > self.w or self.coordhead[3] > self.h:
            self.die = True

        if not self.die:
            coords_h = self.canvas.coords(self.squares[0])
            self.canvas.move(self.squares[0], *self.vector)

            for i in range(2, len(self.squares) + 1):
                self.canvas.moveto(self.squares[i - 1], *list(self.coords[i - 2]))

            if not self.apple_alive:
                self.squares.append(self.canvas.create_rectangle(self.prev_coords, fill=f'#111F11'))

            self.after(100-self.count, self.motion)
            self.spawn_apple()
            self.eat_apple()

        else:
            self.DIE()
        self.coordhead = self.canvas.coords(self.squares[0])

    def DIE(self):

        self.Die = tk.Tk()
        label = tk.Label(self.Die, text='ВЫ ПРОИГРАЛИ \n '
                                        f'Счёт :{self.count}', foreground='black', font='Arial 32')
        label.pack()
        btnretry = tk.Button(self.Die, text='Сыграть еще раз', command=self.retry, width=20, height=2,
                             font='Arial 18', )
        btnretry.pack()
        btnexit = tk.Button(self.Die, text='Закрыть', command=self.Exit, width=20, height=2, font='Arial 18', )
        btnexit.pack()

    def eat_apple(self):
        if self.apple_alive:
            coords_head = self.canvas.coords(1)
            coords_apple = self.canvas.coords(self.apple)

            eat = True
            for i in range(4):
                if coords_head[i] != coords_apple[i]:
                    eat = False
            if eat:
                self.count += 1
                self.Count['text'] = f'Счёт :{self.count}'
                self.apple_alive = False
                self.canvas.delete(self.apple)

    def spawn_apple(self):
        if not self.apple_alive:
            dw = self.w // self.sq_size - 1
            dh = self.h // self.sq_size - 1

            free = False
            while not free:
                rnd = [random.randint(0, dw), random.randint(0, dh)]
                self.coord_apple = [rnd[0] * self.sq_size,
                                    rnd[1] * self.sq_size,
                                    (rnd[0] + 1) * self.sq_size,
                                    (rnd[1] + 1) * self.sq_size]
                for i in range(len(self.squares)):
                    self.coord = self.canvas.coords(self.squares[i])
                    for j in range(4):
                        if self.coord[j] != self.coord_apple[j]:
                            free = True

            self.apple = self.canvas.create_oval(self.coord_apple, fill='red', width=2)
            self.apple_alive = True

    def up(self):
        if self.vector != (0, self.sq_size):
            self.vector = (0, -self.sq_size)

    def down(self):
        if self.vector != (0, -self.sq_size):
            self.vector = (0, self.sq_size)

    def right(self):
        if self.vector != (-self.sq_size, 0):
            self.vector = (self.sq_size, 0)

    def left(self):
        if self.vector != (self.sq_size, 0):
            self.vector = (-self.sq_size, 0)

    def retry(self):
        moveApp.destroy()
        self.Die.destroy()

    def Exit(self):
        global exit
        exit = True
        self.destroy()
        if self.die:
            self.Die.destroy()


if __name__ == '__main__':
    exit = False
    while not exit:
        moveApp = MoveRect()
        moveApp.motion()
        moveApp.mainloop()
