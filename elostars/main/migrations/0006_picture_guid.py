# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import elostars.lib.guid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150509_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='guid',
            field=models.CharField(default=elostars.lib.guid.make_guid, max_length=128, verbose_name='guid'),
        ),
    ]
