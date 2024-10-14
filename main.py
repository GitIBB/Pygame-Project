# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	# Initialize the game
	pygame.init()
	# Set the display screen width and screen height
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	# Print starting messages
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	# Create the timer for how fast to refresh the screen
	clock = pygame.time.Clock()
	dt = clock.tick(60) / 1000

	shots = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	running = True
	while running:
		current_time = pygame.time.get_ticks()

		# Is shooting_
		if player.is_shooting:
			player.shoot(current_time, shots)

		# Fill Screen with Black background
		screen.fill((0, 0, 0))

		# Update game state
		for obj in updatable:
			obj.update(dt)

		# For loop to quit the game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0
			
		 # Shot key check
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					player.is_shooting = True
			elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
					player.is_shooting = False

		# Collision Check
		for obj in asteroids:
			if obj.collision(player):
				print("Game Over!")
				return 0
			
		for obj in asteroids:
			for shot in shots:
				print(f"checking collision: asteroid at {obj.rect.center}, Shot at {shot.rect.center}")
				if obj.collision(shot):
					print("collision detected")
					shot.kill()
					shots.remove(shot)

					# call split method from asteroid.py
					new_asteroids = obj.split()
					asteroids.add(*new_asteroids)

					obj.kill()
					asteroids.remove(obj)

		
		# Update Shots
		for shot in shots:
			shot.update(dt)
			if shot.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
				shot.kill()
			
		# draw game objects
		for sprite in drawable:
			sprite.draw(screen)

		# Update the display
		pygame.display.flip()

		# Set FPS to 60
		clock.tick(60)
		
		print(f"number of asteroids: {len(asteroids)}, number of shots: {len(shots)}")



if __name__ == "__main__":
    main()
