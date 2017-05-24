# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0007_auto_20170516_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreview',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 24, 17, 34, 15, 96531, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='albumreview',
            unique_together=set([]),
        ),
    ]
