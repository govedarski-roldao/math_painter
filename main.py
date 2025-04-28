import numpy as np
from PIL import Image
import random


class Canvas:
    def __init__(self, a, b, color, format):
        self.a = a
        self.b = b
        self.color = color.lower()
        self.image_number = random.randint(100, 200)
        self.format = format.lower()
        self.color_map = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            "purple": (128, 0, 128),
            "cyan": (0, 255, 255),
            "magenta": (255, 0, 255),
        }
        self.data = np.zeros((self.a, self.b, 3), dtype=np.uint8)
        self.rgb = self.color_map.get(self.color, (255, 255, 255))
        self.data[:] = self.rgb

    def make(self):
        img = Image.fromarray(self.data, 'RGB')
        img.save(f"canvas{self.image_number}.{self.format}")


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, canvas):
        pass
