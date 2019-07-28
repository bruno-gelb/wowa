import os
import shutil

import yaml

from core.utils import get_path_to_metadata, autodiscover_wow_addon_directory


def uninstall(name_to_uninstall: str) -> None:
    wow_addon_directory = autodiscover_wow_addon_directory()
    metadata = get_path_to_metadata()

    found = False

    if os.path.exists(metadata):
        with open(metadata, 'r') as f:
            for name, v in yaml.load(f, Loader=yaml.FullLoader).items():
                if name_to_uninstall.lower() == name.lower():
                    found = True
                    name_to_uninstall = name
                    break

    if not found:
        print(f'{name_to_uninstall} is not installed.')
        return

    for dir_to_remove in v['dirs']:
        print(f'Deleting {dir_to_remove} ..')
        shutil.rmtree(os.path.join(wow_addon_directory, dir_to_remove))

    with open(metadata, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    data.pop(name_to_uninstall)
    with open(metadata, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

    print(f'Uninstalled {name}.')
