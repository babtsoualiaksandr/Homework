import os
import json

from datetime import datetime, date, time, timezone
from dateutil.parser import parse
import copy
import pickle

from models import Feed, Item, ListFeeds


class LocalStorage():
    def __init__(self, path: str) -> None:
        self._path = os.path.abspath(path)
        if not os.path.isfile(self._path):
            with open(self._path, 'wb') as f:
                feed = Feed('', '', '')
                feeds = ListFeeds(list())
                feeds.feeds.append(feed)
                pickle.dump(feeds, f)

    def read_url(self, url: str, date_filter: str, limit: int = None) -> Feed:
        try:
            datetime.strptime(date_filter, '%Y%m%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be %Y%m%d")
        with open(self._path, 'rb') as f:
            feeds_storage = pickle.load(f)
            print(feeds_storage)

        def equal_date(item: Item) -> bool:
            dt = parse(item.date)
            dt_str = f'{dt.year}{dt.month}{dt.day}'
            if dt_str == date_filter:
                return True
            else:
                return False
        find_idx, find_in_storage = next(((idx, feed) for idx, feed in enumerate(
            feeds_storage.feeds) if feed.url == url), (None, None))

        if find_in_storage is not None:
            find_news_date = [item for item in find_in_storage.items if equal_date(item)]
            return Feed(find_in_storage.url, find_in_storage.feed_title, find_news_date[:limit])
        else:
            raise Exception(f'Is not news {url}')

    def read_all(self, filter_date: str, limit: int = None) -> ListFeeds:
        result = ListFeeds(list())
        with open(self._path, 'rb') as f:
            feeds_storage = pickle.load(f)
        for item_feed in feeds_storage.feeds:
            feed = self.read_url(item_feed.url, filter_date, limit)
            if len(feed.items) != 0:
                result.feeds.append(feed)
        if len(result.feeds) == 0:
            raise Exception(f'Is not news in {filter_date}')

        return result

    def append(self, rss_data: Feed):
        add_feed = copy.deepcopy(rss_data)
        with open(self._path, 'rb') as f:
            feeds_storage = pickle.load(f)
        find_idx, find_in_storage = next(((idx, feed) for idx, feed in enumerate(
            feeds_storage.feeds) if feed.url == add_feed.url), (None, None))
        if find_in_storage is not None:
            find_in_storage.items.extend(add_feed.items)
            seen = set()
            unique_items = [seen.add(item.item_title)
                            or item for item in find_in_storage.items if item.item_title not in seen]
            find_in_storage = Feed(find_in_storage.url, find_in_storage.feed_title, unique_items)
            feeds_storage.feeds[find_idx] = find_in_storage
        else:
            feeds_storage.feeds.append(add_feed)
        with open(self._path, 'wb') as f:
            pickle.dump(feeds_storage, f)
