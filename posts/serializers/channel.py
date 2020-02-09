from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import Channel


class ChannelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class BaseChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = ('id', 'title', 'summary', 'rules',)
        read_only_fields = ('id',)


class ChannelCreateSerializer(BaseChannelSerializer):
    class Meta:
        model = BaseChannelSerializer.Meta.model
        fields = BaseChannelSerializer.Meta.fields + ('admin',)
        read_only_fields = BaseChannelSerializer.Meta.read_only_fields


class ChannelListRetrieveSerializer(BaseChannelSerializer):
    authors = ChannelUserSerializer(read_only=True, many=True)
    followers_count = serializers.SerializerMethodField(read_only=True)
    is_follower = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Channel
        fields = BaseChannelSerializer.Meta.fields + ('admin', 'authors', 'followers_count', 'is_follower')
        read_only_fields = BaseChannelSerializer.Meta.read_only_fields + ('authors', 'followers_count')

    @staticmethod
    def get_followers_count(instance: Channel):
        return instance.followers.count()

    def get_is_follower(self, instance: Channel):
        user_id = self.context['request'].user.id
        return instance.followers.filter(id=user_id).exists()


class ChannelAdminSerializer(BaseChannelSerializer):
    class Meta:
        model = Channel
        fields = BaseChannelSerializer.Meta.fields
        read_only_fields = BaseChannelSerializer.Meta.read_only_fields
