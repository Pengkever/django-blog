# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-03 06:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_time',
            new_name='created_time',
        ),
    ]