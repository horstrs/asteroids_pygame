import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, shoot_cd):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cd = shoot_cd
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time
    
    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.lower_shoot_cd(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)
        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_SPACE]:
            if self.can_shoot():
                self.shoot()

    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity += forward * PLAYER_SHOOT_SPEED
        self.shoot_cd = PLAYER_SHOOT_COOLDOWN

    def can_shoot(self):
        return self.shoot_cd <= 0
    
    def lower_shoot_cd(self, delta_time):
        self.shoot_cd -= delta_time