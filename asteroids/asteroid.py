import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        
        random_rotation_angle = random.uniform(20, 50)
        new_asteroid1_velocity = self.velocity.rotate(random_rotation_angle) * 1.2
        new_asteroid2_velocity = self.velocity.rotate(-random_rotation_angle) * 1.2
        
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

        new_asteroid1.velocity = new_asteroid1_velocity
        new_asteroid2.velocity = new_asteroid2_velocity
        



    def update(self, delta_time: float) -> None:
        self.position += (self.velocity * delta_time)

