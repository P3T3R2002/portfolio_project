import pygame
from constants import SCREEN_WIDTH, MENU_CONSTANTS, PLAYER_CONSTANTS

def main_menu(score, player):
    
    game_time = pygame.time.Clock()
    draw(player, score)

    while True:
        if pygame.mouse.get_pressed(num_buttons=5)[0]:
            for item in player.get_level().items():
                center = pygame.Vector2(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"][item[0]])
                center += pygame.Vector2(MENU_CONSTANTS['plus']['relative_pos'])
                if item[1][0] != item[1][1] and click_inside(pygame.Vector2(pygame.mouse.get_pos()), center, MENU_CONSTANTS['plus']['radius']):
                    if item[1][0] != item[1][1]:
                        score = buy_upgrade(score, item, player)
                        draw(player, score)
                        pygame.time.wait(200)
            if click_inside(pygame.Vector2(pygame.mouse.get_pos()), pygame.Vector2(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"]["play"]), MENU_CONSTANTS['font_size']['play']):
                return score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            
        pygame.display.flip()
        game_time.tick(60)

def click_inside(click_pos, button_pos, r):
    distance = click_pos.distance_to(button_pos)
    return distance < r

def buy_upgrade(score, item, player):
    if PLAYER_CONSTANTS['price'][item[0]][item[1][0]-1] <= score:
        player.level_up(item[0])
        return score - PLAYER_CONSTANTS['price'][item[0]][item[1][0]-1]
    return score

def draw(player, score):
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont('arial', MENU_CONSTANTS['font_size']['level_up'])
    
    screen.fill('black')
    for item in player.get_level().items():
        text_surface = font.render(f"{item[0]}: lvl {item[1]}", True, (255, 255, 255))
        screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width(), MENU_CONSTANTS["position_Y"][item[0]]))
        if item[1][0] != item[1][1]:
            draw_plus(screen, item)
            text_surface = font.render(f"{PLAYER_CONSTANTS['price'][item[0]][item[1][0]-1]}", True, (255, 255, 255))
            screen.blit(text_surface, (SCREEN_WIDTH/2 + MENU_CONSTANTS["position_Y"]['relative_price'], MENU_CONSTANTS["position_Y"][item[0]]))


    text_surface = font.render(f"current score: {score}", True, (255, 255, 255))
    screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width(), MENU_CONSTANTS["position_Y"]["score"]))

    font = pygame.font.SysFont('arial', MENU_CONSTANTS['font_size']['play'])
    text_surface = font.render(f"PLAY", True, (255, 255, 255))
    screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, MENU_CONSTANTS["position_Y"]["play"]))

    pygame.display.flip()
    return

def draw_plus(screen, item):
    center = pygame.Vector2(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"][item[0]])
    center += pygame.Vector2(MENU_CONSTANTS['plus']['relative_pos'])
    radius = MENU_CONSTANTS['plus']['radius']
    pygame.draw.circle(screen, 'BLUE', center, radius)
    pygame.draw.line(screen, 'WHITE', (center[0], center[1] - radius), (center[0], center[1] + radius), 5)
    pygame.draw.line(screen, 'WHITE', (center[0] - radius, center[1]), (center[0] + radius, center[1]), 5)
