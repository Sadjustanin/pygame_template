import os

import pygame
from pygame import Surface, SurfaceType, HWSURFACE, DOUBLEBUF, RESIZABLE
from pygame.sysfont import SysFont
from pygame.time import Clock
from screeninfo import get_monitors

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

font: SysFont = pygame.sysfont.SysFont("comicsansms", 100, True, True)
main_clock: Clock = pygame.time.Clock()
main_menu_background: Surface | SurfaceType = pygame.image.load("../assets/images/main_menu_background.png")
main_menu_background_with_buttons: Surface | SurfaceType = pygame.image.load(
    "../assets/images/main_menu_background_with_buttons.png")

WIDTH: int = 0
HEIGHT: int = 0

for i in get_monitors():
    WIDTH = i.width
    HEIGHT = i.height

pygame.display.set_caption("Karamba")

screen: Surface | SurfaceType = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN,
                                                        HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_icon(main_menu_background)
