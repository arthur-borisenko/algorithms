import math
import threading
import turtle
from threading import Lock
from time import sleep

mutex = Lock()
from logging import *
basicConfig(filename='log.log',level=DEBUG)
meterToPixel = 40000
m = 3
Fx = 0
Fy = -9.8 * m
x = x0 = 0
y = y0 = 0
Vy = Vy0 = 0
Vx0 = Vx = 0.05
t = 0
dt = 0.0004
bombs = []
bomb_power = 0.5


def bax(x, y):
    mutex.acquire()
    try:
        bombs.append((x, y))
    finally:
        mutex.release()

        bomb = turtle.Turtle(shape="circle", visible=False)
        bomb.penup()
        bomb.setposition(x, y)
        bomb.pendown()
        bomb.showturtle()
        sleep(0.1)  # fortodo>>move clean to separate thread
        bomb.hideturtle()
        print("on click ", threading.current_thread().ident, x, y)
        pass


turtle.onscreenclick(bax, btn=1, add=None)
institute = turtle.Turtle(shape="turtle", visible=False)
institute.penup()
institute.setposition(x * meterToPixel, y * meterToPixel)
institute.pendown()
institute.showturtle()

school = turtle.Turtle(shape="turtle", visible=False)
school.penup()
school.setposition(x * meterToPixel, y * meterToPixel)
school.pendown()
school.showturtle()
while 1 < 2:
    mutex.acquire()
    try:
        for i in range(len(bombs)):
            (bomb_x, bomb_y) = bombs.pop()
            print("on tick ", threading.current_thread().ident, bomb_x, bomb_y)
            pril_cat = x - bomb_x
            prot_cat = y - bomb_y
            gipot = math.sqrt(pril_cat ** 2 + prot_cat ** 2)
            cos_a = pril_cat / gipot
            sin_a = prot_cat / gipot

            Vx += bomb_power * cos_a
            Vy += bomb_power * sin_a
            info('coss square:'+str(cos_a**2+sin_a**2))
    finally:
        mutex.release()

        dVx = (Fx / m) * dt
        dVy = (Fy / m) * dt

        Vx = Vx + dVx
        Vy = Vy + dVy

        x = x + Vx * dt
        y = y + Vy * dt
        institute.setposition(x * meterToPixel, y * meterToPixel)

        t = t + dt
        x_ = (Fx / m * (t ** 2) / 2 + Vx0 * t + x0) * meterToPixel
        y_ = (Fy / m * (t ** 2) / 2 + Vy0 * t + y0) * meterToPixel
        school.setposition(x_, y_)

        sleep(dt)
