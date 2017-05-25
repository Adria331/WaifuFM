# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0009_auto_20170524_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumreview',
            name='location',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 25, 16, 42, 50, 698261, tzinfo=utc)),
        ),
    ]
