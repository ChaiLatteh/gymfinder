# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-26 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPNAME', '0017_auto_20170725_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.FileField(null=True, upload_to='v/t31.0-8'),
        ),
    ]
