# Modules
import pygame
from constants import PLAYER_COLOR, PLAYER_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
	    pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), PLAYER_WIDTH)
       
    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision_detection(self, other_circle):
        distance = self.position.distance_to(other_circle.position)
        if distance <= (self.radius + other_circle.radius):
            return True
        return False

        



