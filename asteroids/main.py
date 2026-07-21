import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_FILL_COLOR
from logger import log_state 

def main():

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    game_clock = pygame.time.Clock()
    delta_time = 0.0

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(SCREEN_FILL_COLOR)
        pygame.display.flip()

        delta_time = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
