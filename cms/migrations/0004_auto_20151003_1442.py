# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20151003_1441'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
                ('is_admin', models.IntegerField(null=True, blank=True)),
                ('is_deleted', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'cms_admin',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.CreateModel(
            name='User',
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
                'db_table': 'cms_user',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
