# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-11 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0015_pregunta_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
