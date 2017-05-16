# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('waifufmapp', '0003_auto_20170421_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('rating', models.PositiveSmallIntegerField(verbose_name='', choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')])),
                ('album', models.ForeignKey(to='waifufmapp.Album')),
                ('song', models.ForeignKey(to='waifufmapp.Song')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='song',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AlterUniqueTogether(
            name='albumreview',
            unique_together=set([('album', 'user')]),
        ),
    ]
