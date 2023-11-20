import os
import json
import pygame

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def load_existing_save(savefile) -> any:
    with open(os.path.join(savefile), 'r+') as file:
        controls: any = json.load(file)
    return controls


def write_save(data) -> any:
    with open(os.path.join(os.getcwd(), 'save.json'), 'w') as file:
        json.dump(data, file)


def load_save() -> any:
    try:
        # Save is loaded
        save: any = load_existing_save('save.json')
    except:
        # No save file, so create one
        save: dict[str, int | dict[str, dict[str, int] | dict[str, int]]] = create_save()
        write_save(save)
    return save


def create_save() -> any:
    new_save: dict = {
        "controls": {
            "0": {"Left": pygame.K_a, "Right": pygame.K_d, "Up": pygame.K_w, "Down": pygame.K_s,
                  "Start": pygame.K_RETURN, "Action1": pygame.K_KP_ENTER},
            "1": {"Left": pygame.K_a, "Right": pygame.K_d, "Up": pygame.K_w, "Down": pygame.K_s,
                  "Start": pygame.K_RETURN, "Action1": pygame.K_KP_ENTER}
        },
        "current_profile": 0
    }

    return new_save


def reset_keys(actions) -> any:
    for action in actions:
        actions[action] = False
    return actions
