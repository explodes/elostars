# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import elostars.main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150509_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default=b'male', max_length=128, choices=[(b'male', 'Male'), (b'female', 'Female')]),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(default='', upload_to=elostars.main.models.image_name, verbose_name='image'),
            preserve_default=False,
        ),
    ]
