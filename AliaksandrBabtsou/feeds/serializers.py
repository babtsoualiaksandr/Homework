from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from feeds.models import RssReader
from feeds.models import Feed, Item, Link
from django.contrib.auth.models import User


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    def create(self, validated_data):
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


class RssReaderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = RssReader
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
