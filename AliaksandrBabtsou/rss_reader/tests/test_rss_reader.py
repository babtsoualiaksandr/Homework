import sys 
from src.rss_reader import parse_args
from src.rss_reader import get_version
from src.parser_xml import read_rss
import pytest
import pkg_resources

print(sys.path)



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

def test_read_rss():
    url = 'https://news.yahoo.com/rss/'
    result = read_rss(url,1)
    assert result[0]['Feed'] == 'Yahoo News - Latest News & Headlines'
    assert result[0][0]['Title'] == 'Man accused in co-worker deaths tells deputies he was raped'
    assert result[0][0]['Link'] == 'https://news.yahoo.com/man-accused-co-worker-deaths-193312526.html'
    assert result[0][0]['Date'] == '2021-10-04T19:33:12Z'

"""
Feed: Yahoo News - Latest News & Headlines

Title: Nestor heads into Georgia after tornados damage Florida
Date: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html

[image 2: Nestor heads into Georgia after tornados damage Florida][2]Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged
homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve
off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its
march across a swath of the U.S. Southeast.


Links:
[1]: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html (link)
[2]: http://l2.yimg.com/uu/api/res/1.2/Liyq2kH4HqlYHaS5BmZWpw--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media.zenfs.com/en/ap.org/5ecc06358726cabef94585f99050f4f0 (image)
"""
