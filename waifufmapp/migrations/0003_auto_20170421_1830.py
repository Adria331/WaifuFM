# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0002_auto_20170420_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(null=True, upload_to=b'picture_artist', blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='area',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='artist',
            name='area',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]
