# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_encoded_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='encoded_image',
            field=models.CharField(max_length=1000000),
        ),
    ]