from GUI import Gui
from Square import Square, Colour

import tkinter
import pygame
import time


def main():
    print("Velocities are in 1000 pixels per second")
    root = tkinter.Tk()
    gui = Gui(root)
    colour = Colour()
    pygame.init()
    e = gui.getRestituition()
    we = gui.getResWall()
    A = Square(colour.red, 30, 30, 100, 100, gui.getA()[0], gui.getA()[1])
    B = Square(colour.blue, 30, 30, 300, 100, gui.getB()[0], gui.getB()[1])
    amountOfCollisions = 0
    justCollided = False

    width = 400
    height = 200
    pygame.display.set_caption("Collision")
    screen = pygame.display.set_mode((width, height))

    gameRunning = True
    while gameRunning == True:  # main loop
        for event in pygame.event.get():  # event handler
            if event.type == pygame.QUIT:
                gameRunning = False

        tic = time.perf_counter()
        # Collision With Walls
        if A.collidesWithWalls(width) == False:
            A.translate(A.velocity * (time.perf_counter() - tic) * 1000, 0)
        else:
            A.velocity = (A.velocity * -1) * we
            print("Velocity A:", A.velocity)
            A.translate(A.velocity * (time.perf_counter() - tic) * 1000, 0)
            amountOfCollisions += 1
        if B.collidesWithWalls(width) == False:
            B.translate(B.velocity * (time.perf_counter() - tic) * 1000, 0)
        else:
            B.velocity = (B.velocity * -1) * we
            print("Velocity B:", B.velocity)
            B.translate(B.velocity * (time.perf_counter() - tic) * 1000, 0)
            amountOfCollisions += 1

        # Object Collision
        if A.x > B.x:
            if A.collidesWithSquare(B) == True:
                # Conservation of momentum calculations for A
                tmp = A.velocity
                A.velocity = ((A.velocity + B.velocity) -
                              (e*(A.velocity - B.velocity))) / 2
                B.velocity = (e*(tmp - B.velocity)) + A.velocity
                print("Velocity A:", A.velocity)
                print("Velocity B:", B.velocity)
                amountOfCollisions += 1
                justCollided = True

        else:
            if B.collidesWithSquare(A) == True:
                # Conservation of momentum calculations for B
                tmp = B.velocity
                B.velocity = ((A.velocity + B.velocity) -
                              (e*(B.velocity - A.velocity))) / 2
                A.velocity = (e*(tmp - A.velocity)) + B.velocity
                print("Velocity A:", A.velocity)
                print("Velocity B:", B.velocity)
                amountOfCollisions += 1
                justCollided = True

        # Case of Coalescence
        if A.velocity == B.velocity or ((A.velocity < 0 and B.velocity < 0) and B.velocity > A.velocity and justCollided == True):
            if A.collidesWithSquare(B) or B.collidesWithSquare(A):
                print("Objects have coalesced")
                gameRunning = False

        if justCollided == 1:
            justCollided = 0

        # Case of infinite speed
        if (A.velocity > 200 or A.velocity < -200) and (B.velocity > 200 or B.velocity < - 200):
            print("Objects have reached max speed of simulation")
            gameRunning = False

        justCollided = False
        screen.fill(colour.black)
        # Render Calls
        pygame.draw.rect(screen, A.colour, pygame.Rect(
            A.x, A.y, A.width, A.height))
        pygame.draw.rect(screen, B.colour, pygame.Rect(
            B.x, B.y, B.width, B.height))
        pygame.display.flip()
    print("There were: ", amountOfCollisions, "collisions")


if __name__ == "__main__":
    main()
