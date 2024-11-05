import pygame

from circleshape import CircleShape

asteroid_color = (255, 255, 255) #RRGGBB
asteroid_width = 2

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, asteroid_color , self.position, self.radius, asteroid_width)
    
    def update(self, dt):
        self.position += self.velocity * dt