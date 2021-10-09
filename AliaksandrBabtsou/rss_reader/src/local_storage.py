import os
import json

from datetime import datetime, date, time, timezone
from dateutil.parser import parse
import copy
import pickle

from models import Feed, ListFeeds

class LocalStorage():
    def __init__(self, path: str) -> None:
        self._path = os.path.abspath(path)
        if not os.path.isfile(self._path):
            with open(self._path, 'wb') as f:
                feeds =[]
                feed = Feed('','','')
                feeds.append(feed)
                pickle.dump(feeds,f)

    def read_url(self, url: str, date_filter: str, limit: int = None) -> Feed:
        try:
            datetime.strptime(date_filter, '%Y%m%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be %Y%m%d")
        with open(self._path, 'rb') as f:
            feeds_storage = pickle.load(f)

        def equal_date(item):
            dt = parse(item.Date)
            dt_str = f'{dt.year}{dt.month}{dt.day}'
            if dt_str == date_filter:
                return True
            else:
                return False
        find_idx, find_in_storage = next(((idx, feed) for idx, feed in enumerate(feeds_storage) if feed.url == url), (None, None))
        
        if find_in_storage is not None:
            find_news_date = [item for item in find_in_storage.items if equal_date(item)]
            return Feed(find_in_storage.url, find_in_storage.Feed, find_news_date[:limit])
        else:
            raise Exception(f'Is not news {url}')

    def read_all(self, filter_date: str, limit: int = None) -> ListFeeds:
        result = ListFeeds(list())
        with open(self._path, 'rb') as f:
            feeds_storage = pickle.load(f)
        for item_feed in feeds_storage:
            feed = self.read_url(item_feed.url, filter_date, limit)
            if len(feed.items) != 0:
                result.Feeds.append(feed)
        if len(result.Feeds) == 0:
                raise Exception(f'Is not news in {filter_date}')

        return result

    def append(self, rss_data: Feed):
        add_feed = copy.deepcopy(rss_data)
        with open(self._path, 'rb') as f:
            feeds_storage =  pickle.load(f)
        find_idx, find_in_storage = next(((idx, feed) for idx, feed in enumerate(feeds_storage) if feed.url == add_feed.url), (None, None))
        if find_in_storage is not None:
            find_in_storage.items.extend(add_feed.items)
            seen = set()            
            unique_items = [seen.add(item.Title) or item for item in find_in_storage.items if item.Title not in seen]
            find_in_storage = Feed(find_in_storage.url, find_in_storage.Feed, unique_items)
            feeds_storage[find_idx] = find_in_storage
        else:
            feeds_storage.append(add_feed)
        with open(self._path, 'wb') as f:
            pickle.dump(feeds_storage,f)


