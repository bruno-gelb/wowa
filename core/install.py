from core.index import index


def install(name: str, version: str) -> (str, str):
    installed_name, installed_version = name, version

    found = index.search(name, version)

    if not found:
        print(f'Not found.')

    installed_name = found['name']

    # todo actually install what we have found

    return installed_name, installed_version
