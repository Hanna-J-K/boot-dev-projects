import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        triangle_points: list[pygame.Vector2] = self.triangle()
        pygame.draw.polygon(screen, PLAYER_COLOR, triangle_points, LINE_WIDTH)

    def rotate(self, delta_time: float) -> None:
        self.rotation += (PLAYER_TURN_SPEED * delta_time)

    def move(self, delta_time: float) -> None:
        movement_unit_vector = pygame.Vector2(0, 1)
        rotated_vector = movement_unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * delta_time
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        if self.shot_cooldown > 0:
            return
        else:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED

    def update(self, delta_time: float) -> None:
        self.shot_cooldown -= delta_time
        keys = pygame.key.get_pressed()

        # move
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-delta_time)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(delta_time)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(delta_time)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-delta_time)

        # shoot
        if keys[pygame.K_SPACE]:
            self.shoot()
