import os
from enum import Enum


def parse_name_version(raw: str) -> (str, str):
    # todo this should respect things like '<', '<=', etc.
    if '==' in raw:
        name, version = raw.split('==')
    else:
        name = raw
        version = 'latest'

    return name, version


def autodiscover_wow_version() -> str:
    # todo this should depend on wow version / os
    return '8.2.0'


def autodiscover_wow_addon_directory() -> str:
    # todo this should depend on wow version / os
    return r'C:\Program Files (x86)\World of Warcraft\_retail_\Interface\AddOns'


def get_metadata_path() -> str:
    wow_addon_directory = autodiscover_wow_addon_directory()
    return os.path.join(wow_addon_directory, 'wowa_metadata.yaml')


class AddonVersionState(Enum):
    ALPHA = 1
    BETA = 2
    RELEASE = 3
