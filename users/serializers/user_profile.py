from rest_framework import serializers

from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()
    followings_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ('avatar', 'location', 'posts_count', 'followings_count', 'followers_count')
        read_only_fields = ('posts_count', 'followings_count', 'followers_count')

    @staticmethod
    def get_posts_count(instance: UserProfile):
        user = instance.user
        return user.posts.count()

    @staticmethod
    def get_followings_count(instance: UserProfile):
        user = instance.user
        return user.following_channels.count()

    @staticmethod
    def get_followers_count(instance: UserProfile):
        user = instance.user
        channel = user.admin_channels.get(title=user.username)
        return channel.followers.count()
