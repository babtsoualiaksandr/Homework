import sys
from src.local_storage import LocalStorage
from src.rss_reader import format_output, parse_args
from src.rss_reader import get_version
from src.parser_xml import read_describe, read_rss
import pytest
import pkg_resources
from unittest import mock
import pickle
from requests.models import Response
import json
import codecs

from models import Feed, Item, ListFeeds
from io import StringIO


print(sys.path)


@pytest.fixture
def get_feed():
    item = Item(item_title='item_title', date='date', link='link', description='description', links=['links'])
    return Feed(url='url', feed_title='feed_title',
                items=[item])


def test_format_output(get_feed):
    with mock.patch('sys.stdout', new=StringIO()) as fake_out:
        format_output(get_feed, json_out=False)
        assert fake_out.getvalue()[:20] == """\x1b[91mFeed: feed_titl"""[:20]


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
    assert args.version
    assert args.verbose
    assert args.limit
    assert args.source
    args = parse_args([url, "--json", "--version"])
    assert args.json
    assert args.version
    assert args.verbose
    assert isinstance(args.limit, None)
    args = parse_args([url, "--limit", "100"])
    assert args.json
    assert args.version
    assert args.verbose
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


with open('doc.tree', 'rb') as f:
    doc = pickle.load(f)


@mock.patch('src.parser_xml.parse', return_value=doc, autospec=True)
def test_parse_xml(mock_parse):
    url = 'https://news.yahoo.com/rss/'
    assert read_rss(url, 1).feed_title == 'Yahoo News - Latest News & Headlines'


def mocked_request_get(*args, **kwargs):
    response_content = None
    with codecs.open('test_describe.html', 'r', "utf-8") as f:
        html_text = f.read()
    html_text = html_text.replace('\n', '')
    request_url = kwargs.get('url', None)
    response_content = json.dumps(html_text)
    response = Response()
    response.status_code = 200
    response._content = str.encode(response_content)
    return response


@mock.patch('src.parser_xml.requests.get', side_effect=mocked_request_get)
def test_read_describe(mock_get):
    assert read_describe('mockurl') == {}
