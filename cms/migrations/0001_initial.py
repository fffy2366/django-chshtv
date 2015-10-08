# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
            ],
            options={
                'db_table': 'cms_admin',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'db_table': 'cms_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
