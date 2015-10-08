# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('email', models.CharField(max_length=128, blank=True)),
                ('username', models.CharField(max_length=256, blank=True)),
                ('password', models.CharField(max_length=255, blank=True)),
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
                ('is_deleted', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'test',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
