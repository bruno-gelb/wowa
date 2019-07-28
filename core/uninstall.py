import os

import yaml

from core.utils import autodiscover_wow_addon_directory


def uninstall(name_to_uninstall: str) -> None:
    wow_addon_directory = autodiscover_wow_addon_directory()
    yaml_path = os.path.join(wow_addon_directory, 'wowa.yaml')

    found = False

    if os.path.exists(yaml_path):
        with open(yaml_path, 'r') as f:
            for name, v in yaml.load(f, Loader=yaml.FullLoader).items():
                if name_to_uninstall.lower() == name.lower():
                    found = True
                    break

    if not found:
        print(f'{name_to_uninstall} is not installed.')
        return

    # todo actually delete addon dirs, but we need to know them somehow

    print(f'Uninstalled {name}.')
