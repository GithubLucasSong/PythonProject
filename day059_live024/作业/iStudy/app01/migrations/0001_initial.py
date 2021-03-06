# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-03 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('position', models.CharField(max_length=32, verbose_name='职位')),
                ('company', models.CharField(blank=True, choices=[('1', '北京总公司'), ('2', '上海分公司'), ('3', '广州分公司')], max_length=32, verbose_name='公司')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('last_login_time', models.DateTimeField(blank=True, null=True, verbose_name='上次登录时间')),
                ('register_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
            ],
        ),
    ]
