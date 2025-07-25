import pygame
from enemy import*
from player import*
from Planet.shoot import *

def go_Planet(planet, player, hud):
    dt = 0
    screen = pygame.display.get_surface()
    game_time = pygame.time.Clock()

    while True:
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        enemys = pygame.sprite.Group()
        shoots = pygame.sprite.Group()

        Planet_Shoot.containers = (shoots, updatable, drawable)
        Enemy.containers = (enemys, updatable, drawable)
        
        score = 0
        winner = False
        while not winner:
            screen.fill('black')
            for thing in updatable:
                thing.update(dt)
            player.update(dt)
            planet.update(dt)

            for thing in drawable:
                thing.draw(screen)
            player.draw(screen)
            hud.draw(screen)


            for bullet1 in shoots:
                for bullet2 in shoots:
                    if bullet1.collsion(bullet2):               
                        bullet2.kill()
                        bullet1.kill()
                        score += 1    
                        player.score += 1 
                        hud.update_score(player.score)
                        hud.update_fight(score)   
                for enemy in enemys:
                    if enemy.collsion(bullet1): 
                        score += 5   
                        player.score += 5  
                        hud.update_score(player.score)  
                        hud.update_fight(score)  
                        enemy.kill()
                        bullet1.kill()
                if bullet1.position.x > SCREEN_WIDTH and bullet1.friendly:
                    bullet1.kill()
                if player.collsion(bullet1):
                    print(f"Game Over!\nYour score: {player.score}")
                    player.dead = True
                    return True 
            for enemy in enemys:
                if player.collsion(enemy):
                    print(f"Game Over!\nYour score: {player.score}")
                    player.dead = True
                    return True

            if score > 50 * 2 ** (planet.difficulty-1):
                winner = True
                planet.completed()
                return planet
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None

            pygame.display.flip()
            dt = game_time.tick(60)/1000


 