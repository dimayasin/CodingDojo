# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-26 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20180226_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='banana',
            new_name='user',
        ),
    ]
