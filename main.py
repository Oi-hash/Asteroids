# Import pygame
import pygame

# Import constants
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

def main():
	# Init
	pygame.init()
	print(f'Starting asteroids!')
	# FPS / Time tracking
	cl = pygame.time.Clock()
	framerate = 60
	dt = 0
	# Screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(f'Screen width: {SCREEN_WIDTH}')
	print(f'Screen height: {SCREEN_HEIGHT}')
	print(f'Framerate: {framerate}')
	# Background color
	color = (0, 0, 0) #RRGGBB
	# Game loop
	while True:
		for event in pygame.event.get():
			# If window has been closed, shutdown pygame
			if event.type == pygame.QUIT:
				return
		# Screen fill
		screen.fill(color, rect=None)
		# Screen update
		pygame.display.flip()
		# 
		dt = cl.tick(framerate) / 1000
		print(f'dt: {dt}')
		

if __name__ == "__main__":
	main()
