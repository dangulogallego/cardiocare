# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-11 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0018_auto_20171011_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntajecategoria',
            name='categoria',
            field=models.IntegerField(default=1),
        ),
    ]
