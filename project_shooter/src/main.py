
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


    planets = BST_Map_Node()
    while True:

        planet = Space(planets)
        if not planet:
            return 
        if not Planet(planet):
            return 
        planets.completed_Node(planet)





if __name__ == "__main__":
    main()