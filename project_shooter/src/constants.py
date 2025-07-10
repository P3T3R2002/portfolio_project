SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

MAP_WIDTH = 20000
MAP_HIGHT = 10000

PLAYER_RADIUS = 20
PLAYER_SPEED = 600
PLAYER_TURN_SPEED = 300
PLAYER_SHOOT_SPEED = 1500
PLAYER_SHOOT_COOLDOWN = 0.5
PLAYER_SHOT_RADIUS = 5
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.3  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS


ENEMY_X_LINE = 1000

ENEMY_RADIUS = 50
ENEMY_SHOOT_SPEED = 200
ENEMY_SHOOT_COOLDOWN = 2
ENEMY_SHOT_RADIUS = 20

ENEMY_WEAPON_SPEED = [2, 1.5, 1, 0.5]
ENEMY_SHOOT_SPEED = [100, 200, 300, 400]
ENEMY_SPAWN_RATE = [2, 1.5, 1, 0.5]
ENEMY_SPEED = [(50, 30), (60, 40), (80, 50), (100, 70)]

PLAYER_WEAPON_SPEED = [0.5, 0.4, 0.3, 0.2, 0.1]
PROJECTILES = [1, 2, 3]
DIRECTIONS = [1, 2, 4]
PLAYER_SPEED = [200, 400, 600]


POWER_UP = ["dash", "piercing"]
GAME_CONSTANTS = {'player': {'weapon': {'rate_of_fire': PLAYER_WEAPON_SPEED, 
                                        'projectiles': {'num': PROJECTILES, 
                                                        'speed':PLAYER_SHOOT_SPEED, 
                                                        'radius': PLAYER_SHOT_RADIUS},
                                        'directions': DIRECTIONS
                                        },
                            'ship': {'turn_speed': PLAYER_TURN_SPEED, 
                                     'radius': PLAYER_RADIUS, 
                                     'speed': PLAYER_SPEED, 
                                     'power_up': POWER_UP
                                     },
                            },
                  'enemy': {'weapon': {'speed':ENEMY_SHOOT_SPEED, 
                                       'rate_of_fire': ENEMY_WEAPON_SPEED, 
                                        'projectiles': {'speed': ENEMY_SHOOT_SPEED, 
                                                        'radius': ENEMY_SHOT_RADIUS},
                                       },
                            'ship': {'radius': ENEMY_RADIUS, 
                                     'speed': ENEMY_SPEED, 
                                     'spawn_rate': ENEMY_SPAWN_RATE
                                     },
                            },
                  'screen': {'width': SCREEN_WIDTH, 
                             'height': SCREEN_HEIGHT
                             }  
                    }