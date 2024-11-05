import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_LIVES, PLAYER_HIT_COOLDOWN, PLAYER_SPAWN_X, PLAYER_SPAWN_Y
from circleshape import CircleShape
from shooting import Shot

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shot_cooldown = 0
		self.lives = PLAYER_LIVES
		self.damage_cooldown = 0
	
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
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()
		self.shot_cooldown -= dt
		self.damage_cooldown -= dt

	def shoot(self):
		if self.shot_cooldown > 0:
			return
		new_shot = Shot(self.position.x, self.position.y)
		new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
		self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
	
	def reduce_lives(self):
		if self.damage_cooldown > 0:
			return
		self.lives -= 1
		self.damage_cooldown = PLAYER_HIT_COOLDOWN
		print(f'Lost 1 life : {self.lives} lives left')

	def respawn(self):
		self.position.x = PLAYER_SPAWN_X
		self.position.y = PLAYER_SPAWN_Y			


