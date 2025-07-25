import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH, MENU_CONSTANTS, PLAYER_CONSTANTS

class Plus(CircleShape):
    def __init__(self, item):
        super().__init__(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"][item[0]], MENU_CONSTANTS['plus']['radius'], MENU_CONSTANTS['plus']['source'])
        self.position +=  MENU_CONSTANTS["position_Y"]['relative_pos']
        self.image_rect.center = self.position
        self.text = item[0]
        self.visible = True

    def click_inside(self, click_pos):
        distance = click_pos.distance_to(self.position)
        return distance < self.radius

class Text:
    def __init__(self, x, y, text, font):
        self.font = pygame.font.SysFont('arial', MENU_CONSTANTS['font_size'][font])
        self.text_surface = self.font.render(text, True, (255, 255, 255))
        self.position = pygame.Vector2(x, y)
        
    def draw(self, screen):
        screen.blit(self.text_surface, (self.position.x, self.position.y))


class PriceText(Text):
    def __init__(self, x, y, text):
        super().__init__(x, y, text, "level_up")
        self.position.x += MENU_CONSTANTS["position_Y"]['relative_price']

class UpgradeInfoText(Text):
    def __init__(self, x, y, text):
        super().__init__(x, y, text, "level_up")
        self.position.x -= self.text_surface.get_width()

class ButtonText(Text):
    def __init__(self, x, y, text):
        super().__init__(x, y, text, "button")
        self.position.x -= self.text_surface.get_width()/2

class MainMenu:
    def __init__(self, score, player):
            self.score = score
            self.player = player
            self.texts = {}
            self.plus = []
            self.__add_text()
            self.__add_plus()

    def __add_text(self):
        for item in self.player.get_level().items():
            row = []
            row.append(UpgradeInfoText(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"][item[0]], f"{item[0]}: lvl {item[1]}"))
            if item[1][0] != item[1][1]:
                row.append(PriceText(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"][item[0]], f"{PLAYER_CONSTANTS['price'][item[0]][item[1][0]-1]}"))
            self.texts[item[0]] = row

        self.texts['score'] = [UpgradeInfoText(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"]['score'], f"current score: {self.score}")]

        self.texts['button'] = [
            ButtonText(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"]["exit"], "EXIT"),
            ButtonText(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"]["play"], "PLAY")
        ]


    def __add_plus(self):
        for item in self.player.get_level().items():

            if item[1][0] != item[1][1]:
                self.plus.append(Plus(item))

    def __update_texts(self, text):
        item = self.player.get_level()[text]
        row = []
        row.append(UpgradeInfoText(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"][text], f"{text}: lvl {item}"))
        if item[0] != item[1]:
            row.append(PriceText(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"][text], f"{PLAYER_CONSTANTS['price'][text][item[0]-1]}"))
        self.texts[text] = row
        self.texts['score'] = [UpgradeInfoText(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"]['score'], f"current score: {self.score}")]

    def buy_upgrade(self, plus):
        text = plus.text
        item = self.player.get_level()[text]
        if item[0] == item[1]:
            return
        if PLAYER_CONSTANTS['price'][text][item[0]-1] <= self.score:
            self.player.level_up(text)
            self.score -= PLAYER_CONSTANTS['price'][text][item[0]-1]
            self.__update_texts(text)
        item = self.player.get_level()[text]
        if item[0] == item[1]:
            plus.visible = False

    def draw(self, screen):
        screen.fill('black')
        for item in self.texts.values():
            for text in item:
                text.draw(screen)

        for plus in self.plus:
            if plus.visible:
                plus.draw(screen)

        pygame.display.flip()
        return

    def main_menu(self, score, player):
            screen = pygame.display.get_surface()
            game_time = pygame.time.Clock()

            menu = MainMenu(score, player)
            menu.draw(screen)

            while True:
                if pygame.mouse.get_pressed(num_buttons=5)[0]:
                    for plus in menu.plus:
                        if plus.click_inside(pygame.Vector2(pygame.mouse.get_pos())):
                            menu.buy_upgrade(plus)
                            menu.draw(screen)
                            pygame.time.wait(200)
                    if click_inside_play(pygame.Vector2(pygame.mouse.get_pos())):
                        return menu.score
                    if click_inside_exit(pygame.Vector2(pygame.mouse.get_pos())):
                        return None

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return None
                    
                pygame.display.flip()
                game_time.tick(60)


def click_inside_play(click_pos):
    distance = click_pos.distance_to(pygame.Vector2(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"]["play"]+MENU_CONSTANTS['font_size']['button']/2))
    return distance < MENU_CONSTANTS['font_size']['button']
def click_inside_exit(click_pos):
    distance = click_pos.distance_to(pygame.Vector2(SCREEN_WIDTH/2, MENU_CONSTANTS["position_Y"]["exit"]+MENU_CONSTANTS['font_size']['button']/2))
    return distance < MENU_CONSTANTS['font_size']['button']