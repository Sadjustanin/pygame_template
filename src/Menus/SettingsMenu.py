import os
import sys

import pygame

from src.CustomButtons.ImageButtons.AudioSliderButton import AudioSliderButton
from src.CustomButtons.ImageButtons.AudioSwitchButton import AudioSwitchButton
from src.CustomButtons.ImageButtons.BackToMainMenuButton import BackToMainMenuButton
from src.CustomButtons.ImageButtons.ChangeResolutionButton import ChangeResolutionButton
from src.CustomButtons.ImageButtons.ImageButton import ImageButton
from src.MainSettings import WIDTH, screen, main_menu_background, current_height, current_width

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

pygame.display.set_caption("Settings")
pygame.display.set_icon(main_menu_background)

change_resolution_button: ChangeResolutionButton = ChangeResolutionButton(WIDTH / 2 - (252 / 2), 100, 252, 74, "Resolution",
                                                    "../../assets/images"
                                                    "/image_button.png", "../../assets/images/image_button_hovered.png",
                                                    "../../assets/sounds/button_click_sound.mp3")
audio_switch_button: AudioSwitchButton = AudioSwitchButton(WIDTH / 2 - (252 / 2), 200, 252, 74, "Audio Switch",
                                               "../../assets/images"
                                               "/image_button.png", "../../assets/images/image_button_hovered.png",
                                               "../../assets/sounds/button_click_sound.mp3")
audio_slider_button: AudioSliderButton = AudioSliderButton(WIDTH / 2 - (252 / 2), 300, 252, 74, "Audio slider",
                                               "../../assets/images"
                                               "/image_button.png", "../../assets/images/image_button_hovered.png",
                                               "../../assets/sounds/button_click_sound.mp3")
back_to_main_menu_button: BackToMainMenuButton = BackToMainMenuButton(WIDTH / 2 - (252 / 2), 400, 252, 74, "Back",
                                                    "../../assets/images"
                                                    "/image_button.png", "../../assets/images/image_button_hovered.png",
                                                    "../../assets/sounds/button_click_sound.mp3")


def settings_menu():
    running: bool = True

    while running:
        screen.blit(pygame.transform.scale(main_menu_background, (current_width, current_height)), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            for button in [change_resolution_button, audio_switch_button, audio_slider_button,
                           back_to_main_menu_button]:
                button.handle_event(event)

        change_resolution_button.check_hover(pygame.mouse.get_pos())
        change_resolution_button.draw(screen)
        audio_switch_button.check_hover(pygame.mouse.get_pos())
        audio_switch_button.draw(screen)
        audio_slider_button.check_hover(pygame.mouse.get_pos())
        audio_slider_button.draw(screen)
        back_to_main_menu_button.check_hover(pygame.mouse.get_pos())
        back_to_main_menu_button.draw(screen)

        pygame.display.flip()
