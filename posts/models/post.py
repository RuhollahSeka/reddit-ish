from decouple import config
from django.db import models

from _helpers.db.utils import RenameOnUpload
from posts.models import ContentModel, Channel


class Post(ContentModel):
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
