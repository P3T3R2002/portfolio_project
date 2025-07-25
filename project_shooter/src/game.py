from hud import HUD
from player import *
from camera import *
from main_menu import *
from boss.boss import *
from Space.space import *
from Planet.planet import *
from Space.game_map import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    def __init__(self):
        self.score = 30000
        self.planets = BST_Map_Node()
        self.player = Space_Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.hud = HUD(self.player, self.planets)
        self.main_menu = MainMenu(self.score, self.player)
        self.camera = Camera()
        self.boss = Boss()
        self.winner = False
        self.planet = None
        self.exit = False
        self.boss_available = False

    def restart(self):
        self.planets = BST_Map_Node()
        self.camera = Camera()
        self.boss = Boss()
        self.score += self.player.score
        self.player.revive()
        self.hud.update_minimap(self.planets)
        self.hud.update_score(self.score)
        self.hud.reset_sceen()
        self.main_menu.player = self.player

    def start_main_menu(self):
        self.score = self.main_menu.main_menu(self.score, self.player)
        if self.score == None:
            self.exit = True

    def change_player(self):
        self.player = self.player.change_player()

    def start_boss(self):
        self.hud.boss_hud()
        self.hud.fight.set_max_score(500)
        self.player = self.player.change_to_boss()
        exit = self.boss.start_boss(self.player, self.hud)
        self.winner = self.player.winner
        if not exit:
            self.exit = True

    def start_space(self):
        self.planet = Space(self.planets, self.player, self.camera, self.hud)
        self.boss_available = self.player.boss_available
        if not self.planet:
            self.exit = True
        self.hud.change_sceen()

    def start_planet(self):
        self.hud.fight.set_max_score(50 * 2 ** (self.planet.difficulty-1))
        self.planet = go_Planet(self.planet, self.player, self.hud)
        self.hud.change_sceen()
        if not self.planet:
            self.exit = True
        if self.player.dead:
            return 
        self.planets.completed_Node(self.planet)
        self.hud.update_minimap(self.planets)
        self.planet = None

    def player_won(self):
        screen = pygame.display.get_surface()
        game_time = pygame.time.Clock()
        while True:
            screen.fill('black')
            text = ButtonText(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "YOU WON!!")
            text.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                    return None
                
            pygame.display.flip()
            game_time.tick(60)/1000