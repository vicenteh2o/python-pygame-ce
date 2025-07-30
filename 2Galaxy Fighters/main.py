import pygame

from const import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Fighters")

BORDER = pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)


def draw_window(red, yellow):
    WIN.fill(COLORS["black"])
    pygame.draw.rect(WIN, COLORS["red"], BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def main():
    red = RED_SPACESHIP.get_rect(center=(700, 300))
    yellow = YELLOW_SPACESHIP.get_rect(center=(100, 300))

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
