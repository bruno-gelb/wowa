import os
import urllib
import zipfile
from typing import Union

from core.index import index
from core.utils import autodiscover_wow_addon_directory, autodiscover_wow_version


def install(name: str, version: str) -> None:
    installed_name, installed_version = name, version

    found = index.search(name, version)

    if found:
        url = resolve(found)
        if url:
            downloaded = download(url)
            unpack(downloaded)

            installed_name = found['name']

            print(f'Successfully installed {installed_name}=={installed_version}. ')


def resolve(entry: dict) -> Union[str, None]:
    print('Resolving addon version to install ..')

    wow_version = autodiscover_wow_version()
    print(f'Your WoW version is {wow_version}.')

    for file in entry['latestFiles']:
        if not file['gameVersion'] or wow_version == file['gameVersion'][0]:
            print(f'Therefore resolved {entry["name"]} version to compatible {file["displayName"]}.')
            return file['downloadUrl']

    print('Unable to resolve addon version for this WoW version.')


def download(addon_download_link: str) -> str:
    print(f'Downloading {addon_download_link} ..')

    tmp_dir = os.path.join(os.environ['TEMP'], 'wowa')
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    archive_name = addon_download_link.split('/')[-1]
    urllib.request.urlretrieve(addon_download_link,
                               os.path.join(tmp_dir, archive_name))
    print(f'Done.')
    return os.path.join(tmp_dir, archive_name)


def unpack(path: str) -> None:
    addons_dir = autodiscover_wow_addon_directory()
    print(f'Unpacking {path} to {addons_dir} ..')

    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(addons_dir)

    print(f'Done.')
