# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-28 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logReg_app', '0001_initial'),
        ('travels_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='dest',
            new_name='destination',
        ),
        migrations.AddField(
            model_name='trip',
            name='all_users',
            field=models.ManyToManyField(related_name='all_trips', to='logReg_app.User'),
        ),
    ]
