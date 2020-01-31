from django.core.exceptions import ValidationError
from django.db import models

from posts.models import ContentModel, Post


class Comment(ContentModel):
    parent_comment = models.ForeignKey(
        to='self',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='comments',
        verbose_name='کامنت اصلی'
    )

    parent_post = models.ForeignKey(
        to=Post,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='comments',
        verbose_name='پست اصلی'
    )

    def save(self, *args, **kwargs):
        if self.parent_comment is None and self.parent_post is None:
            raise ValidationError('Comments should have a parent content.')
        super().save(*args, **kwargs)
