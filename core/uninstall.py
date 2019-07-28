import os
import shutil

import click
import yaml

from core.utils import get_metadata_path, autodiscover_wow_addon_directory


def uninstall(name_to_uninstall: str) -> None:
    wow_addon_directory = autodiscover_wow_addon_directory()
    metadata_path = get_metadata_path()

    found = False

    if os.path.exists(metadata_path):
        with open(metadata_path, 'r') as f:
            for name, v in yaml.load(f, Loader=yaml.FullLoader).items():
                if name_to_uninstall.lower() == name.lower():
                    found = True
                    name_to_uninstall = name
                    break

    if not found:
        click.echo(f'{name_to_uninstall} is not installed.')
        return

    for dir_to_remove in v['dirs']:
        click.echo(f'Deleting {os.path.join(wow_addon_directory, dir_to_remove)} ..')
        shutil.rmtree(os.path.join(wow_addon_directory, dir_to_remove))

    with open(metadata_path, 'r') as f:
        metadata = yaml.load(f, Loader=yaml.FullLoader)
    metadata.pop(name_to_uninstall)
    with open(metadata_path, 'w') as f:
        yaml.dump(metadata, f, default_flow_style=False)

    click.echo(f'Uninstalled {name}.')
