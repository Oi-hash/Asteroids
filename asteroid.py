import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_COLOR, ASTEROID_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR , self.position, self.radius, ASTEROID_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Randomizing angle of splitting
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_velocity1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_velocity2 * 1.2

    #def explosion(self):
    #    random_angle = 
