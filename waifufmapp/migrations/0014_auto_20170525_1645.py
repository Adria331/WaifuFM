# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0013_auto_20170525_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreview',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 25, 16, 45, 40, 741394, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='userlocation',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
