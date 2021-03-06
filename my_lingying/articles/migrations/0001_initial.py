# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-22 17:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('content', models.CharField(max_length=500, verbose_name='动态内容')),
                ('passport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Passport', verbose_name='发动态者')),
            ],
            options={
                'db_table': 'articles',
            },
        ),
    ]
