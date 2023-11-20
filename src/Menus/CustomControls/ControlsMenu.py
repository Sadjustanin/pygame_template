import os

import pygame
from pygame import SurfaceType, Surface, HWSURFACE, DOUBLEBUF, RESIZABLE

from src.MainSettings import WIDTH, HEIGHT, main_clock, \
    main_menu_background_with_buttons
import src.Menus.CustomControls.Util
from src.Menus.CustomControls.ControlsGUI import ControlsHandler

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def run_settings_menu():
    pygame.init()
    running: bool = True

    actions: dict = {"Left": False, "Right": False, "Up": False, "Down": False, "Start": False, "Action1": False}
    canvas: Surface | SurfaceType = pygame.Surface((WIDTH / 2, HEIGHT / 2))
    this_screen: Surface | SurfaceType = pygame.display.set_mode((WIDTH * 4, HEIGHT * 4), pygame.FULLSCREEN,
                                                                 HWSURFACE | DOUBLEBUF | RESIZABLE)

    save: dict[str, int | dict[str, dict[str, int] | dict[str, int]]] = src.Menus.CustomControls.Util.load_save()
    control_handler: ControlsHandler = ControlsHandler(save)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == control_handler.controls['Left']:
                    actions['Left'] = True
                if event.key == control_handler.controls['Right']:
                    actions['Right'] = True
                if event.key == control_handler.controls['Up']:
                    actions['Up'] = True
                if event.key == control_handler.controls['Down']:
                    actions['Down'] = True
                if event.key == control_handler.controls['Start']:
                    actions['Start'] = True
                if event.key == control_handler.controls['Action1']:
                    actions['Action1'] = True

            if event.type == pygame.KEYUP:
                if event.key == control_handler.controls['Left']:
                    actions['Left'] = False
                if event.key == control_handler.controls['Right']:
                    actions['Right'] = False
                if event.key == control_handler.controls['Up']:
                    actions['Up'] = False
                if event.key == control_handler.controls['Down']:
                    actions['Down'] = False
                if event.key == control_handler.controls['Start']:
                    actions['Start'] = False
                if event.key == control_handler.controls['Action1']:
                    actions['Action1'] = False

        control_handler.update(actions)
        canvas.blit(main_menu_background_with_buttons, (0, 0))
        control_handler.render(canvas)

        this_screen.blit(pygame.transform.scale(canvas, (WIDTH * 2, HEIGHT * 2)), (0, 0))
        pygame.display.update()
        main_clock.tick(60)

        src.Menus.CustomControls.Util.reset_keys(actions)
