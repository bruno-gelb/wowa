import os

import yaml

from core.utils import get_path_to_metadata


def list_installed() -> None:
    metadata = get_path_to_metadata()

    if not os.path.exists(metadata):
        return

    with open(metadata, 'r') as f:
        for name, v in yaml.load(f, Loader=yaml.FullLoader).items():
            version = v['version']
            print(f'{name}{version}')
