import pygame
from constants import *
from player import Player  # noqa: F403


def main():
    pygame.init()
    # Creating screen using our constant variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        # this variable will not only store the total game time that has passed, it will also keep our FPS at 60
        game_time = game_clock.tick(60)
        dt = game_time / 1000


if __name__ == "__main__":
    main()
