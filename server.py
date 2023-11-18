import os.path
import socket


def create_file(title: str = "unnamed", extension: str = "txt", make_duplicate: bool = True,
                duplicate_number: int = 1000) -> None:
    if os.path.exists(f"{title}.{extension}"):

        class DuplicateRestriction(Exception):
            def __init__(self, *args):
                super().__init__(args)

            def __str__(self):
                return "Duplication restriction exception"

        class DuplicateDisabled(DuplicateRestriction):
            def __init__(self, *args):
                super().__init__(args)

            def __str__(self):
                return "Duplication disabled"

        class DuplicateLimitation(DuplicateRestriction):
            def __init__(self, f, *args):
                super().__init__(args)
                self.f = f

            def __str__(self):
                return f"Only {self.f} duplicates can exist"

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


create_file("karamba", "json", False)
