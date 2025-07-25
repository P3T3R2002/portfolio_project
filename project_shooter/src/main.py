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
        if game.winner:
            game.player_won()
            if game.exit:
                return
        else:
            game.restart()
            game.start_main_menu()
            if game.exit:
                return
            if game.boss_available:
                game.start_boss()
                game.change_player()
            if game.exit:
                return
            
            while not game.boss_available:
                    game.start_space()
                    if game.boss_available:
                        game.start_boss()
                        game.change_player()
                        break
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