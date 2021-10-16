import rest_framework
from feeds.serializers import RegisterSerializer
from feeds.models import RssReader
from feeds.serializers import RssReaderSerializer
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
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


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


class RssReaderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = RssReader.objects.all()
    serializer_class = RssReaderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        print(self.request)
        print(serializer)
        try:
            _feed = get_all_news_from_url(
                url=serializer.data['url'], limit=serializer.data['limit'])
        except Exception as err:
            print(err)
        try:
            new_feed = generics.get_object_or_404(Feed, url_feed=_feed.url)
        except Exception as err:
            print(err)
            new_feed = Feed(url_feed=_feed.url,
                            title=_feed.feed_title, owner=self.request.user)
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
