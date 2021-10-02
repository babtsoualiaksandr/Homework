import sys 
sys.path.append('..')
from rss_reader.rss_reader import parse_args
from rss_reader.rss_reader import get_version
import pytest
import pkg_resources


def test_parse_args():
    """Test parse args"""
    url = 'https://news.yahoo.com/rss/'
    args= parse_args([url,"--json"])    
    assert args.json == True
    assert args.version == False
    assert args.verbose == False
    assert args.limit == None
    assert args.source == [url]
    args= parse_args([url,"--json", "--version"])    
    assert args.json == True
    assert args.version == True
    assert args.verbose == False
    assert args.limit == None
    args= parse_args([url,"--limit", "100"])    
    assert args.json == False
    assert args.version == False
    assert args.verbose == False
    assert args.limit == 100


def test_get_version():
    """Test get version script    """
    assert get_version() == f"Version { pkg_resources.require('rss_reader')[0].version}"








