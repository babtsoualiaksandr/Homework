from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feeds.views import RegisterView
from feeds import views
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'feeds', views.FeedViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'links', views.LinkViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'rss_reader', views.RssReaderViewSet)
router.register(r'register', views.RegisterView)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
