# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-02 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagementSystem', '0008_auto_20181002_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='association',
            name='associationName',
            field=models.CharField(default='AKF', max_length=100),
            preserve_default=False,
        ),
    ]
