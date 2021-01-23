from tkinter import *
from tk.figures.circle_in_rectangle import CircleInRectangle
from tk.figures.rectangle import Rectangle
from tk.figures.triangle import Triangle
from time import sleep


class ScreenSaverWidget:
    mainWindow = None
    canvas = None
    window_size = None
    sleep_interval = None

    def __init__(self, window_size, sleep_interval):
        self.window_size = window_size
        self.sleep_interval = sleep_interval
        self.mainWindow = Tk()
        self.canvas = Canvas(self.mainWindow, width=window_size, height=window_size)
        self.canvas.pack()

    def start(self):
        while True:
            CircleInRectangle(self.window_size).draw(self.canvas)
            Rectangle(self.window_size).draw(self.canvas)
            Triangle(self.window_size).draw(self.canvas)


            self.mainWindow.update()
            sleep(float(self.sleep_interval) / 10)
