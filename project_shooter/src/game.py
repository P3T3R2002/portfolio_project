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
        self.planet = None
        self.exit = False
        self.boss_available = True

    def restart(self):
        self.planets = BST_Map_Node()
        self.camera = Camera()
        self.player.revive()
        self.hud.update_minimap(self.planets)
        self.hud.update_score(self.score)
        self.hud.reset_sceen()
        self.main_menu.player = self.player

    def start_main_menu(self):
        self.score = self.main_menu.main_menu(self.score, self.player)
        if self.score == None:
            self.exit = True

    def start_boss(self):
        self.player = self.player.change_to_boss()
        self.boss.start_boss(self.player, self.hud)

    def change_player(self):
        self.player = self.player.change_player()

    def start_space(self):
        self.planet = Space(self.planets, self.player, self.camera, self.hud)
        self.boss_available = self.player.boss_available
        if not self.planet:
            self.exit = True
        self.score += self.player.score
        self.hud.change_sceen()

    def start_planet(self):
        self.planet = Planet(self.planet, self.player, self.hud)
        self.hud.change_sceen()
        if not self.planet:
            self.exit = True
        if self.player.dead:
            return 
        self.planets.completed_Node(self.planet)
        self.hud.update_minimap(self.planets)
        self.planet = None
