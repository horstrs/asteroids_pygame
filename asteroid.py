import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_angle = random.uniform(20, 50)
        
        self.instantiate_split_asteroid(new_angle, new_radius)
        self.instantiate_split_asteroid(-new_angle, new_radius)

    def instantiate_split_asteroid(self, new_angle, new_radius):
        new_position = self.velocity.rotate(new_angle)
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = new_position * 1.2