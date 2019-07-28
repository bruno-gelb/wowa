import os

import yaml

from core.utils import get_path_to_config


def list_installed() -> None:
    config = get_path_to_config()

    if not os.path.exists(config):
        return

    with open(config, 'r') as f:
        for name, v in yaml.load(f, Loader=yaml.FullLoader).items():
            version = v['version']
            print(f'{name}{version}')
