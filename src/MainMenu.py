import sys
from typing import Sequence

import pygame
from pygame import Surface, SurfaceType
from pygame.locals import *
from pygame.font import Font
from pygame.rect import RectType, Rect

from src.CustomButtons.CustomButtons.ConnectButton import ConnectButton
from src.CustomButtons.CustomButtons.HostButton import HostButton
from src.CustomButtons.CustomButtons.QuitButton import QuitButton
from src.CustomButtons.CustomButtons.SettingsButton import SettingsButton
from src.MainSettings import main_clock, main_menu_background, screen, current_width, current_height

pygame.init()

host_button: HostButton = HostButton("Host", 300, 100, (current_width - 400, current_height - 600))
connect_button: ConnectButton = ConnectButton("Connect", 300, 100, (current_width - 400, current_height - 450))
settings_button: SettingsButton = SettingsButton("Settings", 300, 100, (current_width - 400, current_height - 300))
quit_button: QuitButton = QuitButton("Quit", 300, 100, (current_width - 400, current_height - 150))


def draw_text(text: str | bytes | None, received_font: Font,
              color: Color | Color | int | str | tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int],
              surface: Surface, width: float | int, height: float | int) -> None:
    text_obj: Surface | SurfaceType = received_font.render(text, 1, color)
    textrect: Rect | RectType = text_obj.get_rect()
    textrect.topleft = (width, height)
    surface.blit(text_obj, textrect)


def main_menu() -> None:
    while True:
        screen.blit(pygame.transform.scale(main_menu_background, (current_width, current_height)), (0, 0))
        # draw_text("main menu", font, Colors.BLACK.value, screen, 20, 20)

        host_button.draw(screen)
        connect_button.draw(screen)
        settings_button.draw(screen)
        quit_button.draw(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        main_clock.tick(60)


if __name__ == '__main__':
    main_menu()
