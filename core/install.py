import os
import pathlib
import urllib
import zipfile
from typing import Union, Tuple

import yaml

from core.index import index
from core.utils import autodiscover_wow_addon_directory, autodiscover_wow_version, get_path_to_metadata


def install(name: str, version: str) -> None:
    found = index.search(name, version)

    if found:
        installed_name = found['name']
        # todo check if it's already installed
        resolved = resolve(found)
        if resolved:
            installed_version, url = resolved
            if url:
                downloaded = download(url)
                installed_dirs = unpack(downloaded)
                store_install_metadata(
                    installed_name,
                    f'=={installed_version}',
                    installed_dirs
                )
                print(f'Successfully installed {installed_name}=={installed_version}. ')


def resolve(entry: dict) -> Union[Tuple[str, str], None]:
    print('Resolving addon version to install ..')

    wow_version = autodiscover_wow_version()
    print(f'Your WoW version is {wow_version}.')

    for file in entry['latestFiles']:
        if not file['gameVersion'] or wow_version == file['gameVersion'][0]:
            print(f'Therefore resolved {entry["name"]} version to compatible {file["displayName"]}.')
            return file['displayName'], file['downloadUrl']

    print('Unable to resolve addon version for this WoW version.')


def download(addon_download_link: str) -> str:
    tmp_dir = os.path.join(os.environ['TEMP'], 'wowa')
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    archive_name = addon_download_link.split('/')[-1]
    file_path = os.path.join(tmp_dir, archive_name)
    if os.path.exists(file_path):
        print(f'Found already downloaded file for {addon_download_link}.')
    else:
        print(f'Downloading {addon_download_link} ..')
        urllib.request.urlretrieve(addon_download_link, file_path)
    print(f'Done.')
    return file_path


def unpack(path: str) -> list:
    addons_dir = autodiscover_wow_addon_directory()
    print(f'Unpacking {path} to {addons_dir} ..')

    unpacked_dirs = []
    with zipfile.ZipFile(path, 'r') as zip_ref:
        for path in zip_ref.namelist():
            p = pathlib.Path(path)
            unpacked_dirs.append(p.parts[0])
        unpacked_dirs = list(set(unpacked_dirs))
        zip_ref.extractall(addons_dir)

    print(f'Done.')
    return unpacked_dirs


def store_install_metadata(name: str, version: str, dirs: list) -> None:
    metadata = get_path_to_metadata()

    data = {name: {
        'version': version,
        'dirs': dirs,
        'state': None  # todo: 'alpha', 'beta', 'release'
    }}
    if os.path.exists(metadata):
        with open(metadata, 'r') as f:
            data.update(yaml.load(f, Loader=yaml.FullLoader))

    with open(metadata, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
