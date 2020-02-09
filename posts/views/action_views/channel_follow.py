from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Channel


class ChannelFollowAPIView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        data = request.data
        channel = Channel.objects.get(id=data['channel_id'])
        if data.get('follow', False):
            channel.followers.add(user)
            is_follower = True
        else:
            channel.followers.remove(user)
            is_follower = False
        return Response({
            'is_follower': is_follower
        }, status=status.HTTP_200_OK)
