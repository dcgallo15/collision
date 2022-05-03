class Square():
    def __init__(self, colour, width, height, x, y, velocity, mass):
        self.colour = colour
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.velocity = velocity
        self.mass = mass

    def translate(self, x, y):
        self.x += x
        self.y += y

    def collidesWithWalls(self, boundX):
        if self.x <= 0:
            return True
        if (self.x + self.width) >= boundX:
            return True
        return False

    def collidesWithSquare(self, square):
        if self.x > (square.x-square.width):
            return True
        return False


class Colour():
    def __init__(self):
        self.black = [0, 0, 0]
        self.red = [255, 0, 0]
        self.green = [0, 255, 0]
        self.blue = [0, 0, 255]
        self.white = [255, 255, 255]
        self.magenta = [255, 0, 255]
        self.yellow = [255, 255, 0]
        self.cyan = [0, 255, 255]
