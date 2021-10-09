import sys
from src.local_storage import LocalStorage
from src.rss_reader import parse_args
from src.rss_reader import get_version
from src.parser_xml import read_describe, read_rss
import pytest
import pkg_resources
from unittest import mock
import pickle
from requests.models import Response
import json
import codecs


print(sys.path)


def test_parse_args():
    """Test parse args"""
    url = 'https://news.yahoo.com/rss/'
    args = parse_args([url, "--json"])
    assert args.json == True
    assert args.version == False
    assert args.verbose == False
    assert args.limit == None
    assert args.source == url
    args = parse_args([url, "--json", "--version"])
    assert args.json == True
    assert args.version == True
    assert args.verbose == False
    assert args.limit == None
    args = parse_args([url, "--limit", "100"])
    assert args.json == False
    assert args.version == False
    assert args.verbose == False
    assert args.limit == 100


def test_get_version():
    """Test get version script    """
    assert get_version() == f"Version { pkg_resources.require('rss_reader')[0].version}"


def test_read_rss():
    url = 'https://news.yahoo.com/rss/'
    result = read_rss(url, 1)
    assert result['Feed'] == result['Feed']
    assert len(result['Feed']) > 0


def test_local_storage():
    ls = LocalStorage('test.json')
    rss = ls.read_url('https://news.yahoo.com/rss/', '2021106', 1)
    assert isinstance(ls, LocalStorage)
    assert rss['Feed'] == "Yahoo News - Latest News & Headlines"


with open('doc.tree', 'rb') as f:
    doc = pickle.load(f)


@mock.patch('src.parser_xml.parse', return_value=doc, autospec=True)
def test_parse_xml(mock_parse):
    url = 'https://news.yahoo.com/rss/'
    assert read_rss(url, 1)['Feed'] == 'Yahoo News - Latest News & Headlines'
    assert read_rss(url, 4)['items'][3]['Title'] == "Germany puts 100-year-old on trial for Nazi crimes"



def mocked_request_get(*args, **kwargs):
    response_content = None
    with codecs.open('test_describe.html','r', "utf-8") as f:
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
    assert read_describe('mockurl') =='????'
