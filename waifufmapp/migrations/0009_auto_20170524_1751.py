# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0008_auto_20170524_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreview',
            name='comment',
            field=models.TextField(default='No Comment', blank=True),
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 24, 17, 51, 31, 794600, tzinfo=utc)),
        ),
    ]
