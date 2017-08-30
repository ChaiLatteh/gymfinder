# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-29 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APPNAME', '0003_auto_20170809_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageboard_comment',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messageboard_comments', to='APPNAME.Business'),
        ),
        migrations.AlterField(
            model_name='messageboard_comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messageboard_comments', to='APPNAME.User'),
        ),
    ]
