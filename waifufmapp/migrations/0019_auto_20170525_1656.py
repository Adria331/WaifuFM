# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0018_auto_20170525_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumreview',
            name='userlocation',
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 25, 16, 56, 12, 450113, tzinfo=utc)),
        ),
    ]
