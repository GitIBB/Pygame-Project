from circleshape import *
import pygame
import random
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
	

	def draw(self, surface):
		color = (158, 158, 158)
		pygame.draw.circle(surface, color, [self.position.x, self.position.y], self.radius, 2)




	def update(self, dt):
		self.position.x += self.velocity.x * dt
		self.position.y += self.velocity.y * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return []
		
		else:
			random_angle = random.uniform(20, 50)
			new_velocity_1 = self.velocity.rotate(random_angle)
			new_velocity_2 = self.velocity.rotate(-random_angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid_1.velocity = new_velocity_1
			new_asteroid_2.velocity = new_velocity_2

			return [new_asteroid_1, new_asteroid_2]
	
			