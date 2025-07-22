import pygame
from game import Game
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():

    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    game = Game()

    while True:
        print("restart")
        game.restart()
        game.start_main_menu()
        if game.exit:
            return
        
        while True:
            game.start_space()
            if game.player.dead:
                break
            if game.exit:
                return
            game.change_player()

            game.start_planet()
            if game.player.dead:
                game.change_player()
                break
            if game.exit:
                return
            game.change_player()
            
if __name__ == "__main__":
    main()