# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('whenans', models.DateTimeField(verbose_name=b'last time answered')),
                ('correct', models.BooleanField(verbose_name=b'answer was correct?')),
                ('nexttime', models.DateTimeField(verbose_name=b'the next time we show this question to this user')),
                ('question', models.ForeignKey(to='adaptapp.Question')),
                ('user', models.ForeignKey(to='adaptapp.User')),
            ],
        ),
    ]
