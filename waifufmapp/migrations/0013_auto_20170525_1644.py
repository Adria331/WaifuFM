# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0012_auto_20170525_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumreview',
            name='location',
        ),
        migrations.AddField(
            model_name='albumreview',
            name='userlocation',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 25, 16, 44, 25, 616590, tzinfo=utc)),
        ),
    ]
