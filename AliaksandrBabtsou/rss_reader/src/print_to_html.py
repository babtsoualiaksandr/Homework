from models import Feed, ListFeeds
from datetime import datetime
import pkg_resources
from urllib.parse import urlparse
from log import log_decorator
import os
from pathlib import Path

from utilits import is_url_image

logo_rss = pkg_resources.resource_filename(__name__, 'static/rss_512.png')
logo_EPAM = pkg_resources.resource_filename(__name__, 'static/epam_.png')


def output_to(feed: Feed, f):
    """[Creating a page HTML from data parsing data RSS ]

    Args:
        feed (Feed): [data from RSS]
        f ([type]): [file where we write]
    """

    head = f'''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" \\ 
            rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"\\
                 crossorigin="anonymous">
            <title>EPAM Python Training 2021.09</title>
        </head>
        <body>           
            <a href="https://www.epam.com/" class="list-group-item list-group-item-action d-flex \\ 
            gap-3 py-3" aria-current="true">
                <img src="{logo_EPAM}" alt="logo_Epam" width="32" height="32" class="rounded-circle flex-shrink-0">
                <div class="d-flex gap-2 w-100 justify-content-between">
                <div>
                    <h6 class="mb-0">EPAM Python Training 2021.09</h6>
                    <p class="mb-0 opacity-75"></p>
                </div>
                <small class="opacity-50 text-nowrap">{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</small>
                </div>
            </a>
        '''
    url_news = urlparse(feed.url)
    rss_feed = f'''
            <a href="{url_news.scheme+'://'+url_news.netloc}" class="list-group-item \\ 
            list-group-item-action d-flex gap-3 py-3" aria-current="true">
            <img src="{logo_rss}" alt="rss" width="32" height="32" class="rounded-circle flex-shrink-0">
             {url_news.netloc}
            <div class="d-flex gap-2 w-100 justify-content-between">
                <div>
                    <p class="h2">{feed.feed_title}</p>
                </div>
            </div>
            </a>
            <div class="list-group">
        '''
    f.write(head)
    f.write(rss_feed)

    for item in feed.items:
        for idx, link in enumerate(item.links):
            if is_url_image(link):
                img_link = link

        html_item = f''' 
            <a href="{item.link}" class="list-group-item list-group-item-action d-flex gap-3 py-3" \\ 
            aria-current="true">
                <img src="{img_link}" alt="twbs" width="150" class= flex-shrink-0">
                <div class="d-flex gap-2 w-100 justify-content-between">
                <div>
                    <p class="h5">{item.item_title}</p>
                    <p class="mb-0 opacity-75">{item.description}</p>
                    
                </div>
                <small class="opacity-50 text-nowrap">{item.date}</small>
                </div>
            </a>
            '''
        f.write(html_item)
        for idx, link in enumerate(item.links):
            a_link = f'''
                <a href="{link}" class="list-group-item link-secondary"> <small>[{idx+1}]{link}</small></a>
                '''
            f.write(a_link)

    footer = '''
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"\\
                 integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" \\
                     crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" \\
                integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p"\\
                     crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" \\ 
            integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF"\\
                 crossorigin="anonymous"></script>
            </body>
            </html>
            '''

    f.write(footer)


@log_decorator
def print_HTML(list_feed: ListFeeds, path: str = 'report.html'):
    """[File creation]

    Args:
        list_feed (ListFeeds): [data from rss rss]
        path (str, optional): [name file for output]. Defaults to 'report.html'.
    """
    with open(path, 'w') as f:
        if isinstance(list_feed, ListFeeds):
            for feed in list_feed.feeds:
                output_to(feed, f)
        else:
            output_to(list_feed, f)
