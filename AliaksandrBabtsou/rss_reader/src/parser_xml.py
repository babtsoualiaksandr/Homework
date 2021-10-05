from xml.dom import minidom
from html.parser import HTMLParser
import urllib.request
import requests
from log import log_decorator
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class RSSHTMLParser(HTMLParser):
    def __init__(self):
        self.check=None
        self.description ={}
        super().__init__()        

    def handle_starttag(self, tag, attrs):
        if tag =="h1":
            self.check = 'h1'
        if tag =="meta":
            self.check = 'meta content'
            if ('name','twitter:description') in attrs:
                _, self.description['description'] = attrs[1]

    def handle_data(self, data):
        if self.check =='h1':
            self.description['title'] = data
        self.check = None

    def close(self) -> None:
        self.result =[]
        return super().close()

@log_decorator
def read_describe(url: str)-> dict:
    parser = RSSHTMLParser()
    htm_from_url = requests.get(url).text
    htm_from_url = htm_from_url.replace('\n', '')
    parser.feed(htm_from_url)
    return parser.description



@log_decorator
def read_rss(url:str, limit:int=None, json_out: bool=False)-> dict:
    req = urllib.request.urlopen(url)
    if req.getcode()!=200:
        return
    rss_xml=req.read()
    dom = minidom.parseString(rss_xml)
    dom.normalize()
    dom.version
    with minidom.parseString(rss_xml) as dom:
        result = []
        res ={}
        rss = dom.getElementsByTagName('rss')
        version_rss = rss[0].getAttribute('version')
        res['version'] = version_rss
        title = dom.getElementsByTagName('title')[0].childNodes[0].nodeValue
        res['Feed'] = title
        result.append(res)
        items = dom.getElementsByTagName('item')

        limit = len(items) if limit is None else limit
        for i, item in enumerate(items):
            res={}
            if i== limit:
                break
            else:
                title_item = item.getElementsByTagName('title')[0].childNodes[0].nodeValue
                res['Title'] = title_item
                date_item = item.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue
                res['Date'] = date_item
                link_item = item.getElementsByTagName('link')[0].childNodes[0].nodeValue
                res['Link'] = link_item
                res['describe_link'] = read_describe(link_item)
                urls_links =[link_item]  
                

                for el in item.childNodes:
                    url_attribute = el.getAttribute('url')
                    if url_attribute != '':
                        urls_links.append(url_attribute)
                res['Links'] = urls_links

                result.append(res)
    return result if not json_out else json.dumps(result)

if __name__=='__main__':
    url = 'https://news.yahoo.com/rss/'
    print(read_rss(url,limit=10, json_out= True))


    
    
    
