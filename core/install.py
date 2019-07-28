import os
import urllib
import zipfile
from typing import Union, Tuple

import yaml

from core.index import index
from core.utils import autodiscover_wow_addon_directory, autodiscover_wow_version


def install(name: str, version: str) -> None:
    found = index.search(name, version)

    if found:
        installed_name = found['name']
        resolved = resolve(found)
        if resolved:
            installed_version, url = resolved
            if url:
                downloaded = download(url)
                unpack(downloaded)
                remember(installed_name, f'=={installed_version}')
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


def unpack(path: str) -> None:
    addons_dir = autodiscover_wow_addon_directory()
    print(f'Unpacking {path} to {addons_dir} ..')

    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(addons_dir)

    print(f'Done.')


def remember(name: str, version: str) -> None:
    wow_addon_directory = autodiscover_wow_addon_directory()
    yaml_path = os.path.join(wow_addon_directory, 'wowa.yaml')

    data = {name: {'version': version}}
    if os.path.exists(yaml_path):
        with open(yaml_path, 'r') as f:
            data.update(yaml.load(f))

    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
