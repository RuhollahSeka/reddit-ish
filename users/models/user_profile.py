from decouple import config
from django.contrib.auth.models import User
from django.db import models

from _helpers.db.models import TimeModel
from _helpers.db.utils import RenameOnUpload


class UserProfile(TimeModel):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
    )

    avatar = models.ImageField(
        upload_to=RenameOnUpload(config('PROFILE_IMAGES_DIR')),
        null=True,
        blank=True,
        verbose_name='عکس پروفایل'
    )

    location = models.CharField(
        max_length=32,
        blank=True,
        verbose_name='مکان'
    )

    reset_password_uuid = models.UUIDField(
        verbose_name='کد مربوط به لینک فراموشی رمز'
    )
