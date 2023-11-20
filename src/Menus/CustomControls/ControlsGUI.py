import os
from typing import Sequence

import pygame
import sys
from pygame import Surface, SurfaceType, Rect, Color
from pygame.font import Font
from pygame.rect import RectType

from src.Menus.CustomControls.Util import write_save

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class ControlsHandler:
    def __init__(self, save):
        self.cursor_dict = None
        self.font = None
        self.curr_index = None
        self.selected = None
        self.save_file: any = save
        self.curr_block: any = save["current_profile"]
        self.controls: any = self.save_file["controls"][str(self.curr_block)]
        self.setup()

    def update(self, actions: any) -> None:
        if self.selected:
            self.set_new_control()
        else:
            self.navigate_menu(actions)

    def render(self, surface: Surface | SurfaceType) -> None:
        self.draw_text(surface, "Control Profile " + str(self.curr_block + 1), 20, pygame.Color((0, 0, 0)), 480 / 2,
                       270 / 8)
        self.display_controls(surface, self.save_file["controls"][str(self.curr_block)])
        if self.curr_block == self.save_file["current_profile"]:
            self.draw_text(surface, "*", 20,
                           pygame.Color((0, 0, 0)), 20, 20)

    def navigate_menu(self, actions: any) -> None:

        if actions["Down"]:
            self.curr_index: int = (self.curr_index + 1) % (
                    len(self.save_file["controls"][str(self.curr_block)]) + 1)
        if actions["Up"]:
            self.curr_index: int = (self.curr_index - 1) % (
                    len(self.save_file["controls"][str(self.curr_block)]) + 1)

        if actions["Left"]:
            self.curr_block: int = (self.curr_block - 1) % len(self.save_file["controls"])
        if actions["Right"]:
            self.curr_block: int = (self.curr_block + 1) % len(self.save_file["controls"])

        if actions["Action1"] or actions["Start"]:

            if self.cursor_dict[self.curr_index] == "Set":
                self.controls: any = self.save_file["controls"][str(self.curr_block)]
                self.save_file["current_profile"] = self.curr_block
                write_save(self.save_file)
            else:
                self.selected: bool = True

    def set_new_control(self) -> None:
        selected_control: any = self.cursor_dict[self.curr_index]
        done: bool = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key not in self.save_file["controls"][str(self.curr_block)].values():
                        self.save_file["controls"][str(self.curr_block)][selected_control] = event.key
                        write_save(self.save_file)
                        self.selected = False
                        done = True

    def display_controls(self, surface: Surface | SurfaceType, controls: any) -> None:
        color: tuple = (255, 13, 5) if self.selected else (255, 250, 239)
        pygame.draw.rect(surface, color, (80, 270 / 4 - 10 + (self.curr_index * 30), 320, 20))
        i: int = 0
        for control in controls:
            self.draw_text(surface, control + ' - ' + pygame.key.name(controls[control]), 20,
                           pygame.Color((0, 0, 0)), 480 / 2, 270 / 4 + i)
            i += 30
        self.draw_text(surface, "Set Current Profile", 20, pygame.Color((0, 0, 0)), 480 / 2, 270 / 4 + i)

    def setup(self) -> None:
        self.selected: bool = False
        self.font: Font = pygame.font.Font("RetroFont.ttf", 20)
        self.cursor_dict: dict = dict()
        self.curr_index: int = 0
        i: int = 0
        for control in self.controls:
            self.cursor_dict[i] = control
            i += 1
        self.cursor_dict[i] = "Set"

    def draw_text(self, surface: Surface | SurfaceType, text: str,
                  size: Color | Color | int | str | tuple[int, int, int] | tuple[int, int, int, int] | Sequence[
                      int] | None,
                  color: Color | Color | int | str | tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int],
                  x: float | int, y: float | int) -> None:
        text_surface: Surface | SurfaceType = self.font.render(text, True, color, size)
        text_surface.set_colorkey((0, 0, 0))
        text_rect: Rect | RectType = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)
