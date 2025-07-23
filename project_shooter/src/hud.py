import pygame
from main_menu import Text
from constants import MAP_HIGHT, MAP_WIDTH

class HudText(Text):
    def __init__(self, x, y, text):
        super().__init__(x, y, text, "hud")
        self.position.x -=  self.text_surface.get_width()

class HudItem:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.visible = True

    def draw(self, screen):
        pass

class Minimap(HudItem):
    def __init__(self, planet):
        super().__init__(0, 0)
        self.planets = []
        self.__add_planet(planet)
    
    def __add_planet(self, planet):
        pos = ((planet.start_pos.x + MAP_WIDTH/2)/100, (planet.start_pos.y + (MAP_HIGHT+200))/100)
        color = None
        if planet.val.get_completion():
            color = 'Green'
        elif planet.available:
            color = 'Blue'
        else:
            color = 'Red'
        self.planets.append((pos, color))
        if planet.left:
            self.__add_planet(planet.left)
        if planet.right:
            self.__add_planet(planet.right)  

    def draw(self, screen):
        for planet in self.planets:
            pygame.draw.circle(screen, planet[1], planet[0], 3)
    
    def update(self, planets):
        self.planets = []
        self.__add_planet(planets)


class Stats(HudItem):
    def __init__(self, player):
        super().__init__(1200, 20)
        self.stats = {}
        self.__add_text(player)
        
    def __add_text(self, player):
        i = 0
        for item in player.get_level().items():
            self.stats[item[0]] = HudText(self.position.x, self.position.y+i*20, f"{item[0]}: lvl {item[1][0]}")
            i += 1
        self.stats["score"] = HudText(self.position.x, self.position.y+i*20, f"current score: {player.score}")

    def update_score(self, value):
        self.stats["score"] = HudText(self.position.x, self.position.y+4*20, f"current score: {value}")
    
    def update(self, player):
        self.__add_text(player)

    def draw(self, screen):
        if self.visible:
            for text in self.stats.values():
                text.draw(screen)

class HUD:
    def __init__(self, player, planet = None):
        self.stats = Stats(player)
        self.minimap = None
        if planet:
            self.minimap = Minimap(planet)

    def update_score(self, value):
        self.stats.update_score(value)

    def update(self, player):
        self.stats.update(player)

    def update_minimap(self, planets):
        self.minimap.update(planets)



            
    def draw(self, screen):
        self.stats.draw(screen)
        if self.minimap:
            self.minimap.draw(screen)