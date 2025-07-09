
import pygame
from constants import*
from Space.space import *
from Planet.planet import *

def main():

    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    planet = Space()
    if planet:
        Planet(planet)




if __name__ == "__main__":
    main()