import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_FILL_COLOR
from logger import log_state 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    game_clock = pygame.time.Clock()
    delta_time: float = 0.0
    
    center_position_x: float = SCREEN_WIDTH / 2
    center_position_y: float = SCREEN_HEIGHT / 2

    # pygame groups for classes
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(center_position_x, center_position_y)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(SCREEN_FILL_COLOR)
        delta_time = game_clock.tick(60) / 1000
        
        updatable.update(delta_time)
        
        for element in drawable:
            element.draw(screen)
        
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()
