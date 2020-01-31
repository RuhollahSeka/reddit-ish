from django.db import models

from _helpers.db.models import TimeModel


class Notification(TimeModel):
    message = models.CharField(
        max_length=64,
        verbose_name='پیام'
    )

    url = models.URLField(
        verbose_name='لینک هشدار'
    )
