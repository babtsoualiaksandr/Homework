

from requests_html import HTMLSession
from requests_html import HTML
import pandas as pd
import requests
__all__ = {
    'Reader'
}


class Reader:
    def __init__(self, url):
        self.url = url

    def get_source(self):

        try:
            session = HTMLSession()
            response = session.get(self.url)
            return response

        except requests.exceptions.RequestException as e:
            print(e)

    def get_feed(self):

        response = self.get_source()

        df = pd.DataFrame(columns=['title', 'pubDate', 'guid', 'description'])

        with response as r:
            items = r.html.find("item", first=False)

            for item in items:

                title = item.find('title', first=True).text
                pubDate = item.find('pubDate', first=True).text
                guid = item.find('guid', first=True).text
                description = item.find('description', first=True).text

                row = {'title': title, 'pubDate': pubDate,
                       'guid': guid, 'description': description}
                df = df.append(row, ignore_index=True)

        return df

    
reader = Reader("https://practicaldatascience.co.uk/feed.xml")
feed = reader.get_feed()

reader = Reader("https://people.onliner.by/feed")
feed = reader.get_feed()
