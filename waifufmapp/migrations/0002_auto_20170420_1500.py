# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='genre',
        ),
        migrations.AddField(
            model_name='album',
            name='Genre',
            field=models.ForeignKey(default=None, to='waifufmapp.Genre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(verbose_name=b'', choices=[(1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
        migrations.AlterField(
            model_name='song',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
