import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    SHOT_RADIUS = 5

    def __init__(self, x, y):
        super().__init__(x, y, Shot.SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0) # Initialize Velocity, to be set by player class
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, surface):
        color = (100, 200, 200)
        pygame.draw.circle(surface, color, [int(self.position.x), int(self.position.y)], self.radius)


    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def is_off_screen(self, screen_width, screen_height):
        return (self.position.x < 0 or
                self.position.x > screen_width or
                self.position.y < 0 or
                self.position.y > screen_height)

        