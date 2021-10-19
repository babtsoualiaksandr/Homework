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


    def test_rss_create(self):
        response = self.client.get('/rss_reader/')
        rsses = RssReader.objects.all()
        print(rsses, '1'*11)

        serializer = RssReaderSerializer(rsses, many=True)
        print('serializer.data', serializer.data, )
        print('response.data', response.data['results'])

        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
