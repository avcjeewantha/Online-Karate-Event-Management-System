# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-05 05:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagementSystem', '0011_auto_20181003_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='districtName',
        ),
        migrations.RemoveField(
            model_name='province',
            name='provinceName',
        ),
    ]
