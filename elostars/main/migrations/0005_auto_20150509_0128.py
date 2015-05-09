# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import elostars.main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_user_guid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='guid',
            field=models.CharField(default=elostars.main.models.make_guid, unique=True, max_length=128, verbose_name='guid'),
        ),
    ]
