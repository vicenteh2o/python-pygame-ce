import pygame
import time
import random
from constantes import *
pygame.font.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG_IMAGE = pygame.image.load("bg.jpg")
BG = pygame.transform.scale(BG_IMAGE, (WIDTH, HEIGHT))

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, elapsed_time):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    pygame.draw.rect(WIN, "#ff4500", player)
    pygame.display.update()


def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + player.width + PLAYER_VEL <= WIDTH:
            player.x += PLAYER_VEL

        draw(player, elapsed_time)

    pygame.quit()


if __name__ == "__main__":
    main()
