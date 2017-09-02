# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170902_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=12, unique=True, verbose_name='用户名')),
                ('user_password', models.CharField(max_length=20, verbose_name='密码')),
                ('nickname', models.CharField(max_length=10, unique=True, verbose_name='用户昵称')),
                ('user_type', models.SmallIntegerField(max_length=3)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-post_time'], 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Users'),
        ),
    ]
