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

	player = Player(player_spawn_x, player_spawn_y)
	
	# Game loop
	while True:
		for event in pygame.event.get():
			# If window has been closed, shutdown pygame
			if event.type == pygame.QUIT:
				return
		# Screen fill
		screen.fill(color, rect=None)
		# Drawing objects
		player.draw(screen)
		# Screen update
		pygame.display.flip()
		# Calc tick
		dt = clock.tick(framerate) / 1000
		# Updating player position
		player.update(dt)

if __name__ == "__main__":
	main()
