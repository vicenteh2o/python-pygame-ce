import pygame
import time
import random

from constantes import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG_IMAGE = pygame.image.load("bg.jpg")
BG = pygame.transform.scale(BG_IMAGE, (WIDTH, HEIGHT))


def draw(player):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, "#ff4500", player)
    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d]:
            player.x += PLAYER_VEL

        draw(player)

    pygame.quit()


if __name__ == "__main__":
    main()
