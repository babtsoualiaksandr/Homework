from django.http import response
import requests
from requests.models import Response
from rest_framework import status
from feeds.models import RssReader
from django.http import HttpResponse
from feeds.service import save_news
from django.contrib.auth.models import User


def cron_run(self):
    owner = User.objects.get(username='admin')
    rss_es = RssReader.objects.all()
    for idx, rss in enumerate(rss_es):
        save_news(url=rss.url, limit=None, format='json', user=owner)
    return HttpResponse({"Update news...........       Ok "}, status=200)
