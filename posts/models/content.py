from django.db import models

from _helpers.db.models import TimeModel


class ContentModel(TimeModel):
    text = models.TextField(
        verbose_name='متن'
    )

    up_voted_users = None

    down_voted_users = None

    archived = models.BooleanField(
        default=False,
        verbose_name='آرشیو شده'
    )

    @property
    def up_votes(self):
        return self.up_voted_users.count()

    @property
    def down_votes(self):
        return self.down_voted_users.count()

    @property
    def score(self):
        return self.up_votes - self.down_votes

    class Meta:
        abstract = True
