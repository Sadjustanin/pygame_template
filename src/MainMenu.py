import sys
from typing import Sequence

import pygame
from pygame import Surface, SurfaceType
from pygame.locals import *
from pygame.font import Font
from pygame.rect import RectType, Rect

from src.CustomButtons.ConnectButton import ConnectButton
from src.CustomButtons.HostButton import HostButton
from src.CustomButtons.QuitButton import QuitButton
from src.CustomButtons.SettingsButton import SettingsButton
from src.MainSettings import main_clock, main_menu_background, WIDTH, HEIGHT, screen

pygame.init()

host_button: HostButton = HostButton("Host", 300, 100, (WIDTH - 400, HEIGHT - 600))
connect_button: ConnectButton = ConnectButton("Connect", 300, 100, (WIDTH - 400, HEIGHT - 450))
settings_button: SettingsButton = SettingsButton("Settings", 300, 100, (WIDTH - 400, HEIGHT - 300))
quit_button: QuitButton = QuitButton("Quit", 300, 100, (WIDTH - 400, HEIGHT - 150))


def draw_text(text: str | bytes | None, received_font: Font,
              color: Color | Color | int | str | tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int],
              surface: Surface, width: float | int, height: float | int) -> None:
    text_obj: Surface | SurfaceType = received_font.render(text, 1, color)
    textrect: Rect | RectType = text_obj.get_rect()
    textrect.topleft = (width, height)
    surface.blit(text_obj, textrect)


def main_menu() -> None:
    while True:
        screen.blit(pygame.transform.scale(main_menu_background, (WIDTH, HEIGHT)), (0, 0))
        # draw_text("main menu", font, Colors.BLACK.value, screen, 20, 20)

        host_button.draw()
        connect_button.draw()
        settings_button.draw()
        quit_button.draw()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        main_clock.tick(60)


if __name__ == '__main__':
    main_menu()
