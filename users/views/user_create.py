from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer
from users.throttles import BurstAnonRateThrottle, SustainedAnonRateThrottle


class UserCreateAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    throttle_classes = (BurstAnonRateThrottle, SustainedAnonRateThrottle)


