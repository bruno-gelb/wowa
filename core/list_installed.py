import os

import yaml

from core.utils import get_metadata_path


def list_installed() -> None:
    metadata_path = get_metadata_path()

    if not os.path.exists(metadata_path):
        return

    with open(metadata_path, 'r') as f:
        metadata = yaml.load(f, Loader=yaml.FullLoader)
        for name, v in metadata.items():
            version = v['version']
            print(f'{name}=={version}')
