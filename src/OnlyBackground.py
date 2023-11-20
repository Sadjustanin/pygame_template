import sys

import pygame
from pygame.locals import QUIT

from src.MainSettings import screen, main_clock, main_menu_background, WIDTH, HEIGHT

pygame.init()


def main_menu() -> None:
    while True:
        screen.blit(pygame.transform.scale(main_menu_background, (WIDTH, HEIGHT)), (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        pygame.display.update()
        main_clock.tick(60)


if __name__ == '__main__':
    main_menu()
