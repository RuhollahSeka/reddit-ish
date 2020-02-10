from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet, CommentListCreateAPIView, ContributedPostsListAPIView, CreatedPostsListAPIView, \
    FollowingPostsListAPIView, PostCreateAPIView, PostUpdateDestroyAPIView, ChannelListCreateAPIView, \
    AuthorInviteRemoveAPIView, ChannelFollowAPIView, PostVoteAPIView, ChannelUpdateAPIView, CommentVoteAPIView, \
    UserChannelsListAPIView, ChannelRetrieveAPIView

router = DefaultRouter()
router.register('posts', PostViewSet, 'posts')
router.register('channels', ChannelListCreateAPIView, 'channels')


urlpatterns = [
    path('posts/comments/', CommentListCreateAPIView.as_view()),

    path('contributed-posts/', ContributedPostsListAPIView.as_view()),
    path('created-posts/', CreatedPostsListAPIView.as_view()),
    path('following-posts/', FollowingPostsListAPIView.as_view()),
    path('post/', PostCreateAPIView.as_view()),
    path('post/<int:pk>/', PostUpdateDestroyAPIView.as_view()),

    path('channels/<int:pk>/', ChannelUpdateAPIView.as_view()),
    path('channel/<int:pk>/', ChannelRetrieveAPIView.as_view()),
    path('user-channels/', UserChannelsListAPIView.as_view()),

    path('channels/<int:pk>/invite/', AuthorInviteRemoveAPIView.as_view()),
    path('follow-channel/', ChannelFollowAPIView.as_view()),
    path('posts/<int:pk>/vote/', PostVoteAPIView.as_view()),
    path('comments/<int:pk>/vote/', CommentVoteAPIView.as_view()),
]

urlpatterns += router.urls
