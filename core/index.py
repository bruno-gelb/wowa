import json
from datetime import datetime
from time import strptime, mktime

import requests

from core.settings import WOW_TWITCH_ID, WOW_VERSION, INDEX_STALE_IN_MINUTES, PAGE_SIZE, INDEX_PATH


class Index(object):
    def __init__(self) -> None:
        self.data = {
            'built_on': f'{datetime.utcnow()}',
            'addons': []
        }
        self.date_format = '%Y-%m-%d %H:%M:%S.%f'

    @property
    def needs_to_be_rebuilt(self) -> bool:
        try:
            with open(INDEX_PATH, 'r') as f:
                read = json.load(f)
        except FileNotFoundError:
            print(f'Index is absent.')
            return True
        else:
            diff = mktime(strptime(self.data['built_on'], self.date_format)) - \
                   mktime(strptime(read['built_on'], self.date_format))
            if diff >= INDEX_STALE_IN_MINUTES * 60:
                print(f'Index is stale ({diff / 60} min old).')
                return True
        return False

    def build(self) -> None:
        print('Building index ..')

        url = 'https://addons-ecs.forgesvc.net/api/v2/addon/search'

        params = {
            'gameId': WOW_TWITCH_ID,
            'gameVersion': WOW_VERSION,
            'pageSize': PAGE_SIZE,
            'sort': 0
        }
        page = 0
        while True:
            params['index'] = page * PAGE_SIZE
            response = requests.get(url, params=params)
            fetched = json.loads(response.text)
            if not fetched:
                break
            print(f'Found {len(fetched)} entities on page {page}, continuing ..')
            self.data['addons'] += fetched
            page += 1

        self.data['built_on'] = f'{datetime.utcnow()}'
        with open(INDEX_PATH, 'w') as f:
            json.dump(self.data, f)

        amount = len(self.data['addons'])
        print(f'Index built, {amount} addons found for this WoW version.')

    def read(self, index_file: str) -> None:
        with open(index_file, 'r') as f:
            self.data['addons'] = json.load(f)['addons']

    def search(self, name: str, version: str) -> dict:
        if self.needs_to_be_rebuilt:
            self.build()

        self.read(INDEX_PATH)

        print(f'Searching for {name}=={version} ..')

        for entry in self.data['addons']:
            if name.lower() == entry['name'].lower():
                found = entry

        return found


index = Index()
