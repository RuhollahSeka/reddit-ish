from rest_framework.permissions import BasePermission

from posts.models import Channel


class IsChannelAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        channel_id = view.kwargs.get('pk', 0)
        if not channel_id or not isinstance(channel_id, int):
            return False
        channel = Channel.objects.filter(id=channel_id).first()
        return channel and channel.admin == user
