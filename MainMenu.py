import sys
from enum import Enum, unique
from typing import Sequence

import pygame
from pygame import Surface, SurfaceType
from pygame.locals import *
from pygame.font import SysFont, Font
from pygame.rect import RectType, Rect
from pygame.time import Clock
from screeninfo import get_monitors


@unique
class Colors(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


@unique
class Keyboard(Enum):
    K_BACKSPACE = "K_BACKSPACE"
    K_TAB = "K_TAB"
    K_CLEAR = "K_CLEAR"
    K_RETURN = "K_RETURN"
    K_PAUSE = "K_PAUSE"
    K_ESCAPE = "K_ESCAPE"
    K_SPACE = "K_SPACE"
    K_EXCLAIM = "K_EXCLAIM"
    K_QUOTEDBL = "K_QUOTEDBL"
    K_HASH = "K_HASH"
    K_DOLLAR = "K_DOLLAR"
    K_AMPERSAND = "K_AMPERSAND"
    K_QUOTE = "K_QUOTE"
    K_LEFTPAREN = "K_LEFTPAREN"
    K_RIGHTPAREN = "K_RIGHTPAREN"
    K_ASTERISK = "K_ASTERISK"
    K_PLUS = "K_PLUS"
    K_COMMA = "K_COMMA"
    K_MINUS = "K_MINUS"
    K_PERIOD = "K_PERIOD"
    K_SLASH = "K_SLASH"
    K_0 = "K_0"
    K_1 = "K_1"
    K_2 = "K_2"
    K_3 = "K_3"
    K_4 = "K_4"
    K_5 = "K_5"
    K_6 = "K_6"
    K_7 = "K_7"
    K_8 = "K_8"
    K_9 = "K_9"
    K_COLON = "K_COLON"
    K_SEMICOLON = "K_SEMICOLON"
    K_LESS = "K_LESS"
    K_EQUALS = "K_EQUALS"
    K_GREATER = "K_GREATER"
    K_QUESTION = "K_QUESTION"
    K_AT = "K_AT"
    K_LEFTBRACKET = "K_LEFTBRACKET"
    K_BACKSLASH = "K_BACKSLASH"
    K_RIGHTBRACKET = "K_RIGHTBRACKET"
    K_CARET = "K_CARET"
    K_UNDERSCORE = "K_UNDESCORE"
    K_BACKQUOTE = "K_BACKQUOTE"
    K_a = "K_a"
    K_b = "K_b"
    K_c = "K_c"
    K_d = "K_d"
    K_e = "K_e"
    K_f = "K_f"
    K_g = "K_g"
    K_h = "K_h"
    K_i = "K_i"
    K_j = "K_j"
    K_k = "K_k"
    K_l = "K_l"
    K_m = "K_m"
    K_n = "K_n"
    K_o = "K_o"
    K_p = "K_p"
    K_q = "K_q"
    K_r = "K_r"
    K_s = "K_s"
    K_t = "K_t"
    K_u = "K_u"
    K_v = "K_v"
    K_w = "K_w"
    K_x = "K_x"
    K_y = "K_y"
    K_z = "K_z"
    K_DELETE = "K_DELETE"
    K_KP0 = "K_KP0"
    K_KP1 = "K_KP1"
    K_KP2 = "K_KP2"
    K_KP3 = "K_KP3"
    K_KP4 = "K_KP4"
    K_KP5 = "K_KP5"
    K_KP6 = "K_KP6"
    K_KP7 = "K_KP7"
    K_KP8 = "K_KP8"
    K_KP9 = "K_KP9"
    K_KP_PERIOD = "K_KP_PERIOD"
    K_KP_DIVIDE = "K_KP_DIVIDE"
    K_KP_MULTIPLY = "K_KP_MULTIPLY"
    K_KP_MINUS = "K_KP_MINUS"
    K_KP_PLUS = "K_KP_PLUS"
    K_KP_ENTER = "K_KP_ENTER"
    K_KP_EQUALS = "K_KP_EQUALS"
    K_UP = "K_UP"
    K_DOWN = "K_DOWN"
    K_RIGHT = "K_RIGHT"
    K_LEFT = "K_LEFT"
    K_INSERT = "K_INSERT"
    K_HOME = "K_HOME"
    K_END = "K_END"
    K_PAGEUP = "K_PAGEUP"
    K_PAGEDOWN = "K_PAGEDOWN"
    K_F1 = "K_F1"
    K_F2 = "K_F2"
    K_F3 = "K_F3"
    K_F4 = "K_F4"
    K_F5 = "K_F5"
    K_F6 = "K_F6"
    K_F7 = "K_F7"
    K_F8 = "K_F8"
    K_F9 = "K_F9"
    K_F10 = "K_F10"
    K_F11 = "K_F11"
    K_F12 = "K_F12"
    K_F13 = "K_F13"
    K_F14 = "K_F14"
    K_F15 = "K_F15"
    K_NUMLOCK = "K_NUMLOCK"
    K_CAPSLOCK = "K_CAPSLOCK"
    K_SCROLLOCK = "K_SCROLLOCK"
    K_RSHIFT = "K_RSHIFT"
    K_LSHIFT = "K_LSHIFT"
    K_RCTRL = "K_RCTRL"
    K_LCTRL = "K_LCTRL"
    K_RALT = "K_RALT"
    K_LALT = "K_LATL"
    K_RMETA = "K_RMETA"
    K_LMETA = "K_LMETA"
    K_LSUPER = "K_LSUPER"
    K_RSUPER = "K_RSUPER"
    K_MODE = "K_MODE"
    K_HELP = "K_HELP"
    K_PRINT = "K_PRINT"
    K_SYSREQ = "K_SYSREQ"
    K_BREAK = "K_BREAK"
    K_MENU = "K_MENU"
    K_POWER = "K_POWER"
    K_EURO = "K_EURO"


class Button:
    def __init__(self, text: str | bytes | None, width: float | int, height: float | int,
                 pos: tuple[float, float] | tuple[int, int] | tuple[float, int] | tuple[int, float]) -> None:

        # top rectangle
        self.top_rect: Rect = pygame.Rect(pos, (width, height))
        self.top_color: str = "#475F77"

        # text
        self.text_surf: Surface | SurfaceType = font.render(text, True, "#FFFFFF")
        self.text_rect: Rect | RectType = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self) -> None:
        pygame.draw.rect(screen, self.top_color, self.top_rect)
        screen.blit(self.text_surf, self.text_rect)

WIDTH: int = 0
HEIGHT: int = 0

for i in get_monitors():
    WIDTH = i.width
    HEIGHT = i.height

pygame.init()
pygame.display.set_caption("Karamba")

screen: Surface | SurfaceType = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN,
                                                        HWSURFACE | DOUBLEBUF | RESIZABLE)

font: SysFont = pygame.sysfont.SysFont("comicsansms", 100, True, True)
button1: Button = Button("Click me", 200, 100, (100, 150))
main_clock: Clock = pygame.time.Clock()
main_menu_background: Surface | SurfaceType = pygame.image.load("assets/main_menu_background.png")
pygame.display.set_icon(main_menu_background)


def draw_text(text: str | bytes | None, font: Font,
              color: Color | Color | int | str | tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int],
              surface: Surface, width: float | int, height: float | int) -> None:
    text_obj: Surface | SurfaceType = font.render(text, 1, color)
    textrect: Rect | RectType = text_obj.get_rect()
    textrect.topleft = (width, height)
    surface.blit(text_obj, textrect)


def main_menu() -> None:
    clicked: bool = False

    while True:
        screen.blit(pygame.transform.scale(main_menu_background, (WIDTH, HEIGHT)), (0, 0))
        draw_text("main menu", font, Colors.BLACK.value, screen, 20, 20)

        mouse_width, mouse_height = pygame.mouse.get_pos()

        game_menu: Rect = pygame.Rect(50, 200, 200, 50)
        settings_menu: Rect = pygame.Rect(50, 300, 200, 50)

        if game_menu.collidepoint((mouse_width, mouse_height)):
            if clicked:
                game()
                return

        if settings_menu.collidepoint((mouse_width, mouse_height)):
            if clicked:
                options()
                return

        pygame.draw.rect(screen, Colors.BLACK.value, game_menu)
        pygame.draw.rect(screen, Colors.BLACK.value, settings_menu)

        clicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == Keyboard.K_DOWN.value:
                if event.key() == Keyboard.K_ESCAPE.value:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

        pygame.display.update()
        main_clock.tick(60)


def game() -> None:
    clicked: bool = False

    while True:
        screen.blit(pygame.transform.scale(main_menu_background, (WIDTH, HEIGHT)), (0, 0))
        draw_text("game", font, Colors.BLACK.value, screen, 20, 20)

        main_menu_rect: Rect = pygame.Rect(50, 100, 200, 50)
        pygame.draw.rect(screen, Colors.BLACK.value, main_menu_rect)

        mouse_width, mouse_height = pygame.mouse.get_pos()

        if main_menu_rect.collidepoint((mouse_width, mouse_height)):
            if clicked:
                main_menu()
                return

        clicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

        pygame.display.update()
        main_clock.tick(60)


def options() -> None:
    clicked: bool = False

    while True:
        screen.blit(pygame.transform.scale(main_menu_background, (WIDTH, HEIGHT)), (0, 0))
        draw_text("options", font, Colors.BLACK.value, screen, 20, 20)
        button1.draw()

        main_menu_rect: Rect = pygame.Rect(50, 100, 200, 50)
        pygame.draw.rect(screen, Colors.BLACK.value, main_menu_rect)

        mouse_width, mouse_height = pygame.mouse.get_pos()

        if main_menu_rect.collidepoint((mouse_width, mouse_height)):
            if clicked:
                main_menu()
                return

        clicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

        pygame.display.update()
        main_clock.tick(60)


if __name__ == '__main__':
    options()
