from django.db import models

from _helpers.db.models import TimeModel


class ContentModel(TimeModel):
    text = models.TextField(
        verbose_name='متن'
    )

    up_votes = models.PositiveIntegerField(
        default=0,
        verbose_name='تعداد بازخوردهای مثبت'
    )

    down_votes = models.PositiveIntegerField(
        default=0,
        verbose_name='تعداد بازخوردهای منفی'
    )

    @property
    def score(self):
        return self.up_votes - self.down_votes

    class Meta:
        abstract = True
