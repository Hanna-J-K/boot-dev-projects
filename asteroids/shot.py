import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, BULLET_COLOR, self.position, self.radius, LINE_WIDTH)
        
    def update(self, delta_time: float) -> None:
        self.position += (self.velocity * delta_time)
