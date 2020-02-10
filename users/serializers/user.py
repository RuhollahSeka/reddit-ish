from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import Channel
from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        read_only_fields = ('id',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        new_user = super().create(validated_data)
        new_user.set_password(password)
        new_user.save()
        UserProfile.objects.create(user=new_user)
        Channel.objects.create(admin=new_user, title=new_user.username)
        return new_user
