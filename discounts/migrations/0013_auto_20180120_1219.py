# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0012_auto_20180120_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='credit_available',
            field=models.IntegerField(default=1000),
        ),
    ]
