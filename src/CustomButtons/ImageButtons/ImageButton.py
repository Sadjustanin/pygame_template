import pygame
from pygame import Surface, SurfaceType
from pygame.event import Event
from pygame.font import Font
from pygame.mixer import Sound
from pygame.rect import RectType, Rect

from src.Enums import Colors

pygame.init()
pygame.mixer.init()


class ImageButton:
    def __init__(self, x: float | int, y: float | int, width: float | int, height: float | int, text: str | bytes,
                 image_path: str | bytes, hover_image_path: str | bytes = None, sound_path: str | bytes = None):
        self.text_surface: Surface | SurfaceType | None = None
        self.text_rect: Rect | RectType | None = None
        self.current_image: Surface | SurfaceType | None = None
        self.font: Font | None = None
        self.x: float | int = x
        self.y: float | int = y
        self.width: float | int = width
        self.height: float | int = height
        self.text: str | bytes = text

        self.image: Surface | SurfaceType = pygame.transform.scale(pygame.image.load(image_path), (width, height))
        self.hover_image: Surface | SurfaceType = self.image

        if hover_image_path:
            self.hover_image: Surface | SurfaceType = pygame.transform.scale(pygame.image.load(hover_image_path),
                                                                             (width, height))
        self.rect: Rect | RectType = self.image.get_rect(topleft=(x, y))

        if sound_path:
            self.sound: Sound = pygame.mixer.Sound(sound_path)
        self.is_hovered: bool = False

    def draw(self, screen: Surface | SurfaceType):
        self.current_image: Surface | SurfaceType = self.hover_image if self.is_hovered else self.image
        screen.blit(self.current_image, self.rect.topleft)

        self.font: Font = pygame.font.Font(None, 36)
        self.text_surface: Surface | SurfaceType = self.font.render(self.text, True, Colors.BLACK.value)
        self.text_rect: Rect | RectType = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, self.text_rect)

    def check_hover(self, mouse_pos: tuple[int, float] | tuple[float, int] | tuple[float, float] | tuple[int, int]):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
