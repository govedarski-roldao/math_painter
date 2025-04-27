import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def make(self):
        pass


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        pass


class Square:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, canvas):
        pass
