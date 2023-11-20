import socket

client_socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
client_socket.connect(("localhost", 25565))

while True:

    client_socket.send("i wanna go right".encode())

    data: str = client_socket.recv(1024).decode()

    print(data)
