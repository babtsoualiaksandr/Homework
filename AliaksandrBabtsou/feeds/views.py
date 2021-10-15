from django.http.response import JsonResponse
from rest_framework import status
from feeds.permissions import IsOwnerOrReadOnly
from feeds.models import Feed, Item, Link
from feeds.serializers import FeedSerializer, UserSerializer, ItemSerializer, LinkSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets


from rss_reader import get_all_news_from_url


class FeedViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        print(self.request)
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LinkViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def get_news_from_url(request):
    """
    Retrieve, update or delete a code snippet.
    """
    if request.method == 'GET':
        try:
            _feed = get_all_news_from_url(
                url="https://news.un.org/feed/subscribe/en/news/topic/health/feed/rss.xml", limit=13)
        except Exception as err:
            print(err)
        try:
            new_feed = generics.get_object_or_404(Feed, url_feed=_feed.url)
        except Exception as err:
            print(err)
            new_feed = Feed(url_feed=_feed.url,
                            title=_feed.feed_title, owner=request.user)
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
        result_feed = generics.get_object_or_404(Feed, url_feed=_feed.url)

        serializer = FeedSerializer(result_feed, context={'request': request})
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
