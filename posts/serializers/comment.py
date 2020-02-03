from django.contrib.auth.models import User
from rest_framework import serializers

from _helpers.serializers import RecursiveSerializer
from posts.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    comments = RecursiveSerializer(many=True)
    up_voted = serializers.SerializerMethodField()
    down_voted = serializers.SerializerMethodField()
    parent_post = serializers.IntegerField(write_only=True, required=False)
    parent_comment = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Comment
        fields = (
            'id', 'author', 'text', 'score', 'comments', 'up_voted', 'down_voted', 'parent_post', 'parent_comment'
        )
        read_only_fields = ('id', 'score', 'comments', 'up_voted', 'down_voted')

    def get_up_voted(self, instance: Comment):
        user: User = self.context['request'].user
        return user in instance.up_voted_users

    def get_down_voted(self, instance: Comment):
        user: User = self.context['request'].user
        return user in instance.down_voted_users
