# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-14 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anxiety',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='anxiety',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
