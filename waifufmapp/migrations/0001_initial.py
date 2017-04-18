# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('area', models.TextField()),
                ('year', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('area', models.TextField()),
                ('biography', models.TextField(max_length=20000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('rating', models.PositiveSmallIntegerField(verbose_name=b'', choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five')])),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('date', models.DateField()),
                ('author', models.ForeignKey(to='waifufmapp.Artist')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='song',
            field=models.ForeignKey(to='waifufmapp.Song'),
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(to='waifufmapp.Genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ForeignKey(to='waifufmapp.Artist'),
        ),
    ]
