import asyncio

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_event, log_state
from player import Player
from shot import Shot

pygame.init()
clock = pygame.time.Clock()

async def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    hud_font = pygame.font.Font(None, HUD_FONT_SIZE)
    score = 0
    level = 1
    dt = 0.0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                return

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    score += ASTEROID_SCORE
                    new_level = score // SCORE_PER_LEVEL + 1
                    if new_level > level:
                        old_speed_multiplier = 1 + (level - 1) * ASTEROID_SPEED_INCREASE_PER_LEVEL
                        level = new_level
                        new_speed_multiplier = 1 + (level - 1) * ASTEROID_SPEED_INCREASE_PER_LEVEL
                        for active_asteroid in asteroids:
                            active_asteroid.velocity *= new_speed_multiplier / old_speed_multiplier
                        asteroid_field.level = level
                        log_event("level_up", level=level, score=score)
                    asteroid.split()
                    shot.kill()
                    break

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        hud = hud_font.render(f"Score: {score}    Level: {level}", True, "white")
        screen.blit(hud, (20, 20))
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())
