from django.contrib import admin


from .models import Feed, RssReader

# Register your models here.
admin.site.register(Feed)
admin.site.register(RssReader)
