import pygame
from player import *
from Space.space import *
from Planet.planet import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():

    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    score = 0

    while True:

        player = main_menu(score)
        planets = BST_Map_Node()
        camera = Camera()
        
        while True:
            print("Going into space...")

            planet = Space(planets, player, camera)
            if player.dead:
                score += player.score
                break
            if not planet:
                print("Exit")
                return 
            print(f"Going into Planet {planet.get_difficulty()}")
            player = player.change_player()

            succecc = Planet(planet, player)
            if player.dead:
                score += player.score
                break

            if not succecc:
                print("Exit")
                return 
            
            print(f"Completed Planet {planet.get_difficulty()}")
            planets.completed_Node(planet)
            player = player.change_player()



def main_menu(score):
    print('Menu:', score)
    return Space_Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

if __name__ == "__main__":
    main()