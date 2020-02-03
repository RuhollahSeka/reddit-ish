from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import Channel


class ChannelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ChannelSerializer(serializers.ModelSerializer):
    authors = ChannelUserSerializer(read_only=True, many=True)
    followers_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Channel
        fields = ('id', 'title', 'summary', 'rules', 'admin', 'authors', 'followers_count')
        read_only_fields = ('id', 'authors', 'followers_count')

    @staticmethod
    def get_followers_count(instance: Channel):
        return instance.followers.count()
