from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        read_only_fields = ('id',)

    def create(self, validated_data):
        new_user = super().create(validated_data)
        UserProfile.objects.create(user=new_user)
        return new_user
