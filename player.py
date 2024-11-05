import pygame

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
	
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt
	
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()
		print(f'DT on update: {dt}')
		if keys[pygame.K_a]:
			Player.rotate(self, -dt)
		if keys[pygame.K_d]:
			Player.rotate(self, dt)
		if keys[pygame.K_w]:
			Player.move(self, dt)
		if keys[pygame.K_s]:
			Player.move(self, -dt)
