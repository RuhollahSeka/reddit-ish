from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Channel
from posts.serializers import ChannelCreateSerializer, ChannelListRetrieveSerializer


class ChannelListCreateAPIView(ListModelMixin,
                               RetrieveModelMixin,
                               CreateModelMixin,
                               GenericViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Channel.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = {
        'title': ['exact']
    }

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return ChannelCreateSerializer
        return ChannelListRetrieveSerializer
