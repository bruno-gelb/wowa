import os

import yaml

from core.utils import autodiscover_wow_addon_directory


def list_installed() -> None:
    wow_addon_directory = autodiscover_wow_addon_directory()
    yaml_path = os.path.join(wow_addon_directory, 'wowa.yaml')

    if not os.path.exists(yaml_path):
        return

    with open(yaml_path, 'r') as f:
        for name, v in yaml.load(f, Loader=yaml.FullLoader).items():
            version = v['version']
            print(f'{name}{version}')
