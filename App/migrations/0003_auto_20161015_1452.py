# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-15 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20161015_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modeluser',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
    ]
