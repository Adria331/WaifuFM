# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0005_auto_20170516_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='area',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='area',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.TextField(max_length=200),
        ),
    ]
