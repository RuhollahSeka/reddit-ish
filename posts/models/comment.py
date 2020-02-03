from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from posts.models import ContentModel, Post


class Comment(ContentModel):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='مولف',
    )

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

    up_voted_users = models.ManyToManyField(
        to=User,
        related_name='up_voted_comments',
        verbose_name='کاربرانی که رای مثبت ثبت کردند'
    )

    down_voted_users = models.ManyToManyField(
        to=User,
        related_name='down_voted_comments',
        verbose_name='کاربرانی که رای منفی ثبت کردند'
    )

    def save(self, *args, **kwargs):
        if self.parent_comment is None and self.parent_post is None:
            raise ValidationError('Comments should have a parent content.')
        if self.parent_comment and self.parent_post:
            raise ValidationError('Comments should have only one parent content.')
        super().save(*args, **kwargs)
