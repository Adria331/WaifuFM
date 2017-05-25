# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0010_auto_20170525_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreview',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 25, 16, 43, 15, 57751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='location',
            field=models.TextField(default='', max_length=100),
        ),
    ]
