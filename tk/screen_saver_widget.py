from tkinter import *
from tk.circle_in_rectangle import CircleInRectangle
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
            oval = CircleInRectangle(self.window_size)
            self.canvas.create_oval(
                oval.left_corner_x,
                oval.left_corner_y,
                oval.right_corner_x,
                oval.right_corner_y,
                fill=oval.color_hex
            )
            self.mainWindow.update()
            sleep(float(self.sleep_interval) / 10)
