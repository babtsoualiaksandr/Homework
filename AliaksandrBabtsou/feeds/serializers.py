from rest_framework import serializers
from feeds.models import Feed, Item, Link
from django.contrib.auth.models import User


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    def create(self, validated_data):
        print(validated_data)
        super(self, validated_data)

    def create(self, validated_data):
        links = validated_data.pop('links', [])
        instance = Item.objects.create(**validated_data)
        for link_data in links:
            link = Link.create(link_data)
            instance.links.add(link)
        return instance

    class Meta:
        model = Item
        fields = "__all__"
        extra_kwargs = {'links': {'required': False}}


class FeedSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    items = ItemSerializer(many=True, read_only=False)

    class Meta:
        model = Feed
        fields = "__all__"
        extra_kwargs = {'items': {'required': False}}


class UserSerializer(serializers.HyperlinkedModelSerializer):
    feeds = serializers.HyperlinkedRelatedField(
        many=True, view_name='feed-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'feeds']
