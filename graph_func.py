'''
    График функции 1/x
    Graph of function 1/x
'''
import tkinter as tk


def draw_circle(c: tk.Canvas, x, y, r, width=3, color='black'):
    c.create_oval(x - r, y - r, x + r, y + r, width=width, outline=color)


root = tk.Tk()

canvas = tk.Canvas(width=1200, height=1000)

canvas.create_line(100, 600, 1100, 600, arrow='last', width=1)
canvas.create_line(600, 1100, 600, 100, arrow='last', width=5)


def f(x):
    if x != 0:
        return 6666 / x
    return 100000000000000


for x in range(-500, 500):
    y = -f(x)
    x_next = x + 1
    y_next = -f(x_next)
    canvas.create_line(x+600, y+600, x_next+600, y_next+600, width=3)

canvas.pack()
root.mainloop()
