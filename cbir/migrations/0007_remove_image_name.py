# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 15:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbir', '0006_auto_20160203_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
    ]