import pygame
# Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Map
MAP_WIDTH = 20000
MAP_HIGHT = 10000

# menu
MENU_CONSTANTS = {  'position_Y': { 'rate_of_fire': 200+1*40,       #
                                    'projectile_num': 200+2*40,     #
                                    'ship_speed': 200+3*40,         # font size 36->40   
                                    'directions': 200+4*40,         #
                                    'score': 200+5*40,              #
                                    'play': 540,
                                    'exit': 650,
                                    'relative_pos': (50, 20),
                                    'relative_price': 100
                                },
                    'plus': {'radius': 15,
                             'source': pygame.transform.scale(pygame.image.load("src/assets/plus.png"), (15*2, 15*2))
                             },
                    'font_size': {'level_up': 36,
                                  'button': 60,
                                  'hud': 16
                                  },
                    'hud_pos_Y': {'rate_of_fire': 1*20,       #
                                    'projectile_num': 2*20,     #
                                    'ship_speed': 3*20,         # font size 16->20   
                                    'directions': 4*20,         #
                                    'score': 5*20
                                    }  
}

# Player
POWER_UP = ["dash", "piercing"]
PLAYER_CONSTANTS = {'weapon': {'rate_of_fire': [0.5, 0.4, 0.3, 0.2, 0.1], 
                               'projectile': {'num': [1, 2, 3], 
                                               'speed': 1500, 
                                               'radius': 5,
                                               "source": pygame.transform.scale(pygame.image.load("src/assets/player_bullets.png"), (4, 24))
                                              },
                                'directions': [1, 2, 3]
                                },
                    'ship': {'turn_speed': 300, 
                             'speed': [200, 400, 600],
                             'power_up': POWER_UP,
                             'radius': 20, 
                             "source": pygame.transform.scale(pygame.image.load("src/assets/player_ship.png"), (20*2, 20*2))
                             },
                    'price': {'rate_of_fire': [100, 300, 600, 1500],
                              'projectile_num': [1000, 2000],
                              'ship_speed': [500, 1000],
                              'directions': [1000, 2500]
                              }
                    }

# Enemy
ENEMY_CONSTANTS =  {'weapon': {'rate_of_fire': [2, 1.5, 1, 0.5], 
                                'projectile': {'speed': [100, 200, 300, 400], 
                                              'radius': 20,
                                              "source": pygame.transform.scale(pygame.image.load("src/assets/enemy_rockets.png"), (24, 72))
                                              },
                              },
                    'ship': {'speed': [(50, 30), (60, 40), (80, 50), (100, 70)], 
                             'spawn_rate': [2, 1.5, 1, 0.5],
                             'spawn_line': 1000,
                             'radius': 50, 
                             "source":  pygame.transform.scale(pygame.image.load("src/assets/enemy_ship.png"), (50*2, 50*2))
                             },
                   }



# Asteroids
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.3  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

ASTEROID_CONSTANTS = {'min_radius': ASTEROID_MIN_RADIUS,
                      'max_radius': ASTEROID_MAX_RADIUS,
                      'kinds': { 'num': ASTEROID_KINDS,
                                'SMALL': pygame.transform.scale(pygame.image.load("src/assets/asteroid_SMALL.png"), (ASTEROID_MIN_RADIUS*2, ASTEROID_MIN_RADIUS*2)),
                                'MIDDLE':pygame.transform.scale(pygame.image.load("src/assets/asteroid_MIDDLE.png"), (ASTEROID_MIN_RADIUS*2*2, ASTEROID_MIN_RADIUS*2*2)),
                                'BIG': pygame.transform.scale(pygame.image.load("src/assets/asteroid_BIG.png"), (ASTEROID_MIN_RADIUS*3*2, ASTEROID_MIN_RADIUS*3*2)),
                                },
                      'spawn_rate': ASTEROID_SPAWN_RATE
                      }

PLANET_CONSTANTS = {'radius': 200,
                    'source': pygame.transform.scale(pygame.image.load("src/assets/earth.png"), (200*2, 200*2))
                    }