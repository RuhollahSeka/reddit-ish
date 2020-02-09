from rest_framework.generics import UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from _helpers.permissions import IsChannelAdmin
from posts.serializers import ChannelAdminSerializer


class ChannelUpdateAPIView(UpdateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsChannelAdmin,)
    serializer_class = ChannelAdminSerializer
