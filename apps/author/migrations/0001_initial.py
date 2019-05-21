# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-05-05 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthoerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='姓名')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='电子邮箱')),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'female'), (1, 'male')], null=True, verbose_name='性别')),
                ('avater', models.ImageField(upload_to='avater', verbose_name='头像')),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者列表',
            },
        ),
    ]
