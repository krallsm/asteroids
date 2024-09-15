import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self, dt):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, radius)
            asteroid1.velocity = self.velocity.rotate(angle)
            asteroid1.position += asteroid1.velocity * (dt * 1.2)
            asteroid2 = Asteroid(self.position.x, self.position.y, radius)
            asteroid2.velocity = self.velocity.rotate(-angle)
            asteroid2.position += asteroid2.velocity * (dt * 1.2)
            return [asteroid1, asteroid2]