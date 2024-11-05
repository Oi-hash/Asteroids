# Import pygame
import pygame

# Import constants, player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from player import Player


def main():
	# Init PyGame
	pygame.init()
	print(f'Starting asteroids!')
	# FPS / Time tracking
	clock = pygame.time.Clock()
	framerate = 60
	dt = 0
	# Screen obj.
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(f'Screen width: {SCREEN_WIDTH}')
	print(f'Screen height: {SCREEN_HEIGHT}')
	print(f'Framerate: {framerate}')
	# Background color
	color = (0, 0, 0) #RRGGBB
	# Player spawn coordinates
	player_spawn_x = SCREEN_WIDTH / 2
	player_spawn_y = SCREEN_HEIGHT / 2

	# Groups
	group_updatable = pygame.sprite.Group()
	group_drawable = pygame.sprite.Group()

	# Adding player instance to groups
	Player.containers = (group_updatable, group_drawable)

	# Player instance 
	player = Player(player_spawn_x, player_spawn_y)
	
	# Game loop
	while True:
		for event in pygame.event.get():
			# If window has been closed, shutdown pygame
			if event.type == pygame.QUIT:
				return
		# Updating updatable elements
		for element in group_updatable:
			element.update(dt)
		# Screen fill
		screen.fill(color, rect=None)
		# Drawing drawable objects
		for element in group_drawable:
			element.draw(screen)
		# Calc tick / limiting to framerate
		dt = clock.tick(framerate) / 1000
		# Screen update
		pygame.display.flip()
		

if __name__ == "__main__":
	main()
