from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.serializers.user_profile import UserProfileSerializer


class UserProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
