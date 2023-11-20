import pygame
from pygame.event import Event

from src.CustomButtons.ImageButtons.ImageButton import ImageButton

pygame.init()
pygame.mixer.init()


class AudioSliderButton(ImageButton):
    def handle_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
