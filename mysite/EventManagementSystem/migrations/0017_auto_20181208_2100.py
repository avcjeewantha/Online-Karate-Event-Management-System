# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-08 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagementSystem', '0016_auto_20181208_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='kumite',
            field=models.BooleanField(choices=[(True, 'Kumite'), (False, 'Kata')], default=True, verbose_name='Event Category'),
        ),
    ]
