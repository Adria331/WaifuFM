# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0023_auto_20170525_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreview',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 25, 19, 18, 47, 42702, tzinfo=utc)),
        ),
    ]
