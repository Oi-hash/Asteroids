import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

asteroid_color = (255, 255, 255) #RRGGBB
asteroid_width = 2

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, asteroid_color , self.position, self.radius, asteroid_width)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            random_angle = random.uniform(20, 50)
            new_velocity1 = self.position.rotate(random_angle)
            new_velocity2 = self.position.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = new_velocity1 * 1.1
            new_asteroid2.velocity = new_velocity2 * 1.1
            self.kill()