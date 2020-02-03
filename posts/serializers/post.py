from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import Post
from posts.serializers import CommentSerializer


class BasePostSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(read_only=True)
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
        return instance.up_voted_users.filter(id=user.id).exists()

    def get_down_voted(self, instance: Post):
        user: User = self.context['request'].user
        return instance.down_voted_users.filter(id=user.id).exists()


class PostListCreateSerializer(BasePostSerializer):
    class Meta:
        model = BasePostSerializer.Meta.model
        fields = BasePostSerializer.Meta.fields
        read_only_fields = BasePostSerializer.Meta.read_only_fields


class PostRetrieveSerializer(BasePostSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = BasePostSerializer.Meta.model
        fields = BasePostSerializer.Meta.fields + ('comments',)
        read_only_fields = BasePostSerializer.Meta.read_only_fields + ('comments',)
