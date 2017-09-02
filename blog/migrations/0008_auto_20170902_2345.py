# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170902_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='users',
            name='nickname',
            field=models.CharField(max_length=20, unique=True, verbose_name='用户昵称'),
        ),
    ]
