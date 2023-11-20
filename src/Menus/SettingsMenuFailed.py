import pygame
import pygame_menu as pm
from pygame.font import Font
from pygame_menu import BaseImage, Theme, Menu

from src.Enums import Colors
from src.MainSettings import WIDTH, HEIGHT

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)


def main():
    resolution = [("1920x1080", "1920x1080"),
                  ("1280x720", "1280x720"),
                  ("640x480", "640x480"), ]

    def print_settings():
        print("\n\n")
        settings_data = main_menu.get_input_data()

        for key in settings_data.keys():
            print(f"{key}\t:\t{settings_data[key]}")

    image_path = "../../assets/images/main_menu_background.png"

    my_image: BaseImage = pm.baseimage.BaseImage(image_path=image_path,
                                                 drawing_mode=pm.baseimage.IMAGE_MODE_REPEAT_XY,
                                                 drawing_offset=(0, 0))

    my_font: Font = pm.font.get_font(pm.font.FONT_MUNRO, 50)

    my_theme_main_menu: Theme = Theme(background_color=my_image, widget_padding=25, widget_font=my_font,
                                      title_bar_style=pm.widgets.MENUBAR_STYLE_NONE)

    main_menu: Menu = pm.Menu('', WIDTH, HEIGHT, theme=my_theme_main_menu)

    # main_menu.theme.widget_alignment = pm.locals.ALIGN_CENTER
    #
    # main_menu.add.button(title="Settings", action=settings,
    #                      font_color=Colors.WHITE.value, background_color=Colors.GREEN.value)
    #
    # main_menu.add.label(title="")
    #
    # main_menu.add.button(title="Exit", action=pm.events.EXIT,
    #                      font_color=Colors.WHITE.value, background_color=Colors.RED.value)

    main_menu.theme.widget_font_size = 25
    main_menu.theme.widget_font_color = Colors.BLACK.value
    main_menu.theme.widget_alignment = pm.locals.ALIGN_LEFT

    main_menu.add.dropselect_multiple(title="Window Resolution", items=resolution,
                                      dropselect_multiple_id="Resolution",
                                      open_middle=True, max_selected=1,
                                      selection_box_height=6)

    main_menu.add.toggle_switch(
        title="Music", default=True,
        toggleswitch_id="/home/void/PycharmProjects/pygame_template/assets/sounds/background_music.mp3")
    main_menu.add.toggle_switch(
        title="Sounds", default=False, toggleswitch_id="sound")

    # settings.add.range_slider(title="FOV", default=60, range_values=(
    #     50, 100), increment=1, value_format=lambda x: str(int(x)), rangeslider_id="fov")

    main_menu.add.clock(clock_format="%d-%m-%y %H:%M:%S",
                        title_format="Local Time : {0}")

    main_menu.add.button(title="Print Settings", action=print_settings,
                         font_color=Colors.WHITE.value, background_color=Colors.GREEN.value)
    main_menu.add.button(title="Restore Defaults", action=main_menu.reset_value,
                         font_color=Colors.WHITE.value, background_color=Colors.RED.value)
    main_menu.add.button(title="Return To Main Menu",
                         action=pm.events.BACK, align=pm.locals.ALIGN_CENTER)

    main_menu.mainloop(screen)


main()
