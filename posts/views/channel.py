from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Channel
from posts.serializers import ChannelSerializer


class ChannelListCreateAPIView(ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ChannelSerializer

    queryset = Channel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {
        'title': ['exact']
    }
