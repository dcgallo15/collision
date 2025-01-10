# NOTE: THIS IS A TESTING PROGRAM FOR THE COLLISIONS

import time
import pygame
from Square import Square, Colour


def main():
    colour = Colour()
    pygame.init()
    A = Square(colour.red, 30, 30, 100, 100, int(input("Enter Va: ")), 1)
    B = Square(colour.blue, 30, 30, 200, 100, int(input("Enter Vb: ")), 1)

    gameRunning = True
    width = 320
    height = 240
    pygame.display.set_caption("Collision")
    screen = pygame.display.set_mode((width, height))
    while gameRunning == True:
        tic = time.perf_counter()

        # Wall Collision
        if A.collidesWithWalls(width) == False:
            A.translate(A.velocity * (time.perf_counter() - tic) * 1000, 0)
        else:
            A.velocity = (A.velocity * -1)
            print("New A:", A.velocity)
            A.translate(A.velocity * (time.perf_counter() - tic) * 1000, 0)

        if B.collidesWithWalls(width) == False:
            B.translate(B.velocity * (time.perf_counter() - tic) * 1000, 0)
        else:
            B.velocity = (B.velocity * -1)
            print("New B:", B.velocity)
            B.translate(B.velocity * (time.perf_counter() - tic) * 1000, 0)

        # Object Collision
        if A.x < B.x:
            if B.collidesWithSquare(A) == True:
                print("Collision B")
        else:
            if A.collidesWithSquare(B) == True:
                print("Collision A")

        screen.fill(colour.black)
        # Render Calls
        pygame.draw.rect(screen, A.colour, pygame.Rect(
            A.x, A.y, A.width, A.height))
        pygame.draw.rect(screen, B.colour, pygame.Rect(
            B.x, B.y, B.width, B.height))
        pygame.display.flip()


if __name__ == "__main__":
    main()
