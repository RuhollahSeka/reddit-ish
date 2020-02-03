from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from _helpers.permissions import IsChannelAuthor
from posts.serializers import PostListCreateSerializer


class PostCreateAPIView(CreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsChannelAuthor,)
    serializer_class = PostListCreateSerializer
