import turtle
from time import sleep

meterToPixel = 1000
m = 3
Fx = 0
Fy = -9.8 * m
x = x0 = 0
y = y0 = 0
Vx = 0.5
Vy = 0
Vy0 = 0
Vx0 = 0.5
t = 0
dt = 0.0004

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
