from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=250, blank=True, default='')
    url_feed = models.CharField(
        max_length=250, blank=True, default='', unique=True)
    owner = models.ForeignKey(
        'auth.User', related_name='feeds', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.url_feed} {self.owner}'

    class Meta:
        ordering = ['url_feed']


class Item(models.Model):
    title = models.CharField(max_length=250, blank=True)
    date = models.CharField(max_length=50, blank=True)
    link_item = models.URLField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    feed = models.ForeignKey(Feed, related_name='items',
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.date} {self.feed}'


class Link(models.Model):
    link = models.URLField(max_length=250, blank=False)
    item = models.ForeignKey(Item, related_name='links',
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.link} {self.item}'


CHOICES_FORMAT_OUTPUT = [
    ('json', 'json'),
    ('html', 'html'),
    ('pdf', 'pdf'),
]


class RssReader(models.Model):
    url = models.URLField(max_length=250, blank=True)
    limit = models.SmallIntegerField(blank=True)
    format = models.CharField(choices=CHOICES_FORMAT_OUTPUT,
                              default='Json', max_length=10)
    owner = models.ForeignKey(
        'auth.User', related_name='Rssreaders', on_delete=models.CASCADE)
    date_req = models.DateField(auto_now=False, auto_now_add=True)
    date_from_db = models.DateField(
        auto_now=False, auto_now_add=False, blank=True)

    def get(self):
        return self.url
