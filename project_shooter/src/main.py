import pygame
from player import *
from Space.space import *
from Planet.planet import *
from main_menu import main_menu
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():

    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    score = 30000
    player = Space_Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:

        score = main_menu(score, player)
        if score == None:
            print("Exit")
            return 
        planets = BST_Map_Node()
        camera = Camera()

        player.revive()
        
        while True:
            print("Going into space...")

            planet = Space(planets, player, camera)
            if player.dead:
                print("dead")
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
                player = player.change_player()
                break

            if not succecc:
                print("Exit")
                return 
            
            print(f"Completed Planet {planet.get_difficulty()}")
            planets.completed_Node(planet)
            player = player.change_player()



if __name__ == "__main__":
    main()