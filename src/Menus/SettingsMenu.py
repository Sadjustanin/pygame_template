import os
import sys

import pygame
from pygame import Surface, SurfaceType, RESIZABLE, DOUBLEBUF, HWSURFACE

from src.CustomButtons.ImageButton import ImageButton
from src.MainSettings import WIDTH, HEIGHT

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

this_screen: Surface | SurfaceType = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption("Settings")

change_resolution_button: ImageButton = ImageButton(WIDTH / 2 - (252 / 2), 100, 252, 74, "Resolution",
                                                    "../../assets/images"
                                                    "/image_button.png", "../../assets/images/image_button_hovered.png",
                                                    "../../assets/sounds/button_click_sound.mp3")
audio_switch_button: ImageButton = ImageButton(WIDTH / 2 - (252 / 2), 200, 252, 74, "Audio Switch",
                                               "../../assets/images"
                                               "/image_button.png", "../../assets/images/image_button_hovered.png",
                                               "../../assets/sounds/button_click_sound.mp3")
audio_slider_button: ImageButton = ImageButton(WIDTH / 2 - (252 / 2), 300, 252, 74, "Audio slider",
                                               "../../assets/images"
                                               "/image_button.png", "../../assets/images/image_button_hovered.png",
                                               "../../assets/sounds/button_click_sound.mp3")


def settings_menu():
    running: bool = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            change_resolution_button.handle_event(event)
            audio_switch_button.handle_event(event)
            audio_slider_button.handle_event(event)

        change_resolution_button.check_hover(pygame.mouse.get_pos())
        change_resolution_button.draw(this_screen)
        audio_switch_button.check_hover(pygame.mouse.get_pos())
        audio_switch_button.draw(this_screen)
        audio_slider_button.check_hover(pygame.mouse.get_pos())
        audio_slider_button.draw(this_screen)

        pygame.display.flip()


settings_menu()
