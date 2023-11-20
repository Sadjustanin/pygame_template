import pygame
from src.CustomButtons.CustomButtons.CustomButton import CustomButton
from src.Sound.Main import play_sound


class HostButton(CustomButton):
    def __init__(self, text: str | bytes | None, width: float | int, height: float | int,
                 pos: tuple[float, float] | tuple[int, int] | tuple[float, int] | tuple[int, float],
                 elevation: int = 10) -> None:

        # Core attributes
        super().__init__(text, width, height, pos, elevation)

    def check_click(self):
        self.mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
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
