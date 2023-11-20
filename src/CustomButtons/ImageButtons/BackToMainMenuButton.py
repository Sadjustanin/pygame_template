import sys

import pygame
from pygame.event import Event
from pygame.locals import *

from src.CustomButtons.ImageButtons.ImageButton import ImageButton

pygame.init()
pygame.mixer.init()


class BackToMainMenuButton(ImageButton):
    def handle_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                from src.MainMenu import main_menu
                self.sound.play()
                main_menu()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pass
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
