from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserCreateAPIView
from users.views.user_profile import UserProfileRetrieveUpdateAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserCreateAPIView.as_view()),
    path('profiles/', UserProfileRetrieveUpdateAPIView.as_view()),
]
