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
    player = Space_Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:

        if not main_menu(score, player):
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



def main_menu(score, player):
    
    dt = 0
    game_time = pygame.time.Clock()
    Start = draw(player, score)

    while True:
        if pygame.mouse.get_pressed(num_buttons=5)[0]:
            i = 1
            for item in player.get_level().items():
                if item[1][0] != item[1][1] and click_inside(pygame.Vector2(pygame.mouse.get_pos()), pygame.Vector2(SCREEN_WIDTH/2+50, 220+i*40), 15):
                    player.level_up(item[0])
                    Start = draw(player, score)
                    pygame.time.wait(200)
                i += 1
            if click_inside(pygame.Vector2(pygame.mouse.get_pos()), Start, 60):
                return True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            
        pygame.display.flip()
        dt = game_time.tick(60)/1000

def click_inside(click_pos, button_pos, r):
    distance = click_pos.distance_to(button_pos)
    return distance < r

def draw(player, score):
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont('arial', 36)
    
    i = 1
    screen.fill('black')
    for item in player.get_level().items():
        text_surface = font.render(f"{item[0]}: lvl {item[1]}", True, (255, 255, 255))
        screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width(), 200+i*40))
        i += 1
        if item[1][0] != item[1][1]:
            draw_plus(screen, (SCREEN_WIDTH/2+50, 180+i*40))

    text_surface = font.render(f"current score: {score}", True, (255, 255, 255))
    screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width(), 200+i*40))

    i += 1
    font = pygame.font.SysFont('arial', 60)
    text_surface = font.render(f"PLAY", True, (255, 255, 255))
    screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, 200+i*40+100))

    pygame.display.flip()
    return pygame.Vector2(SCREEN_WIDTH/2, 200+i*40+100 + text_surface.get_height()/2)

def draw_plus(screen, center):
    pygame.draw.circle(screen, 'BLUE', center, 15)
    pygame.draw.line(screen, 'WHITE', (center[0], center[1] - 15), (center[0], center[1] + 15), 5)
    pygame.draw.line(screen, 'WHITE', (center[0] - 15, center[1]), (center[0] + 15, center[1]), 5)

if __name__ == "__main__":
    main()