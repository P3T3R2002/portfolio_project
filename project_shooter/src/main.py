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
    player = Space_Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    camera = Camera()
    while True:
        print("Going into space...")

        planet = Space(planets, player, camera)
        if not planet:
            print("Exit")
            return 
        print(f"Going into Planet {planet.get_difficulty()}")
        player = player.change_player()
        if not Planet(planet, player):
            print("Exit")
            return 
        
        print(f"Completed Planet {planet.get_difficulty()}")
        planets.completed_Node(planet)
        player = player.change_player()





if __name__ == "__main__":
    main()