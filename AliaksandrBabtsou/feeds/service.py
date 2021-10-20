
from datetime import datetime
from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import generics, status
from feeds.serializers import FeedSerializer, ItemSerializer
from feeds.models import Feed, Item, Link
from rss_reader import get_news_from_url
from feeds.models import Item, Feed
from dateutil.parser import parse


def save_news(url, limit, format, user):

    try:
        _feed = get_news_from_url(url=url, limit=limit, format=format)
        print(len(_feed.items), 'len =====')
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


def equal_date(date_str: str, date_filter: str) -> bool:
    dt = parse(date_str)
    dt_filter = datetime.strptime(date_filter, '%Y%m%d')
    dt_str = f'{dt.year}{dt.month}{dt.day}'
    dt_filter_str = f'{dt_filter.year}{dt_filter.month}{dt_filter.day}'
    if dt_str == dt_filter_str:
        return True
    else:
        return False


def get_news(req):
    url = req.GET.get('url')
    date = req.GET.get('date')
    if (url and date is None):
        try:
            news = Feed.objects.get(url_feed=url)
        except Exception as err:
            return HttpResponse({f"Not found {url}"}, status=status.HTTP_404_NOT_FOUND)
        serializer = FeedSerializer(
            news, many=False, context={'request': req})
        response = Response(
            serializer.data,
            content_type="application/json",
            status=status.HTTP_200_OK,
        )
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
    elif (url is None and date):
        news = Item.objects.all()        
        news_date = [item for item in Item.objects.all(
        ) if equal_date(item.date, date)]
        if news_date is None:
            return HttpResponse({f"Not found {date}"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(
            news_date, many=True, context={'request': req})
        response = Response(
            serializer.data,
            content_type="application/json",
            status=status.HTTP_200_OK,
        )
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
    elif (url and date):
        news = Item.objects.all()
        news_date = [item for item in Item.objects.all(
        ) if equal_date(item.date, date)]
        if news_date is None:
            return HttpResponse({f"Not found {date}"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(
            news_date, many=True, context={'request': req})
        response = Response(
            serializer.data,
            content_type="application/json",
            status=status.HTTP_200_OK,
        )
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
    else:
        return HttpResponse({"OK??"}, status=222)
