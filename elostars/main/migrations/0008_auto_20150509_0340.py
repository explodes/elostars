# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0007_auto_20150509_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='losses',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='picture',
            name='score',
            field=models.PositiveIntegerField(default=1600),
        ),
        migrations.AddField(
            model_name='picture',
            name='wins',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
