# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0052_auto_20161206_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idc',
            name='address',
            field=models.CharField(max_length=1000, verbose_name='\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='contact',
            field=models.CharField(max_length=1000, verbose_name='\u8054\u7cfb\u4eba'),
        ),
    ]
