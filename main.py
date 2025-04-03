import sys
import pygame
from constants import *  # noqa: F403
from asteroidfield import AsteroidField
from player import Player, Shot  # noqa: F403
from asteroid import Asteroid

def main():
    pygame.init()
    # Creating screen using our constant variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405
    game_clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2  # noqa: F405
    y = SCREEN_HEIGHT / 2  # noqa: F405
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers= (updatable, drawable, shots)
    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for item in asteroids:
            if item.colliding(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if item.colliding(shot):
                    shot.kill()
                    item.split()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        # this variable will not only store the total game time that has passed, it will also keep our FPS at 60
        game_time = game_clock.tick(60)
        dt = game_time / 1000


if __name__ == "__main__":
    main()
