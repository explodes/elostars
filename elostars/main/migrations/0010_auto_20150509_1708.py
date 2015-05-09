# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150509_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='view_gender',
            field=models.CharField(default=b'both', max_length=128, choices=[(b'both', 'Both'), (b'male', 'Male'), (b'female', 'Female')]),
        ),
        migrations.AlterField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(related_name='pictures', to=settings.AUTH_USER_MODEL),
        ),
    ]
