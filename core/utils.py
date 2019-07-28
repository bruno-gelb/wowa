def parse_name_version(raw: str) -> (str, str):
    if '==' in raw:
        name, version = raw.split('==')
    else:
        name = raw
        version = 'latest'

    return name, version
