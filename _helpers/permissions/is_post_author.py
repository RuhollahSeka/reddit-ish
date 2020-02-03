from rest_framework.permissions import BasePermission

from posts.models import Post


class IsPostAuthor(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        post_id = view.kwargs.get('pk', 0)
        if post_id and isinstance(post_id, int):
            return False
        post = Post.objects.filter(id=post_id).first()
        return post and post.author == user.id
