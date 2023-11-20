import json
import os.path
import socket
import time


def create_file(title: str = "unnamed", extension: str = "txt", make_duplicate: bool = True,
                duplicate_number: int = 1000) -> None:
    if os.path.exists(f"{title}.{extension}"):

        class DuplicateRestriction(Exception):
            def __init__(self, *args: any):
                super().__init__(args)

            def __str__(self):
                return "Duplication restriction exception"

        class DuplicateDisabled(DuplicateRestriction):
            def __init__(self, *args: any):
                super().__init__(args)

            def __str__(self):
                return "Duplication disabled"

        class DuplicateLimitation(DuplicateRestriction):
            def __init__(self, number: int, *args: any):
                super().__init__(args)
                self.number = number

            def __str__(self):
                return f"Only {self.number} duplicates can exist"

        if make_duplicate:
            for i in range(1, duplicate_number + 1):
                current_title: str = title + str(i)

                if not os.path.exists(f"{current_title}.{extension}"):
                    open(f"{current_title}.{extension}", 'x')
                    break
            else:
                raise DuplicateLimitation(duplicate_number)
        else:
            raise DuplicateDisabled()
    else:
        open(f"{title}.{extension}", 'x')


def modify_file(title: str = "unnamed", extension: str = "txt", literal: str = "r+", case: int = 1,
                **kwargs: any) -> any:
    match case:
        case 1:
            with open(f"{title}.{extension}", literal) as file:
                json.dump(kwargs, file, indent=kwargs.keys().__len__())
        case 2:
            with open(f"{title}.{extension}", literal) as file:
                file.truncate()
        case 3:
            with open(f"{title}.{extension}", literal) as file:
                return json.load(file)
        case _:
            pass


title: str = "server2"
extension: str = "json2"

# create_file(title, extension, False)
# modify_file(title, extension, ip="10.242.179.35", port=25565)
data: dict = modify_file(title, extension, case=3)

if __name__ == '__main__':

    main_socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    main_socket.bind((data.get("ip"), data.get("port")))
    main_socket.setblocking(False)
    main_socket.listen(4)
    players_sockets: list[socket] = list()

    # class Sock:
    #     def __init__(self, sock: socket) -> None:
    #         self.temp_data = sock
    #
    #     def __enter__(self):
    #         self.temp_data: str = self.temp_data.recv(1024).decode()
    #
    #         print(self.temp_data)
    #         return self
    #
    #     def __exit__(self, exc_type, exc_val, exc_tb) -> None:
    #         print("exiting context: ", self, exc_type, exc_val, exc_tb)

    while True:

        # checking whether anyone wants to join the game
        try:
            new_socket, address = main_socket.accept()
            new_socket.setblocking(False)
            players_sockets.append(new_socket)

            print(address, "connected")
        except BlockingIOError:
            print("none connected")

        # read player commands
        for sock in players_sockets:
            try:
                temp_data: str = sock.recv(1024).decode()

                print("received", temp_data)
            except BlockingIOError:
                pass
            except ConnectionResetError:
                pass

        # process commands

        # send a new playing field state
        for sock in players_sockets:
            try:
                sock.send("new game state".encode())
            except BlockingIOError and BrokenPipeError:
                print("player", players_sockets[players_sockets.index(sock)].getsockname(), "disconnected")

                players_sockets.remove(sock)
                sock.close()

        time.sleep(1)
