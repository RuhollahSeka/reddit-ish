# Generated by Django 2.2.9 on 2020-02-01 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='reset_password_uuid',
            field=models.UUIDField(blank=True, null=True, verbose_name='کد مربوط به لینک فراموشی رمز'),
        ),
    ]