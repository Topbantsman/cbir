# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbir', '0007_remove_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]