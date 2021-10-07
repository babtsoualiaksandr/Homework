import os
import json

from datetime import datetime, date, time, timezone
from dateutil.parser import parse


class LocalStorage():
    def __init__(self, path: str) -> None:
        print(path)
        self._path = os.path.abspath(path)
        print(self._path)
        if not os.path.isfile(self._path):
            with open(self._path, 'w') as f:
                json.dump({"url": {"Feed": "", "items": []}}, f)

    def read_url(self, url: str, date_filter: str, limit: int = None) -> dict:
        try:
            datetime.strptime(date_filter, '%Y%m%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be %Y%m%d")
        with open(self._path, 'r') as f:
            data_read = json.load(f)

        def equal_date(item):
            dt = parse(item['Date'])
            dt_str = f'{dt.year}{dt.month}{dt.day}'
            if dt_str == date_filter:
                return True
            else:
                return False
        if url in data_read:
            items = list(filter(equal_date, data_read[url]['items']))
            if limit is not None:
                items = items[:limit]
            result = {'Feed': data_read[url]['Feed'], 'items': items}
            return result
        else:
            raise Exception(f'Is not news {url}')

    def read_all(self, filter_date: str, limit: int = None) -> dict:
        result = []
        with open(self._path, 'r') as f:
            data_read = json.load(f)
        for url in data_read:
            feed = self.read_url(url, filter_date, limit)
            if feed['Feed'] != '':
                result.append(feed)
        return result

    def append(self, rss_data: dict):
        data_append = {}
        key_url = rss_data['url']
        data_append[key_url] = {'Feed': rss_data['Feed'], 'items': rss_data['items']}

        data_append[key_url]['items'].extend(data_append[key_url]['items'])
        list_items = data_append[key_url]['items']

        with open(self._path, 'r') as f:
            data_read = json.load(f)
        if key_url in data_read:
            data_append[key_url]['items'].extend(data_read[key_url]['items'])
            iniqui_items = list({v['Title']: v for v in list_items}.values())
            data_read[key_url]['items'] = iniqui_items

        else:
            data_read[key_url] = data_append[key_url]

        with open(self._path, 'w') as f:
            json.dump(data_read, f, ensure_ascii=False)
