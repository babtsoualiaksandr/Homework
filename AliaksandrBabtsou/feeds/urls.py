from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feeds import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'feeds', views.FeedViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'links', views.LinkViewSet)
router.register(r'items', views.ItemViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('get_news/', views.get_news_from_url)
]
