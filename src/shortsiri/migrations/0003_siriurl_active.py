# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-21 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortsiri', '0002_auto_20180920_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='siriurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
