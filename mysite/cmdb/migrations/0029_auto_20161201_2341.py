# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0028_prarttype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelconf',
            name='mmodel',
        ),
        migrations.AlterModelOptions(
            name='prarttype',
            options={'verbose_name': '/Meta/\u914d\u4ef6\u7c7b\u522b', 'verbose_name_plural': '/Meta/\u914d\u4ef6\u7c7b\u522b'},
        ),
        migrations.AlterField(
            model_name='prarttype',
            name='type',
            field=models.CharField(help_text='\u5fc5\u987b\u552f\u4e00&\u4e0d\u80fd\u4e3a\u7a7a', max_length=255, unique=True, verbose_name='\u914d\u4ef6\u7c7b\u522b'),
        ),
        migrations.DeleteModel(
            name='BrandModel',
        ),
        migrations.DeleteModel(
            name='ModelConf',
        ),
    ]
