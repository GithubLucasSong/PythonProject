# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-15 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('classs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Class')),
            ],
        ),
    ]
