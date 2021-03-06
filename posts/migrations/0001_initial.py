# Generated by Django 2.2.9 on 2020-01-31 18:08

import _helpers.db.utils.rename_on_upload
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر')),
                ('title', models.CharField(max_length=32, verbose_name='عنوان کانال')),
                ('summary', models.TextField(verbose_name='توضیحات')),
                ('rules', models.TextField(verbose_name='قوانین')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='admin_channels', to=settings.AUTH_USER_MODEL, verbose_name='مدیر کانال')),
                ('authors', models.ManyToManyField(related_name='author_channels', to=settings.AUTH_USER_MODEL, verbose_name='مولفان کانال')),
                ('followers', models.ManyToManyField(related_name='following_channels', to=settings.AUTH_USER_MODEL, verbose_name='دنبال\u200cکنندگان')),
            ],
            options={
                'get_latest_by': '-created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر')),
                ('text', models.TextField(verbose_name='متن')),
                ('up_votes', models.PositiveIntegerField(default=0, verbose_name='تعداد بازخوردهای مثبت')),
                ('down_votes', models.PositiveIntegerField(default=0, verbose_name='تعداد بازخوردهای منفی')),
                ('image', models.ImageField(blank=True, null=True, upload_to=_helpers.db.utils.rename_on_upload.RenameOnUpload('/images/posts/'), verbose_name='عکس پست')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='posts.Channel', verbose_name='کانال')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر')),
                ('text', models.TextField(verbose_name='متن')),
                ('up_votes', models.PositiveIntegerField(default=0, verbose_name='تعداد بازخوردهای مثبت')),
                ('down_votes', models.PositiveIntegerField(default=0, verbose_name='تعداد بازخوردهای منفی')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='posts.Comment', verbose_name='کامنت اصلی')),
                ('parent_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='posts.Post', verbose_name='پست اصلی')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
