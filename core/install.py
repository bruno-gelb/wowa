import os
import pathlib
import urllib
import zipfile
from typing import Union, Tuple

import click
import yaml

from core.index import index
from core.utils import (autodiscover_wow_addon_directory,
                        autodiscover_wow_version,
                        get_metadata_path,
                        AddonVersionState)


def is_installed(name: str) -> bool:
    metadata_path = get_metadata_path()
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r') as f:
            metadata = yaml.load(f, Loader=yaml.FullLoader)
            if name.lower() in [n.lower() for n in metadata]:
                return True
    return False


def install(name: str, version: str) -> None:
    if is_installed(name):
        click.echo(f'{name} is already installed.')
        return

    found = index.search(name, version)

    if found:
        installed_name = found['name']
        resolved = resolve(found)
        if resolved:
            installed_version, installed_state, url = resolved
            if url:
                downloaded = download(url)
                installed_dirs = unpack(downloaded)
                update_metadata(
                    installed_name,
                    installed_version,
                    installed_dirs,
                    installed_state
                )
                click.echo(click.style(f'Successfully installed {installed_name}=={installed_version}.', bold=True))


def resolve(entry: dict) -> Union[Tuple[str, AddonVersionState, str], None]:
    click.echo('Resolving addon version to install ..')

    wow_version = autodiscover_wow_version()
    click.echo(f'Your WoW version is {wow_version}.')

    for file in entry['latestFiles']:
        if not file['gameVersion'] or wow_version == file['gameVersion'][0]:
            click.echo(f'Therefore resolved {entry["name"]} version to compatible {file["displayName"]}.')
            if 'alpha' in file['displayName'].lower() or 'alpha' in file['fileName'].lower():
                state = AddonVersionState.ALPHA
            elif 'beta' in file['displayName'].lower() or 'beta' in file['fileName'].lower():
                state = AddonVersionState.BETA
            else:
                state = AddonVersionState.RELEASE
            return file['displayName'], state, file['downloadUrl']

    click.echo(click.style('Unable to resolve addon version for this WoW version.', fg='red'))


def download(addon_download_link: str) -> str:
    tmp_dir = os.path.join(os.environ['TEMP'], 'wowa')
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    archive_name = addon_download_link.split('/')[-1]
    file_path = os.path.join(tmp_dir, archive_name)
    if os.path.exists(file_path):
        click.echo(f'Found already downloaded file for {addon_download_link}.')
    else:
        click.echo(f'Downloading {addon_download_link} ..')
        urllib.request.urlretrieve(addon_download_link, file_path)
    click.echo(click.style('Done.', bold=True))
    return file_path


def unpack(path: str) -> list:
    addons_dir = autodiscover_wow_addon_directory()
    click.echo('Unpacking ' + click.style(path, underline=True)
               + ' to ' + click.style(addons_dir) + '..')

    unpacked_dirs = []
    with zipfile.ZipFile(path, 'r') as zip_ref:
        for path in zip_ref.namelist():
            p = pathlib.Path(path)
            unpacked_dirs.append(p.parts[0])
        unpacked_dirs = list(set(unpacked_dirs))
        zip_ref.extractall(addons_dir)

    click.echo(click.style('Done.', bold=True))
    return unpacked_dirs


def update_metadata(name: str, version: str,
                    dirs: list, state: AddonVersionState) -> None:
    metadata_path = get_metadata_path()

    metadata = {name: {
        'version': f'{version}',
        'dirs': dirs,
        'state': str(state)
    }}
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r') as f:
            metadata.update(yaml.load(f, Loader=yaml.FullLoader))

    with open(metadata_path, 'w') as f:
        yaml.dump(metadata, f, default_flow_style=False)
