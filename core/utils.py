def parse_name_version(raw: str) -> (str, str):
    if '==' in raw:
        name, version = raw.split('==')
    else:
        name = raw
        version = 'latest'

    return name, version


def autodiscover_wow_version() -> str:
    return '8.2.0'


def autodiscover_wow_addon_directory() -> str:
    # todo this should depend on wow version / os
    return r'C:\Program Files (x86)\World of Warcraft\_retail_\Interface\AddOns'
