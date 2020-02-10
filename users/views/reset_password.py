from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import UserProfile
from users.throttles import BurstAnonRateThrottle, SustainedAnonRateThrottle


class ResetPasswordAPIView(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = (BurstAnonRateThrottle, SustainedAnonRateThrottle,)

    def post(self, request):
        reset_uuid = self.kwargs['reset_uuid']
        profile = UserProfile.objects.filter(reset_password_uuid=reset_uuid).first()
        if not profile:
            return Response({'details': "User doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
        user = profile.user
        new_password = request.data.get('password')
        user.set_password(new_password)
        return Response({'details': 'Password reset successfully'}, status=status.HTTP_200_OK)
