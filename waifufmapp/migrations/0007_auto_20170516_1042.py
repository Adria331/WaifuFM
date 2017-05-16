# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waifufmapp', '0006_auto_20170516_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albumreview',
            old_name='data',
            new_name='date',
        ),
    ]
