import random
import numpy as np
from PIL import Image

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
    "orange": (255, 165, 0),
    "pink": (255, 192, 203),
    "brown": (165, 42, 42),
    "gray": (169, 169, 169),
    "lime": (0, 255, 0),
    "indigo": (75, 0, 130),
    "violet": (238, 130, 238),
    "teal": (0, 128, 128),
    "gold": (255, 215, 0),
    "silver": (192, 192, 192),
    "beige": (245, 245, 220),
    "peach": (255, 218, 185),
    "mint": (189, 252, 201)
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
