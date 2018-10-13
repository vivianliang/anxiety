# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-13 22:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anxiety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fear', models.TextField(max_length=2048)),
                ('action', models.TextField(max_length=2048)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anxieties', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
