import sys
import os
from src.local_storage import LocalStorage
from src.rss_reader import format_output, parse_args
from src.rss_reader import get_version
from src.parser_xml import read_describe, read_rss
from src.service_api import get_news_from_url
import pytest
import pkg_resources
from unittest import mock
import pickle
import json
import codecs

from src.models import Feed, Item, ListFeeds
from io import StringIO

from src.utilits import Colors, get_rows_from_text


print(sys.path)


@pytest.fixture
def get_feed():
    item = Item(item_title='item_title', date='date', link='link', description='description', links=['links'])
    return Feed(url='url', feed_title='feed_title',
                items=[item])


def test_format_output(get_feed):
    with mock.patch('sys.stdout', new=StringIO()) as fake_out:
        format_output(get_feed, json_out=False, colors=Colors(True))
        assert fake_out.getvalue()[:20] == """\x1b[31mFeed: feed_titl"""[:20]


def test_local_storage():
    ls = LocalStorage('test.data')
    assert isinstance(ls, LocalStorage)


def test_models():
    list_news = ListFeeds(list[Feed('url', 'title', [Item('title', '2021108', '', ' ', list())])])
    assert isinstance(list_news, ListFeeds)


def test_parse_args():
    """Test parse args"""
    url = 'https://news.yahoo.com/rss/'
    args = parse_args([url, "--json"])
    assert args.json
    assert not args.version
    assert not args.verbose
    args = parse_args([url, "--json", "--version"])
    assert args.json
    assert args.version
    assert not args.verbose
    args = parse_args([url, "--limit", "100"])
    assert not args.json
    assert not args.version
    assert not args.verbose
    assert args.limit == 100


def test_get_version():
    """Test get version script    """
    assert get_version() == f"Version { pkg_resources.require('rss_reader')[0].version}"


def test_read_rss():
    url = 'https://news.yahoo.com/rss/'
    result = read_rss(url, 1)
    print(result.feed_title)
    assert result.feed_title == result.feed_title
    assert len(result.items) == 1


def get_doc():
    is_here = os.path.split(__file__)
    path_to_file = os.path.join(os.path.abspath(os.path.join(is_here[0], os.pardir)), 'src', 'static', 'UN_News.data')
    print(is_here, '*'*12)

    with open(path_to_file, 'rb') as f:
        doc = pickle.load(f)
    return doc


doc = get_doc()


@mock.patch('src.parser_xml.parse', return_value=doc, autospec=True)
def test_parse_xml(mock_parse):
    url = 'https://news.yahoo.com/rss/'
    assert read_rss(url, 1).feed_title == 'UN News'


def test_get_rows_from_text():
    assert len(get_rows_from_text('qferferqf refqerqevqerv vqer', 4)) == 7


links = ["link1", "link2"]
news_one = Item(item_title="One", date="1 04 2021", link="https://epam.rss.comm", description="About One", links=links)
news_two = Item(item_title="Two", date="1 04 2021", link="https://epam.rss.comm", description="About two", links=links)
items = [news_one, news_two]
fake_feed = Feed(url='https://epam.rss.comm', feed_title="News fake from EPAM", items=items)


@mock.patch('src.service_api.read_rss', return_value=fake_feed, autospec=True)
def test_service_api(mock_read_rss):
    result = get_news_from_url(url='https://www.un.org/press/en/feed', limit=100, format='json')
    assert isinstance(result, Feed)
    assert result.feed_title == "News fake from EPAM"
    assert len(result.items) == 2
    result = get_news_from_url(url='https://www.un.org/press/en/feed', limit=100, format='pdf')
    assert result.feed_title == "News fake from EPAM"
    assert os.path.exists('report.pdf')
    result = get_news_from_url(url='https://www.un.org/press/en/feed', limit=100, format='html')
    assert len(result.items) == 2
    assert os.path.exists('report.html')

