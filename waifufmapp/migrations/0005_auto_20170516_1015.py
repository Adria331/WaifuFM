# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0004_auto_20170516_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumreview',
            name='song',
        ),
        migrations.AddField(
            model_name='albumreview',
            name='comment',
            field=models.TextField(null=True, blank=True),
        ),
    ]
