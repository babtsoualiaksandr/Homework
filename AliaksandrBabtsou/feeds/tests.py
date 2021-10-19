from django.test import TestCase
from django.test.client import RequestFactory, Client
from rest_framework import status

# Create your tests here
from django.contrib.auth.models import User

from feeds.serializers import RssReaderSerializer

from feeds.models import RssReader


class RssReaderTest(TestCase):
    """ Test module for Rss_reader model """

    def setUp(self):
        User.objects.create(username='epam')
        user = User.objects.get(username='epam')
        RssReader.objects.create(
            url='https://news.un.org/feed/subscribe/en/news/all/rss.xml',
            limit=1, format='json', date_from_db='2021-10-19', owner=user)
        RssReader.objects.create(
            url='https://news.un.org/feed/subscribe/en/news/all/rss.xml2',
            limit=12, format='json', date_from_db='2021-10-20', owner=user)

    def test_rss_all(self):
        response = self.client.get('/rss_reader/')
        rsses = RssReader.objects.all()
        serializer = RssReaderSerializer(rsses, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data['results'])

    def test_rss_get_one(self):
        response = self.client.get('/rss_reader/')
        print('response.status_code', response.status_code)
        rsses = RssReader.objects.filter(id=1)
        serializer = RssReaderSerializer(rsses, many=False)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rss_get_post(self):
        response = self.client.post('/rss_reader/3/',
                                    {"url": 'https://news.un.org/feed/subscribe/en/news/all/rss.xml3',
                                     'limit': 12, 'format': 'json', 'date_from_db': '2021-10-20'})
        print('response.status_code', response.status_code)        
        rsses = RssReader.objects.filter(id=3)
        serializer = RssReaderSerializer(rsses, many=False)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
