from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Post
from posts.serializers import PostRetrieveSerializer, PostListCreateSerializer


class PostViewSet(ModelViewSet):
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return PostRetrieveSerializer
        return PostListCreateSerializer

    def get_queryset(self):
        channel_id = self.kwargs.get('channel_id')
        ordering_type = self.request.query_params.get('ordering')
        ordering_type = ['-' + ordering_type] if ordering_type else []
        channel_filter = {'channel_id': channel_id} if channel_id else {}
        return Post.objects.filter(**channel_filter).order_by(*ordering_type)
