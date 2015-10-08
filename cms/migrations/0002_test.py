# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
            ],
            options={
                'db_table': 'cms_test',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
