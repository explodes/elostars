# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import elostars.lib.guid


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0006_picture_guid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='guid',
            field=models.CharField(default=elostars.lib.guid.make_guid,
                unique=True, max_length=128, verbose_name='guid'),
        ),
    ]
