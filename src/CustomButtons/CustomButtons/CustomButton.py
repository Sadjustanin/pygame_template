import pygame
from pygame import Surface, SurfaceType
from pygame.rect import RectType, Rect

from src.MainSettings import font
from src.Sound.Main import play_sound


class CustomButton:
    def __init__(self, text: str | bytes | None, width: float | int, height: float | int,
                 pos: tuple[float, float] | tuple[int, int] | tuple[float, int] | tuple[int, float],
                 elevation: int = 10) -> None:

        # Core attributes
        self.pressed: bool = False
        self.elevation: int = elevation
        self.dynamic_elevation: int = elevation
        self.original_y_pos: float | int = pos[1]
        self.mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

        # top rectangle
        self.top_rect: Rect = pygame.Rect(pos, (width, height))
        self.top_color: str = "#475F77"

        # bottom rectangle
        self.bottom_rect: Rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color: str = "#354B5E"

        # text
        self.text_surf: Surface | SurfaceType = font.render(text, True, "#FFFFFF")
        self.text_rect: Rect | RectType = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen: Surface | SurfaceType) -> None:
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect: Rect | RectType = self.text_surf.get_rect(center=self.top_rect.center)
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        current_info = pygame.display.Info()
        current_width: int = current_info.current_w
        current_height: int = current_info.current_h

        pygame.draw.rect(pygame.transform.scale(screen, (current_width, current_height)), self.bottom_color,
                         self.bottom_rect, border_radius=50)
        pygame.draw.rect(pygame.transform.scale(screen, (current_width, current_height)), self.top_color, self.top_rect,
                         border_radius=50)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        if self.top_rect.collidepoint(self.mouse_pos):
            self.top_color = "#D74B4B"
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    play_sound()
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = "#475F77"
