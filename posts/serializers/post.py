from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import Post


class BasePostSerializer(serializers.ModelSerializer):
    up_voted = serializers.SerializerMethodField()
    down_voted = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'title', 'image', 'channel', 'text', 'score', 'up_voted', 'down_voted'
        )
        read_only_fields = ('id', 'up_votes', 'down_votes', 'up_voted', 'down_voted')

    def get_up_voted(self, instance: Post):
        user: User = self.context['request'].user
        return user in instance.up_voted_users

    def get_down_voted(self, instance: Post):
        user: User = self.context['request'].user
        return user in instance.down_voted_users


class PostListCreateSerializer(BasePostSerializer):
    class Meta:
        model = BasePostSerializer.Meta.model
        fields = BasePostSerializer.Meta.fields
        read_only_fields = BasePostSerializer.Meta.read_only_fields


class PostRetrieveSerializer(BasePostSerializer):
    class Meta:
        model = BasePostSerializer.Meta.model
        fields = BasePostSerializer.Meta.fields + ('comments',)
        read_only_fields = BasePostSerializer.Meta.read_only_fields + ('comments',)
