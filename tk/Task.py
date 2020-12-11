from tkinter import *
from random import *
from time import sleep
sleepint=input("entervait")
t = Tk()
sz = 500
c = Canvas(t, width=sz, height=sz)
c.pack()


def rgb_to_hex(r, g, b):
    init = (r, g, b)
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def loop(color):
    d = randint(0, round(sz / 5))
    x0 = randint(0, sz)
    y0 = randint(0, sz)
    x1 = x0 + d
    y1 = y0 + d
    c.create_oval(x0, y0, x1, y1, fill=color)
    t.update()
    sleep(float(sleepint)/10)

while True:
    print(rgb_to_hex(randint(0, 255), randint(0, 255), randint(0, 255)))
    loop(rgb_to_hex(randint(0, 255), randint(0, 255), randint(0, 255)))
