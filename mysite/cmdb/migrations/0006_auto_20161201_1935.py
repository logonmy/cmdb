# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_auto_20161201_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='provider',
            name='pmbnum',
            field=models.CharField(max_length=255, verbose_name='\u4f9b\u5e94\u5546\u624b\u673a'),
        ),
    ]
