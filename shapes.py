from canvas import color_map


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
