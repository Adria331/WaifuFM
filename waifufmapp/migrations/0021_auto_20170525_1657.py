# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0020_auto_20170525_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreview',
            name='comment',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 25, 16, 57, 22, 347141, tzinfo=utc)),
        ),
    ]
