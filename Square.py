from pygame import Vector2
from math import atan, degrees, tan, radians


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
        if (square.x - (square.width)) < (self.x + (self.width)) and (square.x + (square.width)) > self.x:
            return True
        return False


class SquarePlus(Square):
    def __init__(self, colour, width, height, x, y, velocity, mass, energy):
        super().__init__(colour, width, height, x, y, velocity, mass)
        self.__energy = energy


class Line():  # 2 Vector2 (start and end), width
    def __init__(self, angle, width, height):
        self.__angle = angle
        self.__width = width
        self.__height = height

    def getStartPos(self):
        return Vector2(0, self.__height)

    def getEndPos(self):
        return Vector2(self.__width, (self.__width * tan(self.__angle)) - self.__height)


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
