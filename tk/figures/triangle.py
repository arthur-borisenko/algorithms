from random import randint
from tkinter import *


# from abc import ABCMeta
class Triangle:
    coordinate_x_1 = None
    coordinate_y_3 = None
    coordinate_y_2 = None
    coordinate_y_1 = None
    coordinate_x_2 = None
    coordinate_x_3 = None
    color_hex = None
    color_hex_outline = None

    def __init__(self, window_size):
        self.coordinate_x_1 = randint(10, window_size)
        self.coordinate_x_2 = randint(10, window_size)
        self.coordinate_x_3 = randint(10, window_size)
        self.coordinate_y_1 = randint(1, window_size)
        self.coordinate_y_2 = randint(1, window_size)
        self.coordinate_y_3 = randint(1, window_size)
        self.color_hex = self.rgb_to_hex(randint(0, 255), randint(0, 255), randint(0, 255))
        self.color_hex_outline = self.rgb_to_hex(randint(0, 255), randint(0, 255), randint(0, 255))

    def draw(self, canvas):
        canvas.create_polygon(self.coordinate_x_1,
                              self.coordinate_y_1,
                              self.coordinate_x_2,
                              self.coordinate_y_2,
                              self.coordinate_x_3,
                              self.coordinate_y_3,
                              fill=self.color_hex,
                              outline=self.color_hex_outline)

    @staticmethod
    def rgb_to_hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)