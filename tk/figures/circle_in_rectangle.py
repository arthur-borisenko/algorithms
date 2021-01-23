from random import randint


class CircleInRectangle:
    left_corner_x = None
    left_corner_y = None
    right_corner_x = None
    right_corner_y = None
    color_hex = None
    color_hex_outline = None

    def __init__(self, window_size):
        diameter = randint(0, round(window_size / 5))
        self.left_corner_x = randint(0, window_size)
        self.left_corner_y = randint(0, window_size)
        self.right_corner_x = self.left_corner_x + diameter
        self.right_corner_y = self.left_corner_y + diameter
        self.color_hex = self.rgb_to_hex(randint(0, 255), randint(0, 255), randint(0, 255))
        self.color_hex_outline = self.rgb_to_hex(randint(0, 255), randint(0, 255), randint(0, 255))

    def draw(self, canvas):
        canvas.create_oval(
            self.left_corner_x,
            self.left_corner_y,
            self.right_corner_x,
            self.right_corner_y,
            fill=self.color_hex,
            outline=self.color_hex_outline
        )

    @staticmethod
    def rgb_to_hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
