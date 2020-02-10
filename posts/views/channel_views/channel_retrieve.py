from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Channel
from posts.serializers import ChannelListRetrieveSerializer


class ChannelRetrieveAPIView(RetrieveAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ChannelListRetrieveSerializer
    queryset = Channel.objects.all()
