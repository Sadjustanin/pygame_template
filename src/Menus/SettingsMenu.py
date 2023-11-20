import sys
from typing import Sequence

import pygame
from pygame import Surface, SurfaceType
from pygame.locals import *
from pygame.font import Font
from pygame.rect import RectType, Rect

from src.Enums import Colors
from src.MainSettings import font, main_clock, main_menu_background, WIDTH, HEIGHT, screen

pygame.init()


class SettingsRect:
    def __init__(self):
        self.top_rect: Rect = pygame.Rect((WIDTH / 2 - 550, HEIGHT / 2 - 350),
                                          ((WIDTH / 1.8), (HEIGHT / 1.5)))
        self.top_color: str = "#475F77"

    def draw(self) -> None:
        pygame.draw.rect(screen, self.top_color, self.top_rect)


def draw_text(text: str | bytes | None, received_font: Font,
              color: Color | Color | int | str | tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int],
              surface: Surface, width: float | int, height: float | int) -> None:
    text_obj: Surface | SurfaceType = received_font.render(text, 1, color)
    textrect: Rect | RectType = text_obj.get_rect()
    textrect.topleft = (width, height)
    surface.blit(text_obj, textrect)


def main_menu() -> None:
    settings: SettingsRect = SettingsRect()

    while True:
        screen.blit(pygame.transform.scale(main_menu_background, (WIDTH, HEIGHT)), (0, 0))
        draw_text("main menu", font, Colors.BLACK.value, screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        settings.draw()
        pygame.display.update()
        main_clock.tick(60)


if __name__ == '__main__':
    main_menu()
