# Import pygame
import pygame
import sys
import os

# Import constants, player, asteroidfield, shooting
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, BACKGROUND_IMAGE_PATH, PLAYER_SPAWN_X, PLAYER_SPAWN_Y
from player import Player
from asteroidfield import AsteroidField, Asteroid
from shooting import Shot

def main():
	# Init PyGame
	pygame.init()
	print(f'Starting asteroids!')

	# FPS / Time tracking
	clock = pygame.time.Clock()
	dt = 0

	# Screen obj.
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(f'Screen width: {SCREEN_WIDTH}')
	print(f'Screen height: {SCREEN_HEIGHT}')
	print(f'Framerate: {FRAMERATE}')

	# Setting background image
	background_image = pygame.image.load(BACKGROUND_IMAGE_PATH)
	background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

	# Groups
	group_updatable = pygame.sprite.Group()
	group_drawable = pygame.sprite.Group()
	group_asteroids = pygame.sprite.Group()
	group_shots = pygame.sprite.Group()

	# Adding instances to groups
	Player.containers = (group_updatable, group_drawable)
	Asteroid.containers = (group_asteroids, group_drawable, group_updatable)
	AsteroidField.containers = (group_updatable)
	Shot.containers = (group_drawable, group_updatable, group_shots)

	# Objects
	player = Player(PLAYER_SPAWN_X, PLAYER_SPAWN_Y)
	asteroid = AsteroidField()
	
	# Game loop
	while True:
		for event in pygame.event.get():
			# If window has been closed, shutdown pygame
			if event.type == pygame.QUIT:
				return
		# Updating updatable elements
		for element in group_updatable:
			element.update(dt)
		# Checking for player-asteroid / shot-asteroid collision
		for asteroid in group_asteroids:
			if asteroid.collision_detection(player) and player.damage_cooldown <= 0:
				player.reduce_lives()
				player.respawn()
				if player.lives == 0:
					print(f'Game Over!')
					sys.exit()

			for bullet in group_shots:
				if asteroid.collision_detection(bullet):
					bullet.kill()
					asteroid.split()

		# Screen blit with background image
		screen.blit(background_image,(0, 0))

		# Drawing drawable objects
		for element in group_drawable:
			element.draw(screen)
		# Calc tick / limiting to framerate
		dt = clock.tick(FRAMERATE) / 1000
		# Screen update
		pygame.display.flip()
		

if __name__ == "__main__":
	main()
