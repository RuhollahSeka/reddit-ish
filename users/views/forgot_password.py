from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.throttles import BurstAnonRateThrottle, SustainedAnonRateThrottle


class ForgotPasswordAPIView(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = (BurstAnonRateThrottle, SustainedAnonRateThrottle)

    def post(self, request):
        username = request.data.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            return Response({'details': 'Wrong username'}, status=status.HTTP_400_BAD_REQUEST)
        email = user.email
        userprofile = user.userprofile
        userprofile.reset_password_uuid = uuid4()
        userprofile.save()
        uuid = userprofile.reset_password_uuid
        message = '''
        To enter your new password, click on the link below 
        127.0.0.1:4200/auth/{}/
        '''.format(uuid)
        send_mail('New Password', message, settings.EMAIL_HOST_USER, email)
