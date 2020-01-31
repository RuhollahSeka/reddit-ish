from django.db import models


class TimeModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ساخت'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ تغییر'
    )

    class Meta:
        get_latest_by = '-created'
        abstract = True
