'''
    Paint
    R -> [+,.,.]
    Shift-R -> [-,.,.]
    G -> [.,+,.]
    Shift-G -> [.,-,.]
    B -> [.,.,+]
    Shift-B -> [.,.,-]
    MouseWheel -> change width
'''
from tkinter import *


class PaintApp:
    def __init__(self, root: Tk):
        self.root = root
        self.canvas: Canvas = Canvas(self.root, width=800, height=600)
        self.width = 1
        self.canvas.pack()
        self.is_draw = False
        self.prev_x = None
        self.prev_y = None
        self.red = 0
        self.green = 0
        self.blue = 0
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.canvas.bind('<MouseWheel>', self.up_width)
        self.canvas.bind_all('<Shift-MouseWheel>', self.down_width)
        self.canvas.bind_all('r', self.up_red)
        self.canvas.bind_all('<Shift-R>', self.down_red)
        self.canvas.bind_all('g', self.up_green)
        self.canvas.bind_all('<Shift-G>', self.down_green)
        self.canvas.bind_all('b', self.up_blue)
        self.canvas.bind_all('<Shift-B>', self.down_blue)
        self.fill = f'#{hex(self.red )[2:]}{hex(self.green)[2:]}{hex(self.blue)[2:]}'

    def up_red(self, event):
        if self.red <= 14:
            self.red += 1

    def down_red(self, event):
        if self.red >= 2:
            self.red -= 1

    def up_green(self, event):
        if self.green <= 14:
            self.green += 1

    def down_green(self, event):
        if self.green >= 2:
            self.green -= 1

    def up_blue(self, event):
        if self.blue <= 14:
            self.blue += 1

    def down_blue(self, event):
        if self.blue >= 2:
            self.blue -= 1

    def up_width(self, event):
        self.width += 1
        print(self.width)

    def down_width(self, event):
        if self.width >= 2:
            self.width -= 2
            print('Толщина = ', self.width)

    def draw(self, event):
        if self.is_draw:
            self.fill = f'#{hex(self.red)[2:]}{hex(self.green)[2:]}{hex(self.blue)[2:]}'
            if self.prev_x and self.prev_y:
                self.canvas.create_line(self.prev_x, self.prev_y, event.x, event.y, width=self.width, fill=self.fill)
        self.prev_x = event.x
        self.prev_y = event.y

    def start_draw(self, event):
        self.is_draw = True

    def reset(self, event):
        self.is_draw = False
        self.prev_x = None
        self.prev_y = None


root = Tk()
paint_app = PaintApp(root)
root.mainloop()

