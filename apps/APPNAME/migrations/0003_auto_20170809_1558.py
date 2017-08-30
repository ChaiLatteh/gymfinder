# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-09 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APPNAME', '0002_meetup_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup_bookmark',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetup_bookmarks', to='APPNAME.Business'),
        ),
        migrations.AddField(
            model_name='meetup_like',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetup_likes', to='APPNAME.Business'),
        ),
        migrations.AddField(
            model_name='messageboard_message_bookmark',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messageboard_message_bookmarks', to='APPNAME.Business'),
        ),
        migrations.AddField(
            model_name='messageboard_message_like',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messageboard_message_likes', to='APPNAME.Business'),
        ),
        migrations.AlterField(
            model_name='meetup_bookmark',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetup_bookmarks', to='APPNAME.User'),
        ),
        migrations.AlterField(
            model_name='meetup_like',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetup_likes', to='APPNAME.User'),
        ),
        migrations.AlterField(
            model_name='messageboard_message_bookmark',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messageboard_message_bookmarks', to='APPNAME.User'),
        ),
        migrations.AlterField(
            model_name='messageboard_message_like',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messageboard_message_likes', to='APPNAME.User'),
        ),
    ]
