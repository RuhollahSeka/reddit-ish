from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Comment
from posts.serializers import CommentSerializer


class CommentListCreateAPIView(ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
