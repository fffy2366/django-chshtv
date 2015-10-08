# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20151003_1442'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
