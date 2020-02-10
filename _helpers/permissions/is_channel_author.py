from rest_framework.permissions import BasePermission

from posts.models import Channel


class IsChannelAuthor(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        channel_id = request.data.get('channel', 0)
        if not channel_id or not isinstance(channel_id, int):
            return False
        channel = Channel.objects.filter(id=channel_id).first()
        return channel and (channel.authors.filter(id=user.id).exists() or channel.admin == user)
