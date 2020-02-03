from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Post
from posts.serializers import PostListCreateSerializer


class ContributedPostsListAPIView(ListAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostListCreateSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(
            Q(comments__author=user) |
            Q(author=user)
        )
