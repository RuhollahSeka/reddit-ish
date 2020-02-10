from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Channel
from posts.serializers import ChannelListRetrieveSerializer


class UserChannelsListAPIView(ListAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ChannelListRetrieveSerializer

    def get_queryset(self):
        user = self.request.user
        return Channel.objects.filter(admin=user)
