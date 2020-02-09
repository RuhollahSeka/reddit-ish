from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from _helpers.permissions import IsChannelAdmin
from posts.models import Channel


class AuthorInviteRemoveAPIView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsChannelAdmin,)

    def post(self, request):
        channel = Channel.objects.get(pk=self.kwargs['pk'])
        data = request.data
        user = User.objects.get(id=data['user_id'])
        if data.get('invite', False):
            channel.authors.add(user)
        elif data.get('remove', False):
            channel.authors.remove(user)
        return Response({
            'is_author': channel.authors.filter(id=user.id).exists()
        }, status=status.HTTP_200_OK)
