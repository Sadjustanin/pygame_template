import os

import pygame
from pygame import Surface, SurfaceType, HWSURFACE, DOUBLEBUF, RESIZABLE
from pygame.sysfont import SysFont
from pygame.time import Clock
from screeninfo import get_monitors

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()

font: SysFont = pygame.sysfont.SysFont("comicsansms", 100, True, True)
main_clock: Clock = pygame.time.Clock()
main_menu_background: Surface | SurfaceType = pygame.image.load("../assets/images/main_menu_background.png")
main_menu_background_with_buttons: Surface | SurfaceType = pygame.image.load(
    "../assets/images/main_menu_background_with_buttons.png")

WIDTH: int = 0
HEIGHT: int = 0

current_info = pygame.display.Info()
current_width: int = current_info.current_w
current_height: int = current_info.current_h

for i in get_monitors():
    WIDTH = i.width
    HEIGHT = i.height

pygame.display.set_caption("Karamba")

screen: Surface | SurfaceType = pygame.display.set_mode((current_width, current_height),
                                                        HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_icon(main_menu_background)
