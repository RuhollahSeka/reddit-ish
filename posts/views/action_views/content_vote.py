from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Post, Comment


class ContentVoteAPIView(APIView):
    http_method_names = ('post',)
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    model = None

    def post(self, request):
        content = self.model.objects.get(pk=self.kwargs['pk'])
        user = request.user
        data = request.data
        up_voted = False
        down_voted = False
        if data.get('up_vote', False):
            self.up_vote(user, content)
            up_voted = True
        elif data.get('down_vote', False):
            self.down_vote(user, content)
            down_voted = True
        else:
            self.remove_vote(user, content)
        return Response({
            'up_voted': up_voted,
            'down_voted': down_voted,
            'score': content.score
        }, status=status.HTTP_200_OK)

    @staticmethod
    def up_vote(user, content):
        content.down_voted_users.remove(user)
        content.up_voted_users.add(user)

    @staticmethod
    def down_vote(user, content):
        content.up_voted_users.remove(user)
        content.down_voted_users.add(user)

    @staticmethod
    def remove_vote(user, content):
        content.up_voted_users.remove(user)
        content.down_voted_users.remove(user)


class PostVoteAPIView(ContentVoteAPIView):
    model = Post


class CommentVoteAPIView(ContentVoteAPIView):
    model = Comment
