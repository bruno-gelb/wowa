import os

# index
INDEX_PATH = os.path.join(os.environ['TEMP'], 'wowa_index.json')
INDEX_STALE_IN_MINUTES = 24 * 60  # set to 0 if you want to rebuild index each time
WOW_TWITCH_ID = 1
PAGE_SIZE = 2000
