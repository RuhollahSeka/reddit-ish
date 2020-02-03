from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, 'posts')


urlpatterns = [

]

urlpatterns += router.urls
