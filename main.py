import numpy as np
from PIL import Image
import random

color_map = {
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

class Canvas:
    def __init__(self, height, width, color, format):
        self.height = height
        self.width = width
        self.color = color.lower()
        self.image_number = random.randint(100, 200)
        self.format = format.lower()
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.rgb = color_map.get(self.color, (255, 255, 255))
        self.data[:] = self.rgb

    def make(self):
        img = Image.fromarray(self.data, 'RGB')
        img.save(f"./images/canvas{self.image_number}.{self.format}")


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.color = color.lower()
        self.rgb = color_map.get(self.color, (255, 255, 255))
        self.width = width
        self.height = height

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.height, self.y: self.y + self.width] = self.rgb


class Square:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color.lower()
        self.rgb = color_map.get(self.color, (255, 255, 255))


    def draw(self, canvas):
        canvas.data[self.x:self.x + self.size, self.y: self.y + self.size] = self.rgb


canvas = Canvas(height=100, width=130, color="purple", format="jpg")
r1 = Rectangle(x=10, y=20, color="yellow", width=10, height=2)
r1.draw(canvas)
s1 = Square(5, 7, 20, "blue")
s1.draw(canvas)
canvas.make()