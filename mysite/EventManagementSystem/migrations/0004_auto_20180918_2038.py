# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-18 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagementSystem', '0003_user_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_type',
            new_name='userType',
        ),
    ]
