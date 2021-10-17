
from rest_framework import generics
from feeds.models import Feed, Item, Link
from rss_reader import get_news_from_url


def save_news(url, limit, format, user):
    print(format, '#'*123)
    try:
        _feed = get_news_from_url(url=url, limit=limit, format=format)
    except Exception as err:
        print(err)
    try:
        new_feed = generics.get_object_or_404(Feed, url_feed=_feed.url)
    except Exception as err:
        print(err)
        new_feed = Feed(url_feed=_feed.url,
                        title=_feed.feed_title, owner=user)
        new_feed.save()

    for item in _feed.items:
        try:
            new_item = generics.get_object_or_404(
                Item, link_item=item.link, feed=new_feed)
        except Exception as err:
            print(err)
            new_item = Item(title=item.item_title, date=item.date,
                            link_item=item.link, description=item.description)
        new_item.feed = new_feed
        new_item.save()
        for link in item.links:
            try:
                new_link = generics.get_object_or_404(
                    Link, link=link, item=new_item)
            except Exception as err:
                print(err)
                new_link = Link(link=link)
                new_link.item = new_item
            new_link.save()
        news = Feed.objects.filter(url_feed=url)
        return news
