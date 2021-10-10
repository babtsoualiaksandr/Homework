from xml.dom import minidom
from html.parser import HTMLParser
import requests
from log import log_decorator
import json
import ssl
from urllib.request import urlopen, Request
from xml.etree.ElementTree import parse

from models import Feed, Item


ssl._create_default_https_context = ssl._create_unverified_context


class RSSHTMLParser(HTMLParser):
    def __init__(self):
        self.check = None
        self.description = {}
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "h1":
            self.check = 'h1'
        if tag == "meta":
            self.check = 'meta content'
            if ('name', 'twitter:description') in attrs:
                _, self.description['description'] = attrs[1]

    def handle_data(self, data):
        if self.check == 'h1':
            self.description['title'] = data
        self.check = None

    def close(self) -> None:
        self.result = []
        return super().close()


@log_decorator
def read_describe(url: str) -> dict:
    parser = RSSHTMLParser()
    headers = {
        'User-Agent': """Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk)
         AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1"""}
    req = requests.get(url, headers=headers)
    if req.status_code != 200:
        return None
    htm_from_url = req.text
    htm_from_url = htm_from_url.replace('\n', '')
    parser.feed(htm_from_url)
    return parser.description


@log_decorator
def read_rss(url: str, limit: int = None) -> Feed:
    u = urlopen(url)
    doc = parse(u)
    items = []

    for idx, item in enumerate(doc.iterfind('channel/item')):
        res = {}
        urls = []
        res['Title'] = item.find('title').text
        res['Date'] = item.find('pubDate').text
        res['Link'] = item.find('link').text
        res['describe_link'] = read_describe(res['Link'])
        for el in item:
            if 'url' in el.attrib:
                urls.append(el.attrib['url'])
        res['Links'] = urls

        items.append(Item(res['Title'], res['Date'], res['Link'], res['describe_link'], res['Links']))
        if limit is not None:
            if idx == limit-1:
                break
    result = Feed(url, doc.find('channel').find('title').text, items)
    return result


if __name__ == '__main__':
    pass
