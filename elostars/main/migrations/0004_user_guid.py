# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import elostars.main.models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_auto_20150509_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='guid',
            field=models.CharField(default=elostars.main.models.make_guid,
                max_length=128, verbose_name='guid'),
        ),
    ]
