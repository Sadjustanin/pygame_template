from pygame.font import Font
from pygame_menu.widgets import TextInput, Button, Label, Frame
from screeninfo import get_monitors
import pygame
import pygame_menu
from pygame import Surface, SurfaceType
from pygame_menu import themes, Menu, Theme, BaseImage
from pygame_menu.examples.simple import start_the_game, set_difficulty

WIDTH, HEIGHT = 0, 0

for i in get_monitors():
    WIDTH = i.width
    HEIGHT = i.height


pygame.init()

auth_surface: Surface | SurfaceType = pygame.display.set_mode((WIDTH / 2, HEIGHT / 2))
main_surface: Surface | SurfaceType = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

image_path = "/home/void/PycharmProjects/pygame_template/assets/main_menu_background.png"
image_path_2 = "/home/void/PycharmProjects/pygame_template/assets/auth_menu_background.png"

my_image: BaseImage = pygame_menu.baseimage.BaseImage(image_path=image_path, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY, drawing_offset=(0, 0))
my_image_2: BaseImage = pygame_menu.baseimage.BaseImage(image_path=image_path_2, drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY, drawing_offset=(0, 0))

my_font: Font = pygame_menu.font.get_font(pygame_menu.font.FONT_MUNRO, 100)

my_theme_main_menu: Theme = Theme(background_color=my_image, widget_padding=25, widget_font=my_font, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)
my_theme_main_menu_2: Theme = Theme(background_color=my_image_2, widget_padding=25, widget_font=my_font, title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE)

def level_menu():
    main_menu._open(level)


main_menu: Menu = pygame_menu.Menu('', WIDTH, HEIGHT, theme=my_theme_main_menu)
main_menu.add.text_input("name", default="karamba")
main_menu.add.button("play", start_the_game)
main_menu.add.button("levels", level_menu)
main_menu.add.button("quit", pygame_menu.events.EXIT)

auth_menu: Menu = pygame_menu.Menu('', WIDTH, HEIGHT, theme=my_theme_main_menu_2)
login: TextInput = auth_menu.add.text_input("login: ")
password: TextInput = auth_menu.add.text_input("password: ")
check_data: Button = auth_menu.add.button("auth")
clock: Label = auth_menu.add.clock(font_size=25, font_name=pygame_menu.font.FONT_DIGITAL)
frame: Frame = auth_menu.add.frame_v(WIDTH / 2, HEIGHT / 2)
frame_title

level: Menu = pygame_menu.Menu("select a difficulty", WIDTH, HEIGHT, theme=themes.THEME_BLUE)
level.add.selector("Difficulty: ", [("Hard", 1), ("Easy", 2)], onchange=set_difficulty)

if __name__ == '__main__':
    auth_menu.mainloop(auth_surface)

    main_menu.mainloop(main_surface)
