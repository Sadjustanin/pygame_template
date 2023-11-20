import os

import pygame
from pygame.mixer import Sound

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
pygame.mixer.init()


button_click_sound: Sound = pygame.mixer.Sound("../../assets/sounds/button_click_sound.mp3")
background_music: Sound = pygame.mixer.Sound("../../assets/sounds/background_music.mp3")
background_music.play(1)
background_music.set_volume(0.1)


def play_sound(sound: Sound = button_click_sound):
    pygame.mixer.Sound.play(sound)


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def stop():
    pygame.mixer.music.stop()
