import socket

import pygame
from pygame import SurfaceType, Surface

from src.Enums import Colors

pygame.init()

INITIAL_WEIGHT: int = 1920
INITIAL_HEIGHT: int = 1080

client_socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
client_socket.connect(("10.242.179.35", 25565))

pygame.init()
screen: Surface | SurfaceType = pygame.display.set_mode((INITIAL_WEIGHT / 2, INITIAL_HEIGHT / 2))
pygame.display.set_caption("agario")

is_0: bool = True

while is_0:

    current_info = pygame.display.Info()
    current_width: int = current_info.current_w
    current_height: int = current_info.current_h

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_0 = False

    if pygame.mouse.get_focused():
        x, y = pygame.mouse.get_pos()
        vector: tuple[int, int] = (x - current_width // 2, y - current_height // 2)
        print(vector)

    client_socket.send("i wanna go right".encode())

    data: str = client_socket.recv(1024).decode()

    screen.fill(Colors.BLACK.value)
    pygame.draw.circle(screen, Colors.GREEN.value, (current_width // 2, current_height // 2), 50)
    pygame.display.update()

else:
    pygame.quit()
