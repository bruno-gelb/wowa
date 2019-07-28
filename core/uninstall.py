import os

import yaml

from core.utils import get_path_to_config


def uninstall(name_to_uninstall: str) -> None:
    config = get_path_to_config()

    found = False

    if os.path.exists(config):
        with open(config, 'r') as f:
            for name, v in yaml.load(f, Loader=yaml.FullLoader).items():
                if name_to_uninstall.lower() == name.lower():
                    found = True
                    break

    if not found:
        print(f'{name_to_uninstall} is not installed.')
        return

    # todo actually delete addon dirs, but we need to know them somehow

    print(f'Uninstalled {name}.')
