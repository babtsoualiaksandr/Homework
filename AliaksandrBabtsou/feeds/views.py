from django.http.request import HttpRequest
import rest_framework
from rest_framework import request
from rest_framework.renderers import StaticHTMLRenderer
from feeds.service import save_news
from feeds.serializers import RegisterSerializer
from feeds.models import RssReader
from feeds.serializers import RssReaderSerializer
from django.http.response import HttpResponse, JsonResponse, ResponseHeaders
from rest_framework import status
from feeds.permissions import IsOwnerOrReadOnly
from feeds.models import Feed, Item, Link
from feeds.serializers import FeedSerializer, UserSerializer, ItemSerializer, LinkSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request


from rss_reader import get_news_from_url


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

    @action(detail=False, methods=['Post'])
    def get_news(self, request: Request, pk=None):
        news = save_news(url=request.data['url'],
                         limit=int(request.data['limit']), format=request.data['format'], user=request.user)
        serializer = FeedSerializer(
            news, many=True, context={'request': request})
        if request.data['format'] == 'pdf':
            with open("report.pdf", 'rb') as pdf_report:
                response = HttpResponse(
                    pdf_report, content_type='application/pdf')
                filename = "report.pdf"
                response['Content-Disposition'] = 'attachment; filename="{}"'.format(
                    filename)
                return response

        if request.data['format'] == 'html':
            with open("report.html", 'r') as html_report:
                response = HttpResponse(
                    html_report, content_type='application/html')
                filename = "report.html"
                response['Content-Disposition'] = 'attachment; filename="{}"'.format(
                    filename)
                return response

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


