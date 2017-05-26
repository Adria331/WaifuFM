# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0022_auto_20170525_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Genre',
            field=models.ForeignKey(default=None, to='waifufmapp.Genre', null=True),
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 25, 19, 17, 16, 632009, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='artist',
            name='location',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
