from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from _helpers.permissions import IsPostAuthor
from posts.models import Post
from posts.serializers import PostListCreateSerializer


class PostUpdateDestroyAPIView(mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               GenericAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsPostAuthor,)
    serializer_class = PostListCreateSerializer
    queryset = Post.objects.all()
