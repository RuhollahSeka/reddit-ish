from decouple import config
from django.contrib.auth.models import User
from django.db import models

from _helpers.db.utils import RenameOnUpload
from posts.models import ContentModel, Channel


class Post(ContentModel):
    title = models.CharField(
        max_length=32,
        verbose_name='عنوان پست'
    )

    image = models.ImageField(
        upload_to=RenameOnUpload(config('POST_IMAGES_DIR')),
        null=True,
        blank=True,
        verbose_name='عکس پست'
    )

    channel = models.ForeignKey(
        to=Channel,
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name='کانال'
    )

    up_voted_users = models.ManyToManyField(
        to=User,
        related_name='up_voted_posts',
        verbose_name='کاربرانی که رای مثبت ثبت کردند'
    )

    down_voted_users = models.ManyToManyField(
        to=User,
        related_name='down_voted_posts',
        verbose_name='کاربرانی که رای منفی ثبت کردند'
    )
