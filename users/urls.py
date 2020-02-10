from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserCreateAPIView, UserProfileRetrieveUpdateAPIView, ForgotPasswordAPIView
from users.views.reset_password import ResetPasswordAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserCreateAPIView.as_view()),
    path('profiles/', UserProfileRetrieveUpdateAPIView.as_view()),
    path('forgot-password/', ForgotPasswordAPIView.as_view()),
    path('reset-password/<uuid:reset_uuid>/', ResetPasswordAPIView.as_view()),
]
