import os

import yaml

from core.utils import get_metadata_path


def list_installed() -> list:
    metadata_path = get_metadata_path()

    installed = []
    if not os.path.exists(metadata_path):
        return installed

    with open(metadata_path, 'r') as f:
        metadata = yaml.load(f, Loader=yaml.FullLoader)
        for name, v in metadata.items():
            version = v['version']
            installed.append(name)
            print(f'{name}=={version}')

    return installed
