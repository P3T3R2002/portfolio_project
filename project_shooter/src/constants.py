
# Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Map
MAP_WIDTH = 20000
MAP_HIGHT = 10000

# Player
POWER_UP = ["dash", "piercing"]
PLAYER_CONSTANTS = {'weapon': {'rate_of_fire': [0.5, 0.4, 0.3, 0.2, 0.1], 
                               'projectile': {'num': [1, 2, 3], 
                                               'speed':1500, 
                                               'radius': 5
                                               },
                                'directions': [1, 2, 3]
                                },
                    'ship': {'turn_speed': 300, 
                             'radius': 20, 
                             'speed': [200, 400, 600],
                             'lvl_up': [50, 100, 200, 400, 700, 1200, 2000, 3000, 4000, 5000],
                             'power_up': POWER_UP
                             },
                    }

# Enemy
ENEMY_CONSTANTS =  {'weapon': {'rate_of_fire': [2, 1.5, 1, 0.5], 
                                'projectile': {'speed': [100, 200, 300, 400], 
                                              'radius': 20
                                              },
                              },
                    'ship': {'radius': 50, 
                             'speed': [(50, 30), (60, 40), (80, 50), (100, 70)], 
                             'spawn_rate': [2, 1.5, 1, 0.5],
                             'spawn_line': 1000
                             },
                   }


# Asteroids
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.3  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

ASTEROID_CONSTANTS = {'min_radius': ASTEROID_MIN_RADIUS,
                      'max_radius': ASTEROID_MAX_RADIUS,
                      'kinds': ASTEROID_KINDS,
                      'spawn_rate': ASTEROID_SPAWN_RATE
                      }
