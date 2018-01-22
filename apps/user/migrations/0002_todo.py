# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-21 19:41
from __future__ import unicode_literals

import apps.user.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            bases=(apps.user.models.ExtTodo, models.Model),
        ),
    ]
