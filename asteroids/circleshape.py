import pygame

class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None: 
        # inheriting classes must override
        pass

    def collides_with(self, other_object: "CircleShape") -> bool:
        distance_between_objects = pygame.math.Vector2.distance_to(self.position, other_object.position)
        return distance_between_objects <=(self.radius + other_object.radius)

    def update(self, delta_time: float) -> None:
        # inheriting classes must override
        pass
