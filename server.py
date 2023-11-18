import os.path
import json
import socket


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
                **kwargs: any) -> None:
    match case:
        case 1:
            with open(f"{title}.{extension}", literal) as file:
                json.dump(kwargs, file, indent=kwargs.keys().__len__())
        case 2:
            with open(f"{title}.{extension}", literal) as file:
                file.truncate()
        case _:
            pass


# create_file("server", "json", False)
modify_file("server", "json", ip="localhost", port=25565)
