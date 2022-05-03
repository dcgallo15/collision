from GUI import Gui
from Square import Square, Colour

import tkinter
import pygame
from sys import exit
import time


def main():
    root = tkinter.Tk()
    gui = Gui(root)
    colour = Colour()
    pygame.init()
    e = gui.getRestituition()
    A = Square(colour.red, 30, 30, 100, 100, gui.getA()[0], gui.getA()[1])
    B = Square(colour.blue, 30, 30, 200, 100, gui.getB()[0], gui.getB()[1])

    width = 320
    height = 240
    pygame.display.set_caption("Collision")
    screen = pygame.display.set_mode((width, height))
    gameRunning = True
    while gameRunning == True:
        tic = time.perf_counter()
        for event in pygame.event.get():  # event handler
            if event.type == pygame.QUIT:
                exit(240)

        # moves the squares
        if A.collidesWithWalls(width) == False:
            A.translate(A.velocity * (time.perf_counter() - tic) * 1000, 0)
        if B.collidesWithWalls(width) == False:
            B.translate(B.velocity * (time.perf_counter() - tic) * 1000, 0)

        if A.collidesWithSquare(B) == True:
            tmp = A.velocity
            A.velocity = (A.velocity + B.velocity) - \
                (e*(A.velocity - B.velocity))
            B.velocity = (e*(tmp - B.velocity)) + A.velocity
            print("New A:", A.velocity)
            print("New B:", B.velocity)

        screen.fill(colour.black)
        # Render Calls
        pygame.draw.rect(screen, A.colour, pygame.Rect(
            A.x, A.y, A.width, A.height))
        pygame.draw.rect(screen, B.colour, pygame.Rect(
            B.x, B.y, B.width, B.height))
        pygame.display.flip()


if __name__ == "__main__":
    main()
