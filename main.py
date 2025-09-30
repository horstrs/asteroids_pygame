import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(COLOR_BLACK)
        for object in drawable_group:
            object.draw(screen)
        updatable_group.update(delta_time)
        for asteroid in asteroids_group:
            if asteroid.collision_check(player):
                sys.exit("Game Over!")
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
