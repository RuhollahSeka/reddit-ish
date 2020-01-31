from django.contrib.auth.models import User
from django.db import models

from _helpers.db.models import TimeModel


class Channel(TimeModel):
    title = models.CharField(
        max_length=32,
        verbose_name='عنوان کانال'
    )

    summary = models.TextField(
        verbose_name='توضیحات'
    )

    rules = models.TextField(
        verbose_name='قوانین'
    )

    admin = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='admin_channels',
        verbose_name='مدیر کانال'
    )

    authors = models.ManyToManyField(
        to=User,
        related_name='author_channels',
        verbose_name='مولفان کانال'
    )

    followers = models.ManyToManyField(
        to=User,
        related_name='following_channels',
        verbose_name='دنبال‌کنندگان'
    )
